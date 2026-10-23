def sapa_mahasiswa(nama, sapaan='Selamat Belajar'):
    print(f"{sapaan}, {nama}!")

# Cara 1: Kedua argumen diberikan 
sapa_mahasiswa('Rina', 'Selamat Pagi')

# Cara 2: Hanya nama, sapaan memiliki nilai default
sapa_mahasiswa('Rina')