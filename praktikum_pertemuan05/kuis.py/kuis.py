def tampilkan_soal(nomor, teks_soal):
    print(f"\nSoal {nomor}:")
    print(teks_soal)
    print("Pilih jawaban A, B, C, atau D")


def periksa_jawaban(jawaban_mahasiswa, kunci_jawaban):
    if jawaban_mahasiswa.upper() == kunci_jawaban:
        return True
    else:
        return False


def hitung_skor(jumlah_benar, jumlah_soal):
    skor = (jumlah_benar / jumlah_soal) * 100
    return skor


def main():
    nomor = 1
    jumlah_benar = 0

    tampilkan_soal(nomor, "Apa ibu kota Indonesia?")
    print("A. Bandung")
    print("B. Jakarta")
    print("C. Surabaya")
    print("D. Semarang")

    jawaban = input("Jawaban Anda: ").strip().upper()

    if jawaban not in ["A", "B", "C", "D"]:
        print("Jawaban tidak valid. Silakan pilih A, B, C, atau D.")
        return

    hasil = periksa_jawaban(jawaban, "B")

    if hasil:
        print("Benar! Jawaban Anda tepat.")
        jumlah_benar = 1
    else:
        print("Salah. Jawaban yang benar adalah B. Jakarta.")

    skor_akhir = hitung_skor(jumlah_benar, 1)
    print(f"Skor akhir: {skor_akhir:.0f}")


if __name__ == "__main__":
    main()