from strings import split, mayuscula

# Esta función convierte la primera letra de una palabra a mayúscula
def mayuscula_primera_letra(palabra):
    # Si la palabra está vacía, la devolvemos sin cambios
    if len(palabra) == 0:
        return palabra
    # Convertimos la primera letra a mayúscula y la concatenamos con el resto de la palabra
    return mayuscula(palabra[0]) + palabra[1:]

# Esta función convierte la primera letra de cada palabra en una cadena a mayúscula
def title_case(S):
    # Dividimos la cadena en palabras
    palabras = split(S, ' ')
    resultado = ""
    for palabra in palabras:
        # Agregamos un espacio entre palabras, excepto para la primera
        if resultado != "":
            resultado += ' '
        # Convertimos la primera letra de cada palabra a mayúscula y la agregamos al resultado
        resultado += mayuscula_primera_letra(palabra)
    return resultado

if __name__ == "__main__":
    # Ejemplos de uso
    texto = 'vamos al mar'
    print(texto)
    print(title_case(texto))  # Imprimirá: 'Vamos Al Mar'
