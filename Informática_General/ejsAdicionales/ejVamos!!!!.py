cadena = input("Ingrese una cadena de 20 a 30 caracteres (deben ser solo dígitos, letras mayúsculas y letras minúsculas): ")

cadenaAux = ""

i = 0
suma = 0
primero = True  # Variable para controlar si es el primer número par

while i < len(cadena):
    if cadena[i] > '0' and cadena[i] < '9':
        if int(cadena[i]) % 2 == 0:
            suma += int(cadena[i])
            if not primero:
                cadenaAux += ' + '  # Solo se agrega el ' + ' después del primer número par
            cadenaAux += cadena[i]
            primero = False  # Después del primer número par, ya se pueden agregar los ' + '
    i += 1

print(f"La suma de los números pares es {suma}.")

print(f"La cuenta que hice fue: {cadenaAux} = {suma}.")
