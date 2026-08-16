def get_pesan_pembuka(bahasa, gaya):
    pesan = {
        ("indonesia", "gaul"): "Waduh, ada yang eror ni bro di code lu:",
        ("indonesia", "galak"): "Woy, code lu aneh kali ayo brantakan bet, coba benerin:",
        ("ngapak", "gaul"): "Pripun niki mas, ana error ki nang kodingan e koe:",
        ("ngapak", "galak"): "Ngapa si koe kantem pikir po? kodingan ajur koyo iki",
    }
    return pesan.get((bahasa, gaya), "Ada error nih bos:")

def terjemahkan_error(pesan_asli):
    kamus = {
        "inalid syntax": "ada kesalahan penulisan struktur kode di baris ini, coba cek lagi tanda kurung, titik dua, atau tanda kutipnya",
        "unexpected EOF while parsing": "kodingan kamu keliatan belum selesai, ada kurung atau kutip yang belum di tutup",
        "expected ':'": "abis nulis if/for/def/while itu wajib di tutup make tanda titik dua (:) di ujung nya",
    }
    for key in kamus:
        if key in pesan_asli:
            return kamus[key]
        return pesan_asli