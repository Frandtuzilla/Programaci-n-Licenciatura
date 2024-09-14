valores = int(input("¿Cuántos valores vas a introducir? "))

while valores <= 0:
    valores = int(input("¡Imposible! ¿Cuántos valores vas a introducir? "))

i = 0
menor = None
mayor = None
suma = 0

while i < valores:
    aux = int(input(f"Escribe el número {i+1}: "))

    if i == 0:
        menor = aux
        mayor = aux
    else:
        if aux < menor:
            menor = aux
        if aux > mayor:
            mayor = aux

    suma += aux
    i += 1

print(f"El mínimo de los valores introducidos es: {menor}")
print(f"El máximo de los valores introducidos es: {mayor}")
print(f"La media de los valores introducidos es: {suma/valores}")
