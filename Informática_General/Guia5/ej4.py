def suma_divisores(num):
    suma = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            suma += i
            if i != num // i:
                suma += num // i
    return suma

def encontrar_amigos(n):
    sumas = [0] * n
    amigos = []
    for i in range(1, n):
        if sumas[i] == 0:
            sumas[i] = suma_divisores(i)
        if sumas[i] < n and sumas[i] > i:
            j = sumas[i]
            if sumas[j] == 0:
                sumas[j] = suma_divisores(j)
            if sumas[j] == i:
                amigos.append((i, j))
    return amigos

def mostrar_amigos(n):
    amigos = encontrar_amigos(n)
    for a, b in amigos:
        print(f"{a} y {b} son amigos")

def main():
    n = int(input("Ingrese un número n: "))
    print(f"Parejas de números amigos menores que {n}:")
    mostrar_amigos(n)

if __name__ == "__main__":
    main()