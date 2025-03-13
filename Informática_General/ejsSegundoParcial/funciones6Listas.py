# Archivo combinado con funciones de ejercicios y comentarios detallados.
# Las funciones han sido ajustadas para no usar `set`.

# Ejercicio 1
def filtrar_valor(L, v):
    """Devuelve una lista sin el valor especificado."""
    lista_filtrada = []  # Inicializa una nueva lista vacía.
    for elemento in L:  # Recorre cada elemento de la lista original.
        if elemento != v:  # Si el elemento no es igual al valor a filtrar:
            lista_filtrada = lista_filtrada + [elemento]  # Añade el elemento a la nueva lista.
    return lista_filtrada  # Devuelve la nueva lista filtrada.

# Ejercicio 2
def stack_push(L, v):
    """Agrega un elemento al final de la lista."""
    return L + [v]  # Devuelve una nueva lista con el elemento agregado al final.

def stack_pop(L):
    """Elimina y retorna el último elemento de la lista."""
    if not L:  # Si la lista está vacía:
        return None  # Retorna None.
    ultimo_elemento = L[-1]  # Obtiene el último elemento de la lista.
    L[:] = L[:-1]  # Modifica la lista original eliminando el último elemento.
    return ultimo_elemento  # Devuelve el último elemento eliminado.

# Ejercicio 3
def eliminar_valor(L, v):
    """Elimina todas las ocurrencias de un valor en la lista."""
    j = 0  # Índice de posición para reconstruir la lista.
    for i in range(len(L)):  # Recorre cada índice de la lista.
        if L[i] != v:  # Si el valor en la posición actual no es igual al valor a eliminar:
            L[j] = L[i]  # Mueve el elemento a la posición `j`.
            j += 1  # Incrementa el índice para la nueva posición.
    L[:] = L[:j]  # Recorta la lista eliminando las ocurrencias del valor.
    return L  # Devuelve la lista modificada.

# Ejercicio 4
def borrar_rango(L, start, stop, step):
    """Elimina elementos en un rango específico con un paso determinado."""
    if step == 0:  # Si el paso es 0, no realiza cambios.
        return L
    if step > 0:  # Ajusta los límites si el paso es positivo.
        start = max(0, start)
        stop = min(stop, len(L))
    else:  # Ajusta los límites si el paso es negativo.
        start = min(start, len(L) - 1)
        stop = max(-1, stop)
    
    i = start  # Índice para recorrer la lista.
    j = start  # Índice para reconstruir la lista.
    
    while i < len(L) and (i < stop if step > 0 else i > stop):
        if (i - start) % step != 0:  # Si el índice no coincide con el paso:
            L[j] = L[i]  # Mueve el elemento a la nueva posición.
            j += 1
        i += 1  # Avanza al siguiente índice.
    
    while i < len(L):  # Mueve los elementos restantes fuera del rango.
        L[j] = L[i]
        i += 1
        j += 1
    
    L[:] = L[:j]  # Recorta la lista para eliminar los elementos dentro del rango.
    return L  # Devuelve la lista modificada.

# Ejercicio 5
import random

def random_pick(L, n):
    """
    Selecciona una cantidad de elementos al azar de la lista sin usar random.sample ni set.
    """
    if n >= 0:  # Si n es positivo, selecciona hasta `n` elementos.
        cantidad = min(n, len(L))
    else:  # Si n es negativo, excluye esa cantidad desde el final.
        cantidad = max(len(L) + n, 0)
    
    resultado = []  # Inicializa la lista de resultados.
    indices_usados = [False] * len(L)  # Crea una lista para rastrear índices usados.
    
    while len(resultado) < cantidad:  # Mientras no se hayan seleccionado suficientes elementos:
        indice = random.randint(0, len(L) - 1)  # Genera un índice aleatorio.
        if not indices_usados[indice]:  # Si el índice no fue usado:
            indices_usados[indice] = True  # Marca el índice como usado.
            resultado.append(L[indice])  # Añade el elemento al resultado.
    
    return resultado  # Devuelve la lista de elementos seleccionados.

# Ejercicio 6
def set_agregar(L, v):
    """Agrega un valor a la lista si no está presente."""
    if v not in L:  # Si el valor no está en la lista:
        L.append(v)  # Añade el valor al final.
    return L

def set_borrar(L, v):
    """Elimina un valor de la lista si está presente."""
    if v in L:  # Si el valor está en la lista:
        L.remove(v)  # Lo elimina.
    return L

def set_union(L1, L2):
    """Devuelve la unión de dos listas, sin duplicados."""
    resultado = L1[:]  # Copia de la primera lista.
    for elemento in L2:  # Recorre cada elemento de la segunda lista.
        if elemento not in resultado:  # Si el elemento no está en el resultado:
            resultado.append(elemento)  # Lo agrega.
    return resultado

def set_interseccion(L1, L2):
    """Devuelve la intersección de dos listas."""
    resultado = []  # Lista vacía para almacenar la intersección.
    for elemento in L1:  # Recorre cada elemento de la primera lista.
        if elemento in L2 and elemento not in resultado:  # Si está en ambas listas y no está repetido:
            resultado.append(elemento)  # Lo agrega al resultado.
    return resultado

def set_resta(L1, L2):
    """Devuelve los elementos de L1 que no están en L2."""
    resultado = []  # Lista vacía para almacenar la resta.
    for elemento in L1:  # Recorre cada elemento de la primera lista.
        if elemento not in L2:  # Si el elemento no está en la segunda lista:
            resultado.append(elemento)  # Lo agrega al resultado.
    return resultado

def set_diferencia_sim(L1, L2):
    """Devuelve la diferencia simétrica entre L1 y L2."""
    resultado = []  # Lista vacía para almacenar la diferencia simétrica.
    for elemento in L1:  # Elementos únicos en L1.
        if elemento not in L2:
            resultado.append(elemento)
    for elemento in L2:  # Elementos únicos en L2.
        if elemento not in L1:
            resultado.append(elemento)
    return resultado

# Ejemplo de uso de todas las funciones
if __name__ == "__main__":
    # Ejercicio 1
    print("Filtrar valor:", filtrar_valor([1, 2, 3, 2, 4], 2))
    
    # Ejercicio 2
    stack = [1]
    stack = stack_push(stack, 2)
    print("Push:", stack)
    print("Pop:", stack_pop(stack), "Stack después del pop:", stack)
    
    # Ejercicio 3
    lista = [1, 3, 1, 4]
    print("Eliminar valor 1:", eliminar_valor(lista, 1))
    
    # Ejercicio 4
    lista = [1, 2, 3, 4, 5, 6, 7]
    print("Borrar rango:", borrar_rango(lista, 2, 6, 2))
    
    # Ejercicio 5
    print("Random pick:", random_pick([1, 2, 3, 4, 5], 2))
    
    # Ejercicio 6
    L1 = [1, 2, 3]
    L2 = [3, 4, 5]
    print("Set agregar:", set_agregar(L1, 4))
    print("Set borrar:", set_borrar(L1, 2))
    print("Set unión:", set_union(L1, L2))
    print("Set intersección:", set_interseccion(L1, L2))
    print("Set resta:", set_resta(L1, L2))
    print("Set diferencia simétrica:", set_diferencia_sim(L1, L2))
