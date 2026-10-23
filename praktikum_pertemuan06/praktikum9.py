nilai = [78, 90, 65, 88, 72]
print("Data:", nilai)
print("Jumlah:", len(nilai))
print("Total:", sum(nilai))
print("Rata-rata:", sum(nilai) / len(nilai))
print("Tertinggi:", max(nilai))
print("Terendah:", min(nilai))
print("Urutan menurun:", sorted(nilai, reverse=True))
lulus = [x for x in nilai if x >=75]
print("Nilai lulus:", lulus)