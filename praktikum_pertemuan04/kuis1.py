n = int(input("Masukkan jumlah data nilai: "))
total = 0
tertinggi = 0
terendah = 100

for i in range(1, n + 1): 
 nilai = int(input(f"Masukkan nilai ke-{i}: "))
 total = total + nilai
 if nilai > tertinggi:
    tertinggi = nilai
 if nilai < terendah:
    terendah = nilai
rata_rata = total / n

print("Hasil perhitungan nilai:")
print(f"total nilai: {total}")
print(f"Rata-rata nilai: {rata_rata}")
print(f"Nilai tertinggi: {tertinggi}")
print(f"Nilai terendah: {terendah}")