# Funciones del ejercicio 1
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

# Funciones del ejercicio 2
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

# Función del ejercicio 3
def buscar_subcadena(S, sub):
    return sub in S

# Función del ejercicio 4
def split(S, c):
    resultado = ['']
    for caracter in S:
        if caracter == c:
            resultado += ['']
        else:
            resultado[-1] += caracter
    return resultado

# Función del ejercicio 5
def strip(S):
    inicio = 0
    while inicio < len(S) and S[inicio] == ' ':
        inicio += 1
    
    fin = len(S) - 1
    while fin > inicio and S[fin] == ' ':
        fin -= 1
    
    return S[inicio:fin+1]

# Función del ejercicio 6
def camel_case(S):
    S = strip(S)
    palabras = split(S, ' ')
    
    resultado = minuscula(palabras[0])
    for palabra in palabras[1:]:
        palabra = minuscula(palabra)
        if len(palabra) > 0:
            primera_letra = palabra[0]
            if es_letra(primera_letra):
                palabra = chr(ord(primera_letra) - 32) + palabra[1:]
        resultado += palabra
    
    return resultado

# Funciones del ejercicio 7
def mayuscula_primera_letra(palabra):
    if len(palabra) == 0:
        return palabra
    return mayuscula(palabra[0]) + palabra[1:]

def title_case(S):
    palabras = split(S, ' ')
    resultado = ""
    for palabra in palabras:
        if resultado != "":
            resultado += ' '
        resultado += mayuscula_primera_letra(palabra)
    return resultado

# Función del ejercicio 8
def find(S, sub):
    n = len(S)
    m = len(sub)
    
    for i in range(n - m + 1):
        if S[i:i+m] == sub:
            return i
    
    return -1

# Funciones del ejercicio 9
def ident_izq(texto, n):
    """Indenta el texto a la izquierda en n espacios."""
    if len(texto) > n:
        return texto[:n]
    return texto + ' ' * (n - len(texto))

def ident_der(texto, n):
    """Indenta el texto a la derecha en n espacios."""
    if len(texto) > n:
        return texto[:n]
    return ' ' * (n - len(texto)) + texto

def ident_cen(texto, n):
    """Centra el texto en n espacios."""
    if len(texto) > n:
        inicio = (len(texto) - n) // 2
        return texto[inicio:inicio+n]
    espacios_izq = (n - len(texto)) // 2
    espacios_der = n - len(texto) - espacios_izq
    return ' ' * espacios_izq + texto + ' ' * espacios_der

# Bloque principal para pruebas
if __name__ == "__main__":
    # Pruebas para las funciones del ejercicio 1
    print("Pruebas de funciones del ejercicio 1:")
    print(f"es_letra('A'): {es_letra('A')}")
    print(f"es_numero('5'): {es_numero('5')}")
    print(f"es_mayuscula('Z'): {es_mayuscula('Z')}")
    print(f"es_minuscula('a'): {es_minuscula('a')}")
    print(f"es_espacio(' '): {es_espacio(' ')}")
    print(f"es_simbolo('!'): {es_simbolo('!')}")

    # Pruebas para las funciones del ejercicio 2
    print("\nPruebas de funciones del ejercicio 2:")
    print(f"mayuscula('Hola Mundo'): {mayuscula('Hola Mundo')}")
    print(f"minuscula('Hola Mundo'): {minuscula('Hola Mundo')}")

    # Prueba para la función del ejercicio 3
    print("\nPrueba de función del ejercicio 3:")
    print(f"buscar_subcadena('Hola Mundo', 'Mundo'): {buscar_subcadena('Hola Mundo', 'Mundo')}")

    # Prueba para la función del ejercicio 4
    print("\nPrueba de función del ejercicio 4:")
    print(f"split('Hola,Mundo,Python', ','): {split('Hola,Mundo,Python', ',')}")

    # Prueba para la función del ejercicio 5
    print("\nPrueba de función del ejercicio 5:")
    print(f"strip('  Hola Mundo  '): '{strip('  Hola Mundo  ')}'")

    # Prueba para la función del ejercicio 6
    print("\nPrueba de función del ejercicio 6:")
    print(f"camel_case('vamos al mar'): {camel_case('vamos al mar')}")
    print(f"camel_case('HELLO world'): {camel_case('HELLO world')}")

    # Pruebas para las funciones del ejercicio 7
    print("\nPruebas de funciones del ejercicio 7:")
    print(f"mayuscula_primera_letra('hola'): {mayuscula_primera_letra('hola')}")
    print(f"title_case('vamos al mar'): {title_case('vamos al mar')}")
    print(f"title_case('HELLO world'): {title_case('HELLO world')}")

    # Prueba para la función del ejercicio 8
    print("\nPrueba de función del ejercicio 8:")
    print(f"find('Hola, qué haces por acá', 'qué'): {find('Hola, qué haces por acá', 'qué')}")
    print(f"find('Hola, qué haces por acá', 'Hola'): {find('Hola, qué haces por acá', 'Hola')}")
    print(f"find('Hola, qué haces por acá', 'como'): {find('Hola, qué haces por acá', 'como')}")

    # Pruebas para las funciones del ejercicio 9
    print("\nPruebas de funciones del ejercicio 9:")
    print(f"ident_izq('12345', 10): '{ident_izq('12345', 10)}'")
    print(f"ident_der('12345', 10): '{ident_der('12345', 10)}'")
    print(f"ident_cen('12345', 10): '{ident_cen('12345', 10)}'")
    print(f"ident_izq('1234567891011', 10): '{ident_izq('1234567891011', 10)}'")
    print(f"ident_der('1234567891011', 10): '{ident_der('1234567891011', 10)}'")
    print(f"ident_cen('1234567891011', 10): '{ident_cen('1234567891011', 10)}'")
