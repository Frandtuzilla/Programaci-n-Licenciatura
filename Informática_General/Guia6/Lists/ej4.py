def borrar_rango(L, start, stop, step):
    # Si el paso es 0, no se puede avanzar, así que devolvemos la lista original
    if step == 0:
        return L
    
    # Ajustamos los índices de inicio y fin según la dirección del paso
    if step > 0:
        # Para paso positivo, aseguramos que start no sea negativo y stop no exceda la longitud de la lista
        start = max(0, start)
        stop = min(stop, len(L))
    else:
        # Para paso negativo, aseguramos que start no exceda la longitud de la lista y stop no sea menor que -1
        start = min(start, len(L) - 1)
        stop = max(-1, stop)
    
    i = start  # i es el índice de lectura
    j = start  # j es el índice de escritura
    
    # Recorremos la lista, saltando elementos según el paso
    if step > 0:
        # Para pasos positivos, avanzamos hacia adelante
        while i < len(L) and i < stop:
            # Si el índice actual no debe ser eliminado, lo copiamos
            if (i - start) % step != 0:
                L[j] = L[i]
                j += 1  # Avanzamos el índice de escritura
            i += 1  # Siempre avanzamos el índice de lectura
    else:
        # Para pasos negativos, avanzamos hacia atrás
        while i < len(L) and i > stop:
            # Si el índice actual no debe ser eliminado, lo copiamos
            if (i - start) % step != 0:
                L[j] = L[i]
                j += 1  # Avanzamos el índice de escritura
            i += 1  # Aunque el paso es negativo, i sigue aumentando porque recorremos la lista de izquierda a derecha
    
    # Copiamos los elementos restantes después del rango
    while i < len(L):
        L[j] = L[i]
        i += 1
        j += 1
    
    # Acortamos la lista para eliminar los elementos sobrantes al final
    L[:] = L[:j]
    
    return L  # Devolvemos la lista modificada

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Lista original:", L)
    
    a = borrar_rango(L, 2, 6, 2)
    print("Lista después de borrar el rango:", a)
    print("¿Es 'a' la misma lista que 'L'?", L is a)  # Debe imprimir True
