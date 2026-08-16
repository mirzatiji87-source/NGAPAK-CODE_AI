import markdown
import random
import os
import zipfile
from flask import Flask, render_template, request, session, redirect, send_file
from checker import cek_pakai_ai
from dialect import get_pesan_pembuka, terjemahkan_error
from database import read_questions, get_question_by_id,  create_question, update_question,  delete_question
from config import ADMIN_PASSWORD, SECRET_KEY

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cek-error", methods=["GET", "POST"])
def cek_error():
    if request.method == "POST":
        kode_user = request.form["kode_user"]
        bahasa_program = request.form["bahasa_program"]
        bahasa_mkd = request.form["bahasa_mkd"]
        gaya = request.form["gaya"]

        pembuka = get_pesan_pembuka(bahasa_mkd, gaya)
        jawaban_ai = cek_pakai_ai(kode_user, bahasa_program, bahasa_mkd, gaya)

        if jawaban_ai:
            hasil_mentah = f"{pembuka}\n\n{jawaban_ai}"
        else:
            try:
                compile(kode_user, "<string>", "exec")
                hasil_mentah = f"{pembuka}\n\nMantap, kodenya aman gak ada syntax error nih keren!"
            except SyntaxError as e:
                penjelasan = terjemahkan_error(e.msg)
                hasil_mentah = f"{pembuka}\n\nAda syntax error di baris {e.lineno}: {penjelasan}"

        hasil = markdown.markdown(hasil_mentah)
        
        return render_template(
            "cek_error.html",
            hasil=hasil,
            bahasa_program=bahasa_program,
            bahasa_mkd=bahasa_mkd,
            gaya=gaya
        )
    return render_template("cek_error.html", hasil=None)

@app.route("/kuis", methods=["GET", "POST"])
def kuis():
    if request.method == "POST":
        bahasa = request.form["bahasa"]
        level = request.form["level"]
        jumlah = int(request.form["jumlah"])

        semua_soal = read_questions(bahasa, level)
        semua_soal = list(semua_soal)
        random.shuffle(semua_soal)
        soal_terpilih = semua_soal[:jumlah]

        session["soal_ids"] = [s["id"] for s in soal_terpilih]
        session["index_sekarang"] = 0
        session["skor"] = 0

        return redirect("/kuis/main")
    return render_template("kuis_pilih.html")

@app.route("/kuis/main", methods=["GET", "POST"])
def kuis_main():
    soal_ids = session.get("soal_ids")
    index_sekarang = session.get("index_sekarang", 0)

    if not soal_ids or index_sekarang >= len(soal_ids):
        session.pop("soal_ids", None)
        session.pop("index_sekarang", None)
        session.pop("skor", None)
        return render_template("kuis_pilih.html")

    if request.method == "POST":
        jawaban = request.form["jawaban"].strip()
        qid = soal_ids[index_sekarang]
        soal = get_question_by_id(qid)

        jawaban_bersih = "".join(jawaban.split())
        kunci_bersih = "".join(soal["fixed_code"].split())

        if jawaban_bersih == kunci_bersih:
            session["skor"] = session["skor"] + 1

        session["index_sekarang"] = index_sekarang + 1

    index_sekarang = session.get("index_sekarang", 0)

    if index_sekarang >= len(soal_ids):
        skor_akhir = session.get("skor", 0)
        total_soal = len(soal_ids)

        session.pop("soal_ids", None)
        session.pop("index_sekarang", None)
        session.pop("skor", None)

        return render_template("kuis_selesai.html", skor=skor_akhir, total=total_soal)

    qid = soal_ids[index_sekarang]
    soal = get_question_by_id(qid)

    return render_template(
        "kuis_main.html",
        soal=soal,
        nomor=index_sekarang + 1,
        total=len(soal_ids),
        skor=session["skor"]
    )
    
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form["password"]
        if password == ADMIN_PASSWORD:
            session["is_admin"] = True
            return redirect("/admin/soal")
        else:
            return render_template("admin_login.html", error="Password salah, coba lagi!")
    return render_template("admin_login.html", error=None)

@app.route("/admin/soal")
def admin_soal():
    if not session.get("is_admin"):
        return redirect("/admin/login")

    filter_bahasa = request.args.get("bahasa", "python")

    if filter_bahasa:
        daftar_soal = read_questions(bahasa=filter_bahasa)
    else:
        daftar_soal = read_questions()

    urutan_level = {"pemula": 0, "medium": 1, "pro": 2}
    daftar_soal = sorted(daftar_soal, key=lambda s: urutan_level.get(s["level"], 99))

    return render_template("admin_soal.html", daftar_soal=daftar_soal, filter_bahasa=filter_bahasa)

@app.route("/admin/soal/tambah", methods=["GET", "POST"])
def admin_tambah():
    if not session.get("is_admin"):
        return redirect("/admin/login")

    if request.method == "POST":
        bahasa = request.form["bahasa"]
        level = request.form["level"]
        buggy_code = request.form["buggy_code"]
        fixed_code = request.form["fixed_code"]
        hint = request.form["hint"]

        create_question(bahasa, level, buggy_code, fixed_code, hint)
        return redirect("/admin/soal")

    return render_template("admin_tambah.html")

@app.route("/admin/soal/edit/<int:qid>", methods=["GET", "POST"])
def admin_edit(qid):
    if not session.get("is_admin"):
        return redirect("/admin/login")

    soal = get_question_by_id(qid)

    if request.method == "POST":
        bahasa = request.form["bahasa"]
        level = request.form["level"]
        buggy_code = request.form["buggy_code"]
        fixed_code = request.form["fixed_code"]
        hint = request.form["hint"]

        update_question(qid, bahasa, level, buggy_code, fixed_code, hint)
        return redirect("/admin/soal")

    return render_template("admin_edit.html", soal=soal)

@app.route("/admin/soal/hapus/<int:qid>")
def admin_hapus(qid):
    if not session.get("is_admin"):
        return redirect("/admin/login")

    delete_question(qid)
    return redirect("/admin/soal")

def buat_zip_source():
    nama_zip = "ngapak_code_source.zip"
    folder_dikecualikan = {".venv", ".venv-1", ".venv-2", "__pycache__"}
    file_dikecualikan = {"config.py", "ngapak_code.db", nama_zip}

    with zipfile.ZipFile(nama_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in folder_dikecualikan and not d.startswith(".")]

            for file in files:
                if file in file_dikecualikan:
                    continue
                path_lengkap = os.path.join(root, file)
                zipf.write(path_lengkap)

    return nama_zip

@app.route("/download-source")
def download_source():
    nama_zip = buat_zip_source()
    return send_file(nama_zip, as_attachment=True)

app = app

if __name__ == "__main__":
    app.run(debug=False)