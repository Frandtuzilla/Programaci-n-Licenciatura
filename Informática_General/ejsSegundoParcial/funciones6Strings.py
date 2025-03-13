# Funciones para verificar caracteres (Ejercicio 1)
def es_letra(c):
    """Determina si un carácter es una letra."""
    # Verifica si el carácter está entre 'A' y 'Z' (mayúsculas) o entre 'a' y 'z' (minúsculas).
    return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z'))

def es_numero(c):
    """Determina si un carácter es un número."""
    # Verifica si el carácter está entre '0' y '9'.
    return ord('0') <= ord(c) <= ord('9')

def es_mayuscula(c):
    """Determina si un carácter es una letra mayúscula."""
    # Verifica si el carácter está entre 'A' y 'Z'.
    return ord('A') <= ord(c) <= ord('Z')

def es_minuscula(c):
    """Determina si un carácter es una letra minúscula."""
    # Verifica si el carácter está entre 'a' y 'z'.
    return ord('a') <= ord(c) <= ord('z')

def es_espacio(c):
    """Determina si un carácter es un espacio o un carácter de espacio."""
    # Verifica si el carácter es un espacio, tabulación, salto de línea o retorno de carro.
    return c in ' \t\n\r'

def es_simbolo(c):
    """Determina si un carácter es un símbolo no alfanumérico."""
    # Es un símbolo si no es letra, número ni espacio.
    return not (es_letra(c) or es_numero(c) or es_espacio(c))


# Funciones para manipulación de texto (Ejercicio 2)
def mayuscula(S):
    """Convierte todas las letras de una cadena a mayúsculas."""
    resultado = ""
    for c in S:
        if es_letra(c):
            # Si es minúscula, convierte a mayúscula restando 32 al valor ASCII.
            if es_minuscula(c):
                resultado += chr(ord(c) - (ord("a") - ord("A")))
            else:
                resultado += c  # Si ya es mayúscula, la deja igual.
        else:
            resultado += c  # No modifica caracteres que no son letras.
    return resultado

def minuscula(S):
    """Convierte todas las letras de una cadena a minúsculas."""
    resultado = ""
    for c in S:
        if es_letra(c):
            # Si es mayúscula, convierte a minúscula sumando 32 al valor ASCII.
            if es_mayuscula(c):
                resultado += chr(ord(c) + (ord("a") - ord("A")))
            else:
                resultado += c  # Si ya es minúscula, la deja igual.
        else:
            resultado += c  # No modifica caracteres que no son letras.
    return resultado


# Función para buscar subcadenas (Ejercicio 3)
def buscar_subcadena(S, sub):
    """Busca si una subcadena está dentro de otra cadena."""
    # Utiliza la operación 'in' para verificar si la subcadena está en la cadena principal.
    return sub in S


# Función para dividir cadenas (Ejercicio 4)
def split(S, c):
    """Divide una cadena en una lista de palabras usando un delimitador."""
    resultado = ['']  # Comienza con una lista vacía para construir palabras.
    for caracter in S:
        if caracter == c:
            # Si el carácter es el delimitador, agrega una nueva palabra vacía.
            resultado += ['']
        else:
            # Si no, añade el carácter a la última palabra en la lista.
            resultado[-1] += caracter
    return resultado


# Función para eliminar espacios en los extremos de una cadena (Ejercicio 5)
def strip(S):
    """Elimina los espacios en blanco al inicio y al final de una cadena."""
    # Determina el inicio de la cadena sin espacios.
    inicio = 0
    while inicio < len(S) and S[inicio] == ' ':
        inicio += 1
    # Determina el final de la cadena sin espacios.
    fin = len(S) - 1
    while fin > inicio and S[fin] == ' ':
        fin -= 1
    # Devuelve la subcadena desde el inicio hasta el final.
    return S[inicio:fin+1]


# Función para convertir a camelCase (Ejercicio 6)
def camel_case(S):
    """Convierte una cadena a formato camelCase."""
    S = strip(S)  # Elimina los espacios al inicio y al final.
    palabras = split(S, ' ')  # Divide la cadena en palabras.
    resultado = minuscula(palabras[0])  # Convierte la primera palabra a minúsculas.
    for palabra in palabras[1:]:
        if len(palabra) > 0:
            # Convierte la primera letra de las palabras siguientes a mayúsculas.
            resultado += chr(ord(palabra[0]) - (ord("a") - ord("A"))) + palabra[1:]
    return resultado


# Función para convertir a Title Case (Ejercicio 7)
def title_case(S):
    """Convierte la primera letra de cada palabra en una cadena a mayúscula."""
    palabras = split(S, ' ')  # Divide la cadena en palabras.
    resultado = ""
    for palabra in palabras:
        if resultado != "":
            resultado += ' '  # Añade un espacio entre palabras.
        # Convierte la primera letra de cada palabra a mayúscula.
        resultado += mayuscula(palabra[0]) + palabra[1:]
    return resultado


# Función para encontrar subcadenas (Ejercicio 8)
def find(S, sub):
    """Encuentra la posición de una subcadena dentro de una cadena."""
    n, m = len(S), len(sub)  # Calcula las longitudes de la cadena y la subcadena.
    for i in range(n - m + 1):
        # Compara un segmento de la cadena principal con la subcadena.
        if S[i:i + m] == sub:
            return i  # Devuelve la posición inicial si hay coincidencia.
    return -1  # Devuelve -1 si no encuentra la subcadena.


# Funciones para indentación (Ejercicio 9)
def ident_izq(texto, n):
    """Indenta el texto a la izquierda en n espacios."""
    if len(texto) > n:
        return texto[:n]  # Recorta el texto si excede el tamaño.
    return texto + ' ' * (n - len(texto))  # Rellena con espacios a la derecha.

def ident_der(texto, n):
    """Indenta el texto a la derecha en n espacios."""
    if len(texto) > n:
        return texto[:n]  # Recorta el texto si excede el tamaño.
    return ' ' * (n - len(texto)) + texto  # Rellena con espacios a la izquierda.

def ident_cen(texto, n):
    """Centra el texto en n espacios."""
    if len(texto) > n:
        inicio = (len(texto) - n) // 2  # Calcula el recorte centrado.
        return texto[inicio:inicio+n]
    espacios_izq = (n - len(texto)) // 2
    espacios_der = n - len(texto) - espacios_izq
    return ' ' * espacios_izq + texto + ' ' * espacios_der  # Rellena con espacios a ambos lados.

# Ejemplo de uso:
if __name__ == "__main__":
    texto = "Hola, Mundo"
    print("Mayúsculas:", mayuscula(texto))  # Ejercicio 2
    print("Minúsculas:", minuscula(texto))  # Ejercicio 2
    print("Buscar subcadena 'Mundo':", buscar_subcadena(texto, "Mundo"))  # Ejercicio 3
    print("Split por ',':", split(texto, ','))  # Ejercicio 4
    print("Strip:", strip("   Hola   "))  # Ejercicio 5
    print("Camel Case:", camel_case("vamos al mar"))  # Ejercicio 6
    print("Title Case:", title_case("vamos al mar"))  # Ejercicio 7
    print("Find 'Mundo':", find(texto, "Mundo"))  # Ejercicio 8
    print("Indentar izquierda:", ident_izq("12345", 10))  # Ejercicio 9
    print("Indentar derecha:", ident_der("12345", 10))  # Ejercicio 9
    print("Indentar centrado:", ident_cen("12345", 10))  # Ejercicio 9
