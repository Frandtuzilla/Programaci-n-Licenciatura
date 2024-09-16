import math

valor = 0
repetirProceso = True

while repetirProceso:
    valor = int(input("Ingrese un número de 3 cifras: "))

    if valor >= 1000 or valor <= 99:
        print("Ingreso inválido.")
    else:
        repetirProceso = False

contadorProceso = 0
cumpleCondicion = False
valorAnterior = valor

while not cumpleCondicion:
    
    cuadrado = valor ** 2
    cuadradoStr = str(cuadrado)
    sumaDigitos = 0
    
    i = 0
    while i < len(cuadradoStr):
        sumaDigitos += int(cuadradoStr[i])
        i += 1
    
    print(f"Suma dígitos = {sumaDigitos}")
    print(f"Número = {sumaDigitos}")
    
    contadorProceso += 1
    
    if sumaDigitos == valor:
        cumpleCondicion = True
    else:
        valor = sumaDigitos

print(f"El proceso se repitió: {contadorProceso} veces")

if sumaDigitos < 2:
    print(f"{sumaDigitos} no es primo.")
else:
    divisor = 2
    esPrimo = True

    while divisor <= math.sqrt(sumaDigitos) and esPrimo:
        if sumaDigitos % divisor == 0:
            esPrimo = False
        divisor += 1

    if esPrimo:
        print(f"{sumaDigitos} es un número primo!")
    else:
        print(f"{sumaDigitos} NO es un número primo!")
