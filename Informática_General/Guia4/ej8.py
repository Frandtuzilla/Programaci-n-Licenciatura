valor = input("Ingrese un número: ")

i = 0
suma = 0

while i<len(valor):
    suma += int(valor[i])
    i += 1

print(f"La suma de los dígitos es: {suma}")