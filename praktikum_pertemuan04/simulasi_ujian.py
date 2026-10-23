soal = [
    "Ibu kota Indonesia adalah?",
    "2 + 2 * 3 hasilnya adalah?",
    "Tipe data untuk teks pada Python disebut?",
    "Fungsi untuk menampilkan teks di Python adalah?",
    "Perintah untuk menghentikan perulangan adalah?",
]
kunci = ["Jakarta", "8", "string", "print()", "break"]

skor = 0
for nomor in range(len(soal)):
    print(f"\nSoal {nomor + 1}: {soal[nomor]}")
    jawaban = input("Jawaban Anda: ")
    if jawaban.strip().lower() == kunci[nomor].lower():
        print("Benar!")
        skor += 1
    else:
        print(f"Salah. Jawaban benar: {kunci[nomor]}")

print(f"\nSkor akhir: {skor}/{len(soal)}")