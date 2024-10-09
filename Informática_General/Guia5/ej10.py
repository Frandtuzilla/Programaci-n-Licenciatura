def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def combinacion(m, n):
    return factorial(m) // (factorial(m - n) * factorial(n))

def variacion(m, n):
    return factorial(m) // factorial(m - n)

def main():
    numero = int(input("Introduce un número: "))
    print("Elige una operación:")
    print("1. Permutación de n")
    print("2. Variación de m tomados de a n")
    print("3. Combinación de m tomados de a n")
    
    opcion = int(input("Ingresa el número de la operación deseada: "))
    
    if opcion == 1:
        resultado = factorial(numero)
        print(f"La permutación de {numero} es: {resultado}")
    elif opcion == 2 or opcion == 3:
        m = numero
        n = int(input("Introduce el valor de n: "))
        if opcion == 2:
            resultado = variacion(m, n)
            print(f"La variación de {m} tomados de a {n} es: {resultado}")
        else:
            resultado = combinacion(m, n)
            print(f"La combinación de {m} tomados de a {n} es: {resultado}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
