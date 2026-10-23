# Bagian 1: menelusuri huruf
kata = "Python"
for huruf in kata:
    print(huruf)

# Bagian 2: penghitung vokal
kalimat = input("Masukkan sebuah kalimat: ")
hitung_vokal = 0 
for huruf in kalimat.lower():
    if huruf in "aiueo":
        hitung_vokal += 1
print("Jumlah huruf vokal:", hitung_vokal)