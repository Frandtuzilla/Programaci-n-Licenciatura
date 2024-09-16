vocales = "aeiouAEIOU"
cantidadPalabrasConVocal = 0

frase = input("Ingrese una frase: ")

i = 0
enPalabra = False  # Indica si estamos dentro de una palabra
palabraIniciaConVocal = False  # Indica si la palabra actual empieza con una vocal
longitudPalabra = 0  # Para contar cuántas letras tiene la palabra

while i < len(frase):
    if frase[i] != " ":  # Si no es un espacio, estamos dentro de una palabra
        if not enPalabra:  # Si es el comienzo de una palabra
            enPalabra = True
            longitudPalabra = 1  # Reseteamos la longitud de la palabra
            if frase[i] in vocales:  # Verificamos si empieza con una vocal
                palabraIniciaConVocal = True
            else:
                palabraIniciaConVocal = False
        else:
            longitudPalabra += 1  # Incrementamos la longitud si sigue la palabra
    else:
        if enPalabra:  # Si venimos de estar dentro de una palabra
            if palabraIniciaConVocal and longitudPalabra > 1:  # Contar si empieza con vocal y tiene más de 1 letra
                cantidadPalabrasConVocal += 1
            enPalabra = False  # Terminamos la palabra

    i += 1

# Verificar si la última palabra es válida
if enPalabra and palabraIniciaConVocal and longitudPalabra > 1:
    cantidadPalabrasConVocal += 1

print(f"Cantidad de palabras que comienzan con una vocal: {cantidadPalabrasConVocal}")
