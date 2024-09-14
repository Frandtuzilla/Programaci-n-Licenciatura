import math

numero = 2

while numero <= 1000:
    divisor = 2
    esPrimo = True

    while divisor <= math.sqrt(numero) and esPrimo:
        if numero % divisor == 0:
            esPrimo = False
        divisor += 1

    if esPrimo:
        print(f"{numero} es primo.")
    
    numero += 1
