def mcd(a, b):
    """
    Calcula el máximo común divisor de a y b usando el algoritmo de Euclides.
    
    Este algoritmo funciona de la siguiente manera:
    1. Si b es 0, a es el MCD.
    2. Si no, el MCD de a y b es el mismo que el MCD de b y el resto de a dividido por b.
    3. Repetimos este proceso hasta que b sea 0.
    """
    
    # Versión iterativa compacta (comentada):
    # while b:
    #     a, b = b, a % b
    # return a
    
    while b:
        # Guardamos el valor actual de b en una variable temporal
        temp = b
        # Calculamos el resto de a dividido por b
        resto = a % b
        # Asignamos a 'a' el valor anterior de 'b'
        a = temp
        # Asignamos a 'b' el valor del resto
        b = resto
    # Cuando b llega a 0, a contiene el MCD
    return a

def simplificar_fraccion(numerador, denominador):
    """Simplifica una fracción y devuelve el resultado."""
    divisor = mcd(numerador, denominador)
    return numerador // divisor, denominador // divisor

def sumar_fracciones(n1, d1, n2, d2):
    """Suma dos fracciones y devuelve el resultado."""
    nuevo_numerador = n1 * d2 + n2 * d1
    nuevo_denominador = d1 * d2
    return simplificar_fraccion(nuevo_numerador, nuevo_denominador)

# Pedir las fracciones al usuario
print("Ingrese la primera fracción:")
n1 = int(input("Numerador: "))
d1 = int(input("Denominador: "))

print("\nIngrese la segunda fracción:")
n2 = int(input("Numerador: "))
d2 = int(input("Denominador: "))

# a) Simplificar y mostrar las fracciones
s_n1, s_d1 = simplificar_fraccion(n1, d1)
s_n2, s_d2 = simplificar_fraccion(n2, d2)

print(f"\na) Fracciones simplificadas:")
print(f"   Primera fracción: {s_n1}/{s_d1}")
print(f"   Segunda fracción: {s_n2}/{s_d2}")

# b) Sumar las fracciones y mostrar el resultado simplificado
suma_n, suma_d = sumar_fracciones(n1, d1, n2, d2)

print(f"\nb) Suma de fracciones simplificada:")
print(f"   Resultado: {suma_n}/{suma_d}")
