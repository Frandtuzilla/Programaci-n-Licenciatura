numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    maximo = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maximo = numero2
else:
    maximo = numero3

if numero1 <= numero2 and numero1 <= numero3:
    minimo = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    minimo = numero2
else:
    minimo = numero3

print(f"El máximo es: {maximo}")
print(f"El mínimo es: {minimo}")