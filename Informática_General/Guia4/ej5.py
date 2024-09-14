import math

numeroEntero = int(input("Ingrese un número entero: "))

if numeroEntero < 2:
    print(f"{numeroEntero} No es primo.")
else:
    divisor = 2
    esPrimo = True

    while divisor <= math.sqrt(numeroEntero):
        if numeroEntero % divisor == 0:
            esPrimo = False
            break
        divisor += 1

    if esPrimo:
        print(f"{numeroEntero} ¡¡Es primo!!")
    else:
        print(f"{numeroEntero} No es primo.")