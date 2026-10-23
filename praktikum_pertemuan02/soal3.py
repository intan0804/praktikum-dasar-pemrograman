Harga_satuan = int(input("Masukkan harga satuan: "))
jumlah = int(input("Masukkan jumlah: "))
persen_diskon = int(input("Masukkan persen diskon: "))

subtotal = Harga_satuan * jumlah
nominal_diskon = subtotal * persen_diskon / 100
total_bayar = subtotal - nominal_diskon

print("subtotal: Rp", subtotal)
print("nominal_diskon: Rp", nominal_diskon)
print("total_bayar: Rp", total_bayar)