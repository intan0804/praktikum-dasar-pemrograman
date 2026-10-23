def hitung_subtotal(harga, jumlah):
    return harga * jumlah

def hitung_diskon(subtotal):
    if subtotal >= 100000:
        return subtotal * 0.1
    else:
        return 0

def tampilkan_struk(nama_barang, subtotal, diskon):
    total_akhir = subtotal - diskon
    print("==== STRUK ====")
    print(f"Barang  : {nama_barang}")
    print(f"Subtotal: {subtotal}")
    print(f"Diskon  : {diskon}")
    print(f"Total   : {total_akhir}")

# Pemanggilan berurutan
subtotal =  hitung_subtotal(25000, 5)
diskon = hitung_diskon(subtotal)
tampilkan_struk('Buku Tulis', subtotal, diskon)