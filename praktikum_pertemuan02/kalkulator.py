print("=== Kalkulator Sederhana ===")
angka1 = int(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = int(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
    print (int(hasil))
elif operator == "-":
    hasil = angka1 - angka2
    print (int(hasil))
elif operator == "*":
    hasil = angka1 * angka2
    print (int(hasil))
elif operator == "/":
    hasil = angka1 / angka2
    print (int(hasil))
else:
    hasil = "Operator tidak dikenali"
    print(int(hasil))

