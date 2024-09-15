import math

numeroEntero = int(input("Ingrese un número entero: "))

if numeroEntero < 2:
    print(f"{numeroEntero} no es primo.")
else:
    divisor = 2
    esPrimo = True # Asumo que es primo

    while divisor <= math.sqrt(numeroEntero) and esPrimo:
        if numeroEntero % divisor == 0: # Si encuentro divisor...
            esPrimo = False # ... no es primo
        divisor += 1

    if esPrimo:
        print(f"{numeroEntero} ¡¡Es primo!!")
    else:
        print(f"{numeroEntero} no es primo.")
