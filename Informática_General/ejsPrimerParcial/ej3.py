# Escribe un programa  que solicite al usuario ingresar una frase.
# La frase puede contener palabras separadas por uno o varios espacios
# y puede incluir caracteres numéricos, letras mayúsculas, letras minúsculas y espacios.

cantidadVocales = 0
cantidadPalabras = 0
 
frase = input("Ingrese una frase: ")

vocales = "aeiouAEIOU"
i = 0

enPalabra = False  # Esto nos ayuda a verificar si estamos dentro de una palabra

while i < len(frase):
    
    j = 0
    while j < len(vocales):
        if frase[i] == vocales[j]:
            cantidadVocales += 1
        j += 1

    if frase[i] != " " and not enPalabra:
        cantidadPalabras += 1
        enPalabra = True
    elif frase[i] == " ":
        enPalabra = False

    i += 1

print(f"Cantidad de palabras: {cantidadPalabras}")
print(f"Cantidad de vocales: {cantidadVocales}")
