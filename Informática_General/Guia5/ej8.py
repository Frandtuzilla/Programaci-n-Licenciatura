def es_perfecto(numero):
    """
    Determina si un número es perfecto.
    Un número es perfecto si la suma de sus divisores (excluyendo el propio número) es igual al número.
    """
    if numero <= 0:
        return False
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

def obtener_numero_perfecto():
    """
    Pide al usuario un número hasta que ingrese un número perfecto.
    """
    while True:
        try:
            p = int(input("Ingrese un número entero positivo: "))
            if p > 0 and es_perfecto(p):
                return p
            else:
                print("El número ingresado no es perfecto. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Programa principal
p = obtener_numero_perfecto()
print(f"El número perfecto ingresado es: {p}")