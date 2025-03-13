# Archivo ej6.py sin uso de set

def set_agregar(L, v):
    """Agrega un valor a la lista si no está presente."""
    if v not in L:
        L.append(v)
    return L

def set_borrar(L, v):
    """Elimina un valor de la lista si está presente."""
    if v in L:
        L.remove(v)
    return L

def set_union(L1, L2):
    """Devuelve la unión de dos listas, sin duplicados."""
    resultado = L1[:]  # Copia de L1
    for elemento in L2:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def set_interseccion(L1, L2):
    """Devuelve la intersección de dos listas."""
    resultado = []
    for elemento in L1:
        if elemento in L2 and elemento not in resultado:
            resultado.append(elemento)
    return resultado

def set_resta(L1, L2):
    """Devuelve los elementos de L1 que no están en L2."""
    resultado = []
    for elemento in L1:
        if elemento not in L2:
            resultado.append(elemento)
    return resultado

def set_diferencia_sim(L1, L2):
    """Devuelve la diferencia simétrica entre L1 y L2 (elementos exclusivos de cada lista)."""
    resultado = []
    for elemento in L1:
        if elemento not in L2 and elemento not in resultado:
            resultado.append(elemento)
    for elemento in L2:
        if elemento not in L1 and elemento not in resultado:
            resultado.append(elemento)
    return resultado

# Ejemplo de uso:
L1 = [1, 2, 3]
L2 = [3, 4, 5]
print("Agregar 4 a L1:", set_agregar(L1, 4))         # Debería agregar 4 a L1 si no está presente
print("Borrar 2 de L1:", set_borrar(L1, 2))          # Debería eliminar 2 de L1 si está presente
print("Unión de L1 y L2:", set_union(L1, L2))        # Debería devolver [1, 2, 3, 4, 5]
print("Intersección de L1 y L2:", set_interseccion(L1, L2))  # Debería devolver [3]
print("Resta de L1 y L2:", set_resta(L1, L2))        # Debería devolver [1, 2]
print("Diferencia simétrica de L1 y L2:", set_diferencia_sim(L1, L2))  # Debería devolver [1, 2, 4, 5]
