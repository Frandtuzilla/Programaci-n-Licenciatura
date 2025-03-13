def filtrar_valor(L, v):
    lista_filtrada = []
    for elemento in L:
        if elemento != v:
            lista_filtrada = lista_filtrada + [elemento]
    return lista_filtrada

# Ejemplo de uso
lista_original = [1, 2, 3, 2, 4, 2, 5]
valor_a_filtrar = 2
lista_filtrada = filtrar_valor(lista_original, valor_a_filtrar)
print(f"Lista original: {lista_original}")
print(f"Lista filtrada (sin {valor_a_filtrar}): {lista_filtrada}")
