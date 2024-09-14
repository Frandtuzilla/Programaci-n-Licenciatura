numero = int(input("Escribe un número mayor que 1: "))

while numero <= 1:
    print(f"{numero} no es un número mayor que 1. Inténtalo de nuevo:")
    numero = int(input("Escribe un número mayor que 1: "))

divisor = 2
print("Descomposición en factores primos:", end=" ")
while numero > 1:
    while numero % divisor == 0:
        print(divisor, end=" ")
        numero //= divisor
    divisor += 1