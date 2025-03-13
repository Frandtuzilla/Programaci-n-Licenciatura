def stack_push(L, v):
    return L + [v]

def stack_pop(L):
    if not L:
        return None
    ultimo_elemento = L[-1]
    L[:] = L[:-1]
    return ultimo_elemento

if __name__ == "__main__":
    L = [1]
    print("Lista inicial:", L)

    L = stack_push(L, 2)
    print("Después de push(2):", L)

    L = stack_push(L, 3)
    print("Después de push(3):", L)

    a = stack_pop(L)
    print("Pop:", a, "Lista actual:", L)

    a = stack_pop(L)
    print("Pop:", a, "Lista actual:", L)

    a = stack_pop(L)
    print("Pop:", a, "Lista actual:", L)

    a = stack_pop(L)
    print("Pop:", a, "Lista actual:", L)
