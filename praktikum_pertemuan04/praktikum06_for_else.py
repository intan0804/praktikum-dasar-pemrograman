bilangan = 18
for i in range(2, bilangan):
    if bilangan % i == 0:
        print(f"{bilangan} bukan bilangan prima")
        break
else:
    print(f"{bilangan} adalah bilangan prima")

# Tugas Pengembangan
bilangan = int(input("Masukkan sebuah bilangan: "))

if bilangan < 2:
    print(f"{bilangan} bukan bilangan prima")
else:
    for i in range(2, bilangan):
        if bilangan % i == 0:
            print(f"{bilangan} bukan bilangan prima")
            break
    else:
        print(f"{bilangan} adalah bilangan prima")

bilangan = int(input("Masukkan sebuah bilangan: "))

if bilangan < 2:
    print(f"{bilangan} bukan bilangan prima")
else:
    for i in range(2, bilangan):
        if bilangan % i == 0:
            print(f"{bilangan} bukan bilangan prima")
            break
    else:
        print(f"{bilangan} adalah bilangan prima")