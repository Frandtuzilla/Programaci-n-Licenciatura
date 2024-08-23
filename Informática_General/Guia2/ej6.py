numero1 = int(float(input("Ingrese el primer número: ")))
numero2 = int(float(input("Ingrese el segundo número: ")))

aux1 = bool(numero1%2 and numero2%2 == 0)
aux2 = bool((numero1+numero2)%2 == 0)
aux3 = bool(numero1**2 < numero2)
aux4 = bool(numero1==numero2)
aux5 = bool(numero1%3 == 0 and numero2%5 == 0)

print(f"\nEl primer número es impar y el segundo par: {aux1}")
print(f"\nLa suma de ambos números es par: : {aux2}")
print(f"\nEl primer número al cuadrado es menor que el segundo número: {aux3}")
print(f"\nLos dos números son iguales: {aux4}")
print(f"\nEl primero es divisible por tres y el segundo divisible por 5: {aux5}\n")
