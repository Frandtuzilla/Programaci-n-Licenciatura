numFactorial = int(float(input("Escribe un número entero mayor que cero: ")))

while numFactorial < 0:
    print("¡Le he pedido un número mayor que cero!")
    numFactorial = int(float(input("\nEscribe un número entero mayor que cero: ")))

result = 1
aux = numFactorial

while aux >= 0:
    if aux == 0:
        result *= 1
    else:
        result *= aux
    aux -= 1

print(f"El factorial de {numFactorial} es: {result}\n")