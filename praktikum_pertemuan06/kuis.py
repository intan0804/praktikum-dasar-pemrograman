# Struktur bank soal: [teks_soal, opsi_a, opsi_b, opsi_c, opsi_d, kunci]
bank_soal = [
    ["Apa ibu kota Indonesia?", "Jakarta", "Bandung", "Surabaya", "Medan", "A"],
    ["2 + 2 = ?", "3", "4", "5", "6", "B"],
    ["Tipe data yang digunakan untuk menyimpan teks adalah?", "Integer", "Float", "String", "Boolean", "C"],
]

skor = 0 
for nomor, soal in enumerate(bank_soal):
    teks, opsi_a, opsi_b, opsi_c, opsi_d, kunci = soal
    print(f"\nSoal {nomor + 1}: {teks}")
    print(f"A. {opsi_a} B. {opsi_b} C. {opsi_c} D. {opsi_d}")
    jawaban = input("Jawaban Anda: ").strip().upper()
    if jawaban == kunci:
        print("Benar!")
        skor += 1
    else:
        print(f"Salah. Jawaban yang benar: {kunci}")

print(f"Jumlah soal: {len(bank_soal)}")
print(f"Benar : {skor}")
print(f"Jumlah skor: {skor}/{len(bank_soal)}")