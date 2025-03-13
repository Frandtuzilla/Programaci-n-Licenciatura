def es_letra(c):
    return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z'))

def es_numero(c):
    return ord('0') <= ord(c) <= ord('9')

def es_mayuscula(c):
    return ord('A') <= ord(c) <= ord('Z')

def es_minuscula(c):
    return ord('a') <= ord(c) <= ord('z')

def es_espacio(c):
    return c == ' ' or c == '\t' or c == '\n' or c == '\r'

def es_simbolo(c):
    return not (es_letra(c) or es_numero(c) or es_espacio(c))
