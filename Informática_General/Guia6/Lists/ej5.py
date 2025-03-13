import random

def random_pick(L, n):
    """    
    Args:
    L (list): La lista de donde se seleccionarán los elementos.
    n (int): Cantidad de elementos a seleccionar. Si es negativo, excluye esa cantidad desde el final.
    
    Returns:
    list: Una lista con los elementos seleccionados al azar.
    """
    if n >= 0:
        cantidad = min(n, len(L))
    else:
        cantidad = max(len(L) + n, 0)
    
    resultado = []
    indices_usados = [False] * len(L)  # Lista para rastrear si un índice fue usado
    
    while len(resultado) < cantidad:
        indice = random.randint(0, len(L) - 1)  # Seleccionar un índice aleatorio
        if not indices_usados[indice]:  # Verificar si el índice no fue usado
            indices_usados[indice] = True  # Marcar el índice como usado
            resultado.append(L[indice])  # Agregar el elemento correspondiente
    
    return resultado

# Ejemplo de uso:
print(random_pick([1, 2, 3, 4, 5], 2))  # Elige dos elementos aleatorios
print(random_pick([1, 2, 3, 4, 5], -2))  # Deja dos elementos afuera
