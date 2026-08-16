from database import create_question

soal_list = [
    # ==== PYTHON - PEMULA ====
    ("python", "pemula", """print("Halo dunia\"""", """print("Halo dunia")""", "Kurang tutup kurung di akhir print"),
    ("python", "pemula", """if x > 5\n    print("gede")""", """if x > 5:\n    print("gede")""", "Kurang titik dua setelah if"),
    ("python", "pemula", """nama = "Budi""", """nama = "Budi\"""", "Kurang tanda kutip penutup"),
    ("python", "pemula", """for i in range(5)\n    print(i)""", """for i in range(5):\n    print(i)""", "Kurang titik dua setelah for"),
    ("python", "pemula", """x = 5\nif x = 5:\n    print("sama")""", """x = 5\nif x == 5:\n    print("sama")""", "Pakai == bukan = buat membandingkan nilai"),

    # ==== PYTHON - MEDIUM ====
    ("python", "medium", """def tambah(a, b)\n    return a + b""", """def tambah(a, b):\n    return a + b""", "Kurang titik dua setelah def"),
    ("python", "medium", """angka = [1, 2, 3\nprint(angka)""", """angka = [1, 2, 3]\nprint(angka)""", "Kurang tutup kurung siku"),
    ("python", "medium", """while True\n    break""", """while True:\n    break""", "Kurang titik dua setelah while"),
    ("python", "medium", """data = {"nama": "Budi", "umur": 20\nprint(data)""", """data = {"nama": "Budi", "umur": 20}\nprint(data)""", "Kurang tutup kurung kurawal"),
    ("python", "medium", """try:\n    x = 1/0\nexcept ZeroDivisionError\n    print("error")""", """try:\n    x = 1/0\nexcept ZeroDivisionError:\n    print("error")""", "Kurang titik dua setelah except"),

    # ==== PYTHON - PRO ====
    ("python", "pro", """class Mobil:\n    def __init__(self, warna)\n        self.warna = warna""", """class Mobil:\n    def __init__(self, warna):\n        self.warna = warna""", "Kurang titik dua setelah def __init__"),
    ("python", "pro", """def faktorial(n):\nif n == 0:\nreturn 1\nreturn n * faktorial(n-1)""", """def faktorial(n):\n    if n == 0:\n        return 1\n    return n * faktorial(n-1)""", "Indentasi salah, body function harus masuk ke dalam blok"),
    ("python", "pro", """kali = lambda x, y x * y""", """kali = lambda x, y: x * y""", "Kurang titik dua di ekspresi lambda"),
    ("python", "pro", """with open("file.txt") as f\n    data = f.read()""", """with open("file.txt") as f:\n    data = f.read()""", "Kurang titik dua setelah with"),
    ("python", "pro", """class Kucing:\n    @property\n    def nama(self)\n        return self._nama""", """class Kucing:\n    @property\n    def nama(self):\n        return self._nama""", "Kurang titik dua setelah def nama"),

    # ==== HTML - PEMULA ====
    ("html", "pemula", """<h1>Judul</h2>""", """<h1>Judul</h1>""", "Tag pembuka dan penutup gak sama, h1 ditutup pake h2"),
    ("html", "pemula", """<p>Halo dunia<p>""", """<p>Halo dunia</p>""", "Kurang tanda slash buat nutup tag p"),
    ("html", "pemula", """<img src="gambar.jpg" alt="foto">>""", """<img src="gambar.jpg" alt="foto">""", "Ada tanda > kelebihan di akhir"),
    ("html", "pemula", """<a href="index.html>Home</a>""", """<a href="index.html">Home</a>""", "Kurang tanda kutip penutup di atribut href"),
    ("html", "pemula", """<div><p>Teks</div></p>""", """<div><p>Teks</p></div>""", "Urutan tag penutup kebalik, p harus ditutup sebelum div"),

    # ==== HTML - MEDIUM ====
    ("html", "medium", """<ul>\n<li>Item 1\n<li>Item 2\n</ul>""", """<ul>\n<li>Item 1</li>\n<li>Item 2</li>\n</ul>""", "Tiap <li> harus ditutup sendiri"),
    ("html", "medium", """<table>\n<tr><td>Data1<td>Data2</tr>\n</table>""", """<table>\n<tr><td>Data1</td><td>Data2</td></tr>\n</table>""", "Tiap <td> harus ditutup sebelum td berikutnya"),
    ("html", "medium", """<form>\n<input type="text" name="nama">\n<button>Submit</button>""", """<form>\n<input type="text" name="nama">\n<button>Submit</button>\n</form>""", "Tag form belum ditutup"),
    ("html", "medium", """<select>\n<option value="1">Satu\n<option value="2">Dua\n</select>""", """<select>\n<option value="1">Satu</option>\n<option value="2">Dua</option>\n</select>""", "Tiap option harus ditutup"),
    ("html", "medium", """<div class=box>Konten</div>""", """<div class="box">Konten</div>""", "Nilai atribut class harus pakai tanda kutip"),

    # ==== HTML - PRO ====
    ("html", "pro", """<script>\nfunction halo() {\n console.log("hi")\n</script>""", """<script>\nfunction halo() {\n console.log("hi")\n}\n</script>""", "Kurang tutup kurung kurawal buat function di dalam script"),
    ("html", "pro", """<label for=nama>Nama</label>\n<input id="nama">""", """<label for="nama">Nama</label>\n<input id="nama">""", "Nilai atribut for harus pakai tanda kutip"),
    ("html", "pro", """<video controls>\n<source src="video.mp4" type="video/mp4">\n<video>""", """<video controls>\n<source src="video.mp4" type="video/mp4">\n</video>""", "Tag penutup salah, harus </video> bukan <video>"),
    ("html", "pro", """<meta charset=UTF-8">""", """<meta charset="UTF-8">""", "Kurang tanda kutip pembuka di value charset"),
    ("html", "pro", """<nav>\n<ul>\n<li><a href="#">Home</li></a>\n</ul>\n</nav>""", """<nav>\n<ul>\n<li><a href="#">Home</a></li>\n</ul>\n</nav>""", "Urutan tag penutup a dan li kebalik"),

    # ==== CSS - PEMULA ====
    ("css", "pemula", """body {\n  color: red\n}""", """body {\n  color: red;\n}""", "Kurang titik koma setelah value"),
    ("css", "pemula", """.judul {\n  font-size: 20px;\n""", """.judul {\n  font-size: 20px;\n}""", "Kurang tutup kurung kurawal"),
    ("css", "pemula", """p {\n  color: blue;\n}\nh1 {\n  color red;\n}""", """p {\n  color: blue;\n}\nh1 {\n  color: red;\n}""", "Kurang titik dua antara property dan value"),
    ("css", "pemula", """.box {\n  width 100px;\n}""", """.box {\n  width: 100px;\n}""", "Kurang titik dua setelah width"),
    ("css", "pemula", """#header {\n  background-color: yellow;\n}\nfooter\n  color: black;\n}""", """#header {\n  background-color: yellow;\n}\nfooter {\n  color: black;\n}""", "Kurang kurung kurawal pembuka setelah selector footer"),

    # ==== CSS - MEDIUM ====
    ("css", "medium", """.btn {\n  padding: 10px;\n  /* border radius\n  border-radius: 5px;\n}""", """.btn {\n  padding: 10px;\n  /* border radius */\n  border-radius: 5px;\n}""", "Komentar belum ditutup pakai */"),
    ("css", "medium", """.container {\n  display: flex\n  justify-content: center;\n}""", """.container {\n  display: flex;\n  justify-content: center;\n}""", "Kurang titik koma setelah display: flex"),
    ("css", "medium", """.card {\n  margin: 10px 20px 5px 15px\n}""", """.card {\n  margin: 10px 20px 5px 15px;\n}""", "Kurang titik koma di akhir value margin"),
    ("css", "medium", """a:hover {\n  color green;\n}""", """a:hover {\n  color: green;\n}""", "Kurang titik dua setelah property color"),
    ("css", "medium", """.grid {\n  grid-template-columns: 1fr 1fr;\n  gap: 10px\n""", """.grid {\n  grid-template-columns: 1fr 1fr;\n  gap: 10px;\n}""", "Kurang titik koma dan tutup kurung kurawal"),

    # ==== CSS - PRO ====
    ("css", "pro", """@media (max-width: 768px {\n  body { font-size: 14px; }\n}""", """@media (max-width: 768px) {\n  body { font-size: 14px; }\n}""", "Kurang tutup kurung di kondisi media query"),
    ("css", "pro", """.box {\n  width: calc(100% - 20px;\n}""", """.box {\n  width: calc(100% - 20px);\n}""", "Kurang tutup kurung di fungsi calc"),
    ("css", "pro", """:root {\n  --main-color red;\n}""", """:root {\n  --main-color: red;\n}""", "Kurang titik dua setelah nama variabel CSS"),
    ("css", "pro", """.flex-item {\n  flex: 1 1 auto\n  align-self: center;\n}""", """.flex-item {\n  flex: 1 1 auto;\n  align-self: center;\n}""", "Kurang titik koma setelah value flex"),
    ("css", "pro", """.text {\n  color: var(--main-color;\n}""", """.text {\n  color: var(--main-color);\n}""", "Kurang tutup kurung di fungsi var"),

    # ==== JAVASCRIPT - PEMULA ====
    ("javascript", "pemula", """console.log("Halo dunia\"""", """console.log("Halo dunia")""", "Kurang tutup kurung di akhir console.log"),
    ("javascript", "pemula", """let nama = "Budi;""", """let nama = "Budi";""", "Kurang tanda kutip penutup"),
    ("javascript", "pemula", """function halo() {\n  console.log("hi")""", """function halo() {\n  console.log("hi")\n}""", "Kurang tutup kurung kurawal function"),
    ("javascript", "pemula", """if (x > 5 {\n  console.log("gede");\n}""", """if (x > 5) {\n  console.log("gede");\n}""", "Kurang tutup kurung di kondisi if"),
    ("javascript", "pemula", """let angka = [1, 2, 3;""", """let angka = [1, 2, 3];""", "Kurang tutup kurung siku array"),

    # ==== JAVASCRIPT - MEDIUM ====
    ("javascript", "medium", """for (let i = 0; i < 5; i++ {\n  console.log(i);\n}""", """for (let i = 0; i < 5; i++) {\n  console.log(i);\n}""", "Kurang tutup kurung di kondisi for"),
    ("javascript", "medium", """const kali = (x, y) => {\n  return x * y;""", """const kali = (x, y) => {\n  return x * y;\n}""", "Kurang tutup kurung kurawal arrow function"),
    ("javascript", "medium", """let obj = { nama: "Budi", umur: 20;""", """let obj = { nama: "Budi", umur: 20 };""", "Kurang tutup kurung kurawal object"),
    ("javascript", "medium", """switch(hari) {\n  case "senin":\n    console.log("awal minggu")\n}""", """switch(hari) {\n  case "senin":\n    console.log("awal minggu");\n    break;\n}""", "Kurang titik koma dan break di dalam case"),
    ("javascript", "medium", """function cekUmur(umur) {\n  if (umur >= 18\n    return "dewasa";\n}""", """function cekUmur(umur) {\n  if (umur >= 18)\n    return "dewasa";\n}""", "Kurang tutup kurung di kondisi if"),

    # ==== JAVASCRIPT - PRO ====
    ("javascript", "pro", """async function ambilData() {\n  const res = await fetch(url)\n  return res.json()""", """async function ambilData() {\n  const res = await fetch(url)\n  return res.json()\n}""", "Kurang tutup kurung kurawal function"),
    ("javascript", "pro", """const { nama umur } = orang;""", """const { nama, umur } = orang;""", "Kurang koma di antara nama variabel destructuring"),
    ("javascript", "pro", """const pesan = `Halo, ${nama}!;""", """const pesan = `Halo, ${nama}!`;""", "Kurang backtick penutup di template literal"),
    ("javascript", "pro", """class Hewan {\n  constructor(nama) {\n    this.nama = nama;\n  }\n  suara() {\n    console.log("...")\n}""", """class Hewan {\n  constructor(nama) {\n    this.nama = nama;\n  }\n  suara() {\n    console.log("...")\n  }\n}""", "Kurang tutup kurung kurawal method suara"),
    ("javascript", "pro", """fetch(url)\n  .then(res => res.json()\n  .then(data => console.log(data));""", """fetch(url)\n  .then(res => res.json())\n  .then(data => console.log(data));""", "Kurang tutup kurung di res.json()"),

    # ==== C# - PEMULA ====
    ("csharp", "pemula", """Console.WriteLine("Halo dunia")""", """Console.WriteLine("Halo dunia");""", "Kurang titik koma di akhir statement"),
    ("csharp", "pemula", """string nama = "Budi""", """string nama = "Budi";""", "Kurang tanda kutip dan titik koma penutup"),
    ("csharp", "pemula", """int x = 5\nConsole.WriteLine(x);""", """int x = 5;\nConsole.WriteLine(x);""", "Kurang titik koma setelah deklarasi variabel"),
    ("csharp", "pemula", """if (x > 5)\n{\n  Console.WriteLine("gede")\n}""", """if (x > 5)\n{\n  Console.WriteLine("gede");\n}""", "Kurang titik koma di dalam blok if"),
    ("csharp", "pemula", """class Program\n{\n  static void Main()\n  {\n    Console.WriteLine("Hi");\n  }""", """class Program\n{\n  static void Main()\n  {\n    Console.WriteLine("Hi");\n  }\n}""", "Kurang tutup kurung kurawal class"),

    # ==== C# - MEDIUM ====
    ("csharp", "medium", """void Tambah(int a, int b)\n{\n  return a + b;\n}""", """int Tambah(int a, int b)\n{\n  return a + b;\n}""", "Return type harus int, bukan void, karena mengembalikan nilai"),
    ("csharp", "medium", """foreach (int angka in daftar)\n{\n  Console.WriteLine(angka)\n}""", """foreach (int angka in daftar)\n{\n  Console.WriteLine(angka);\n}""", "Kurang titik koma di dalam foreach"),
    ("csharp", "medium", """switch (hari)\n{\n  case "senin":\n    Console.WriteLine("awal minggu");\n}""", """switch (hari)\n{\n  case "senin":\n    Console.WriteLine("awal minggu");\n    break;\n}""", "Kurang break di dalam case"),
    ("csharp", "medium", """string pesan = $"Halo, {nama}!""", """string pesan = $"Halo, {nama}!";""", "Kurang tanda kutip dan titik koma penutup string interpolation"),
    ("csharp", "medium", """public class Mobil\n{\n  public string Warna { get; set; }\n""", """public class Mobil\n{\n  public string Warna { get; set; }\n}""", "Kurang tutup kurung kurawal class"),

    # ==== C# - PRO ====
    ("csharp", "pro", """var hasil = daftar.Where(x => x > 5).ToList()""", """var hasil = daftar.Where(x => x > 5).ToList();""", "Kurang titik koma di akhir statement LINQ"),
    ("csharp", "pro", """public List<int> GetAngka(\n{\n  return new List<int>();\n}""", """public List<int> GetAngka()\n{\n  return new List<int>();\n}""", "Kurang tutup kurung di parameter method"),
    ("csharp", "pro", """Func<int, int, int> tambah = (a, b) => a + b""", """Func<int, int, int> tambah = (a, b) => a + b;""", "Kurang titik koma di akhir statement"),
    ("csharp", "pro", """public async Task AmbilData()\n{\n  var data = await client.GetAsync(url)\n}""", """public async Task AmbilData()\n{\n  var data = await client.GetAsync(url);\n}""", "Kurang titik koma setelah await"),
    ("csharp", "pro", """public string Nama { get; set; }\npublic int Umur { get set; }""", """public string Nama { get; set; }\npublic int Umur { get; set; }""", "Kurang titik koma antara get dan set"),
]

for bahasa, level, buggy, fixed, hint in soal_list:
    create_question(bahasa, level, buggy, fixed, hint)

print(f"Selesai! {len(soal_list)} soal berhasil dimasukkan ke database.")