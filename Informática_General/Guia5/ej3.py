def son_amigos(num1, num2):
    def suma_divisores(n):
        suma = 1  # 1 siempre es divisor
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:  # evita contar dos veces la raíz cuadrada
                    suma += n // i
        return suma
    
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# Ejemplo de uso
print(son_amigos(220, 284))  # Debería imprimir True
print(son_amigos(1184, 1210))  # Debería imprimir True
print(son_amigos(2620, 2924))  # Debería imprimir True
print(son_amigos(10, 20))  # Debería imprimir False
