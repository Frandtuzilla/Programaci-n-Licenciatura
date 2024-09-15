import math

repetirProceso = True
cumpleCondiciones = True
nombre = ""
edad = 0
dni = ""
clave = ""

while repetirProceso:
    ingreso = input("Ingrese datos [nombre,edad,DNI]: ")

    contadorDeCampos = 1

    largoIngreso = len(ingreso)

    i = 0
    auxIndex = 0 

    while i < largoIngreso and contadorDeCampos <= 3:
        
        if ingreso[i] == ',':
            if contadorDeCampos == 1:
                nombre = ingreso[0:i]
                auxIndex = i
                contadorDeCampos += 1
            elif contadorDeCampos == 2:
                edad = int(ingreso[auxIndex + 1: i])
                auxIndex = i
                contadorDeCampos += 1

        i += 1

    if contadorDeCampos == 3:
        dni = ingreso[auxIndex + 1: largoIngreso]
        contadorDeCampos += 1
    
    if len(nombre) >= 3 and 10 <= edad <= 99 and 7 <= len(dni) <= 8:
        
        nombreAux = ""
        i = 0

        while i < 3:
            if 'a' <= nombre[i] <= 'z':
                nombreAux += chr(ord(nombre[i]) - ord('a') + ord('A'))
            else:
                nombreAux += nombre[i]

            i += 1

        clave = nombreAux + str(edad) + dni[:4]
        
        repetirProceso = False
    else:
        print("Datos no válidos. Intente de nuevo.")

print(f"Clave generada: {clave}")


if edad < 2:
    print(f"{edad} no es primo.")
else:
    divisor = 2
    esPrimo = True # Asumo que es primo

    while divisor <= math.sqrt(edad) and esPrimo:
        if edad % divisor == 0: # Si encuentro divisor, ...
            esPrimo = False  # ... no es primo 
        divisor += 1

    if esPrimo:
        print(f"{edad} es un número primo!")
    else:
        print(f"{edad} NO es un número primo!")

i = 0
contVocales = 0
vocales = "AEIOUaeiou"

while i < len(nombre):
    
    j = 0
    flag = True

    while flag and j < len(vocales):
        if nombre[i] == vocales[j]:
            contVocales += 1
            flag = False
        j += 1

    i += 1

print(f"{nombre} tiene {contVocales} vocales!")
