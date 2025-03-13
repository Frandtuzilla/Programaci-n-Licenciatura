from ej1 import es_letra, es_mayuscula, es_minuscula

def mayuscula(S):
    resultado = ""
    for c in S:
        if es_letra(c):
            if es_minuscula(c):
                resultado += chr(ord(c) - 32)
            else:
                resultado += c
        else:
            resultado += c
    return resultado

def minuscula(S):
    resultado = ""
    for c in S:
        if es_letra(c):
            if es_mayuscula(c):
                resultado += chr(ord(c) + 32)
            else:
                resultado += c
        else:
            resultado += c
    return resultado

if __name__ == "__main__":
    # Ejemplos de uso
    texto = "Hola, Mundo! 123"
    print(mayuscula(texto))  # Salida: HOLA, MUNDO! 123
    print(minuscula(texto))  # Salida: hola, mundo! 123
