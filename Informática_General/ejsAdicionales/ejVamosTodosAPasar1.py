cadena = input("Ingrese una cadena de palabras separadas por espacios: ")

repetirProceso = True
while repetirProceso:
    k = int(input("Ingrese un número mayor a 0 y menor a la longitud de la cadena: "))
    if 0 < k < len(cadena):
        repetirProceso = False
    else:
        print(f"El número debe ser mayor a 0 y menor a {len(cadena)}.")

palabrasInvertidas = ""
hayPalabrasLargas = False
palabraActual = ""
i = 0

while i < len(cadena):
    if cadena[i] == " ":
        j = len(palabraActual) - 1
        while j >= 0:
            palabrasInvertidas += palabraActual[j]
            j -= 1
        palabrasInvertidas += " "

        if len(palabraActual) > k:
            hayPalabrasLargas = True

        palabraActual = ""
    else:
        palabraActual += cadena[i]

    i += 1

j = len(palabraActual) - 1
while j >= 0:
    palabrasInvertidas += palabraActual[j]
    j -= 1

if len(palabraActual) > k:
    hayPalabrasLargas = True

print("Frase con palabras invertidas:", palabrasInvertidas)

if hayPalabrasLargas:
    print("Hay palabras largas")
else:
    print("No hay palabras largas")
