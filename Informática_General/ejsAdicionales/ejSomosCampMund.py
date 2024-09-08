cantDigits = int(input("Ingrese la cantidad de dígitos que quieres que tenga el número (entre 10 y 20): "))

while cantDigits > 20 or cantDigits < 10:
    cantDigits = int(input("ERROR -> Ingrese la cantidad de dígitos que quieres que tenga el número (entre 10 y 20): "))

numero = int(input(f"Ingrese un número que tenga {cantDigits} cantidad de dígitos: "))

while len(str(numero)) != cantDigits:
    numero = int(input(f"ERROR -> Ingrese un número que tenga {cantDigits} cantidad de dígitos: "))

numero = str(numero)
suma= 0
i = 0
cadenaAux = ''
primero = True

while i < 4:
    suma += int(numero[i])
    if not primero:
        cadenaAux += ' + '
    cadenaAux += numero[i]        
    primero = False
    i += 1

print(f"La suma de los primeros 4 dígitos es: {cadenaAux} = {suma}")