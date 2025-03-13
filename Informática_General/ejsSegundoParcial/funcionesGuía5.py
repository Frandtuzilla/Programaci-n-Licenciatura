# Archivo ej1.py

def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_anio(anio):
    """Devuelve el número de días en un año (365 o 366)."""
    return 366 if es_bisiesto(anio) else 365

# Ejemplo de uso:
print(es_bisiesto(2024))  # Debería imprimir True
print(dias_en_anio(2024))  # Debería imprimir 366


# Archivo ej2.py

def resolver_ecuacion_lineal(a, b):
    """Resuelve una ecuación lineal de la forma ax + b = 0."""
    if a == 0:
        if b == 0:
            return "infinitas"  # Infinitas soluciones (0 = 0)
        else:
            return "ninguna"  # Sin solución (0 = número distinto de 0)
    else:
        return -b / a  # Solución única: x = -b/a

# Ejemplo de uso:
print(resolver_ecuacion_lineal(2, -4))  # Debería imprimir 2.0


# Archivo ej3.py

def son_amigos(num1, num2):
    """Determina si dos números son amigos."""
    def suma_divisores(n):
        suma = 1  # 1 siempre es divisor
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:  # evita contar dos veces la raíz cuadrada
                    suma += n // i
        return suma
    
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# Ejemplo de uso:
print(son_amigos(220, 284))  # Debería imprimir True
print(son_amigos(1184, 1210))  # Debería imprimir True
print(son_amigos(2620, 2924))  # Debería imprimir True
print(son_amigos(10, 20))  # Debería imprimir False


# Archivo ej4.py

def suma_divisores(num):
    """Calcula la suma de los divisores de un número."""
    suma = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            suma += i
            if i != num // i:
                suma += num // i
    return suma

def encontrar_amigos(n):
    """Encuentra todos los pares de números amigos menores que n."""
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
    """Muestra en pantalla los pares de números amigos menores que n."""
    amigos = encontrar_amigos(n)
    for a, b in amigos:
        print(f"{a} y {b} son amigos")

def main():
    """Función principal que solicita un número al usuario e imprime los pares de números amigos menores que dicho número."""
    n = int(input("Ingrese un número n: "))
    print(f"Parejas de números amigos menores que {n}:")
    mostrar_amigos(n)

# Ejemplo de uso:
print(suma_divisores(220))  # Debería imprimir 284
print(encontrar_amigos(3000))  # Debería incluir (220, 284)
mostrar_amigos(3000)  # Imprime parejas como "220 y 284 son amigos"

if __name__ == "__main__":
    main()


# Archivo ej6.py

def mostrar_cifras_inverso(numero):
    """Muestra las cifras de un número en orden inverso."""
    numero_str = str(abs(numero))  # Convertir el número a cadena para facilitar la iteración
    
    for digito in reversed(numero_str):
        print(digito)

# Ejemplo de uso:
mostrar_cifras_inverso(12345)  # Debería imprimir 5, 4, 3, 2, 1 en líneas separadas


# Archivo ej7.py

def es_primo(numero):
    """Determina si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def muestra_primos(limite):
    """Muestra todos los números primos entre 1 y el límite dado."""
    print(f"Números primos entre 1 y {limite}:")
    for num in range(2, limite + 1):
        if es_primo(num):
            print(num, end=" ")
    print()  # Añadir un salto de línea al final

# Ejemplo de uso:
muestra_primos(20)  # Debería imprimir 2, 3, 5, 7, 11, 13, 17, 19 en una línea


# Archivo ej8.py

def es_perfecto(numero):
    """Determina si un número es perfecto."""
    if numero <= 0:
        return False
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

def obtener_numero_perfecto():
    """Pide al usuario un número hasta que ingrese un número perfecto."""
    while True:
        try:
            p = int(input("Ingrese un número entero positivo: "))
            if p > 0 and es_perfecto(p):
                return p
            else:
                print("El número ingresado no es perfecto. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

# Ejemplo de uso:
print(es_perfecto(28))  # Debería imprimir True
print(es_perfecto(10))  # Debería imprimir False


# Archivo ej9.py

def mcd(a, b):
    """Calcula el máximo común divisor de dos números."""
    while b:
        a, b = b, a % b
    return a

def son_coprimos(a, b):
    """Determina si dos números son coprimos."""
    return mcd(a, b) == 1

# Ejemplo de uso:
print(mcd(48, 18))  # Debería imprimir 6
print(son_coprimos(17, 4))  # Debería imprimir True
print(son_coprimos(15, 25))  # Debería imprimir False


# Archivo ej10.py

def factorial(n):
    """Calcula el factorial de un número."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def combinacion(m, n):
    """Calcula la combinación de m elementos tomados de a n."""
    return factorial(m) // (factorial(m - n) * factorial(n))

def variacion(m, n):
    """Calcula la variación de m elementos tomados de a n."""
    return factorial(m) // factorial(m - n)

# Ejemplo de uso:
print(factorial(5))       # Debería imprimir 120
print(combinacion(5, 3))  # Debería imprimir 10
print(variacion(5, 3))    # Debería imprimir 60


# Archivo ej11.py

def mcd(a, b):
    """Calcula el Máximo Común Divisor (MCD) de dos números usando el método de resta sucesiva."""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def mcm(a, b):
    """Calcula el Mínimo Común Múltiplo (MCM) de dos números."""
    mcd_valor = mcd(a, b)
    return (a * b) // mcd_valor, mcd_valor

# Ejemplo de uso:
print(mcd(48, 18))        # Debería imprimir 6
print(mcm(48, 18))        # Debería imprimir (144, 6)


# Archivo ej12.py

def mcd(a, b):
    """Calcula el máximo común divisor de a y b usando el algoritmo de Euclides."""
    while b:
        temp = b
        resto = a % b
        a = temp
        b = resto
    return a

def simplificar_fraccion(numerador, denominador):
    """Simplifica una fracción y devuelve el resultado."""
    divisor = mcd(numerador, denominador)
    return numerador // divisor, denominador // divisor

def sumar_fracciones(n1, d1, n2, d2):
    """Suma dos fracciones y devuelve el resultado simplificado."""
    nuevo_numerador = n1 * d2 + n2 * d1
    nuevo_denominador = d1 * d2
    return simplificar_fraccion(nuevo_numerador, nuevo_denominador)

# Ejemplo de uso:
print(simplificar_fraccion(4, 8))  # Debería imprimir (1, 2)
print(sumar_fracciones(1, 2, 1, 3))  # Debería imprimir (5, 6)


# Archivo ej13.py

def dectobin(decimal):
    """Convierte un número decimal a binario."""
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

def bintodec(binario):
    """Convierte un número binario a decimal."""
    decimal = 0
    potencia = 0
    for digito in binario[::-1]:
        if digito == "1":
            decimal += 2 ** potencia
        potencia += 1
    return decimal

# Ejemplo de uso:
print(dectobin(13))   # Debería imprimir "1101"
print(bintodec("1101"))  # Debería imprimir 13
