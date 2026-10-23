def faktorial(n):
    if n < 0:
        raise ValueError("Faktorial tidak terdefinisi untuk bilangan negatif")
    if n <= 1:          # Kondisi dasar
        return 1
    return n * faktorial(n - 1) # Kasus rekursif

print(faktorial(5))