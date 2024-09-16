from math import sqrt

num = 23
divisor = 3
esPrimo = True

if num < 2 or num % 2 == 0:
    print("No es un número primo")
else:
    while divisor < sqrt(num) and esPrimo:
        if num % divisor == 0:
            esPrimo = False
        divisor += 2
    
    if esPrimo:
        print("El número es primo")
    else:
        print("No es un número primo")