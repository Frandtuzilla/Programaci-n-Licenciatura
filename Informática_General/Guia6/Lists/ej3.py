def eliminar_valor(L, v):
    # Inicializamos j como el índice donde colocaremos los elementos a mantener
    j = 0
    
    # Recorremos la lista utilizando los índices
    for i in range(len(L)):
        # Si el elemento actual no es el valor a eliminar
        if L[i] != v:
            # Copiamos el elemento a la posición j
            L[j] = L[i]
            # Incrementamos j para la próxima posición de escritura
            j += 1
    
    # Acortamos la lista para eliminar los elementos sobrantes
    L[:] = L[:j]
    
    # Retornamos la lista modificada (que es la misma lista original)
    return L

if __name__ == "__main__":
    # Ejemplo de uso
    L = [1, 3, 1, 4]
    print("Lista original:", L)
    
    a = eliminar_valor(L, 1)
    print("Lista después de eliminar el valor 1:", a)
    print("¿Es 'a' la misma lista que 'L'?", L is a)  # Debe imprimir True
