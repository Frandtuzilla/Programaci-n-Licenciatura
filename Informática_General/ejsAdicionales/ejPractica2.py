import random

cantPalabras = random.randint(1, 10)
print(f"La cantidad de palabras en la frase tiene que ser de: {cantPalabras}")

repetirProceso = True

while repetirProceso:

    frase = input("Ingrese una frase: ")

    cumpleCondiciones = True

    if len(frase) > 20 + cantPalabras:
        cumpleCondiciones = False

    i = 0
    cantAsteriscos = 0
    inicioFrase = True  # Control para verificar la primera letra de cada palabra

    # Procesar la frase carácter por carácter
    while cumpleCondiciones and i < len(frase):

        caracter = frase[i]

        if inicioFrase:  # Si es el inicio de una palabra ...
            if not "A" <= caracter <= "Z":  # ... y no es mayúscula ...
                cumpleCondiciones = False  # ... no cumple las condiciones
            else:
                inicioFrase = False  # Si es mayúscula, ya no es el inicio de palabra
        elif not ("A" <= caracter <= "Z" or "a" <= caracter <= "z" or caracter == "*"):  # Verificar que solo haya letras o asteriscos
            cumpleCondiciones = False  # Si no cumple, es inválida

        # Si cumple condiciones y es un asterisco
        if cumpleCondiciones and caracter == "*":
            cantAsteriscos += 1  # Contar los asteriscos
            inicioFrase = True  # Lo que viene después es el inicio de una nueva palabra

        i += 1

    # Verificar que la cantidad de asteriscos sea correcta y la frase no termine en asterisco
    if cumpleCondiciones and cantAsteriscos == cantPalabras - 1 and frase[-1] != "*":
        repetirProceso = False  # Terminar el proceso si la frase es válida
        
        j = 0
        inicioPalabra = 0  # Nuevo índice para controlar el inicio de las palabras
        palabra = ""

        while j < len(frase):
            
            if frase[j] == "*":
                # Extraer palabra desde 'inicioPalabra' hasta el asterisco
                palabra = frase[inicioPalabra:j]
                print(f"{palabra}")
                inicioPalabra = j + 1  # Ajustar el índice para el inicio de la siguiente palabra

            elif j == len(frase) - 1:
                # Extraer la última palabra
                palabra = frase[inicioPalabra:j+1]
                print(f"{palabra}")

            j += 1

    else:
        print("Frase inválida. Inténtelo nuevamente\n")
