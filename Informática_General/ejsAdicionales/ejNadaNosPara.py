frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra para verificar si está dentro de la frase: ")

i = 0
existe = False
lenFrase = len(frase)
lenPalabra = len(palabra)

while i < lenFrase and not existe:
    j = 0
    if frase[i] == palabra[j]:
        while j < lenPalabra and frase[i+j] == palabra[j]:
            j += 1
    if j == lenPalabra:
        existe = True
    i += 1

if existe:
    print(f"La palabra: \"{palabra}\", está en la frase: {frase}")
else:
    print(f"La palabra: \"{palabra}\", NO está en la frase: {frase}")