def buat_biodata(nama, umur, jurusan):
    print(f"Nama:  {nama}")
    print(f"Umur:  {umur}")
    print(f"Jurusan: {jurusan}")

# Positional argument 
buat_biodata('Rani', 19, 'Sistem Informasi')

# Keyword argument 
buat_biodata(jurusan='Sistem Informasi', nama='Rani', umur=19)