def es_primo(numero):
    """
    Determina si un número es primo.
    
    Args:
    numero (int): El número a evaluar.
    
    Returns:
    bool: True si es primo, False si no lo es.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def muestra_primos(limite):
    """
    Muestra todos los números primos entre 1 y el límite dado.
    
    Args:
    limite (int): El límite superior hasta donde buscar primos.
    """
    print(f"Números primos entre 1 y {limite}:")
    for num in range(2, limite + 1):
        if es_primo(num):
            print(num, end=" ")
    print()  # Para añadir un salto de línea al final

# Solicitar al usuario que ingrese el límite
limite = 0
while limite <= 0:
    try:
        limite = int(input("Por favor, ingrese el número límite para buscar primos: "))
        if limite <= 0:
            print("Por favor, ingrese un número positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Llamar a la función con el límite ingresado por el usuario
muestra_primos(limite)
