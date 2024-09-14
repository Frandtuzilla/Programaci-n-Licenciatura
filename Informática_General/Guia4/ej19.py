totalHuevos = 0
pesoTotalChocolate = 0
maxCantidad60g = 0

continuar = True
while continuar:

    tamaño = int(input("Ingrese el tamaño del huevo (60g, 120g o 0 para finalizar): "))

    if tamaño == 0:
        continuar = False
    elif tamaño != 60 and tamaño != 120:
        print("Tamaño inválido. Solo se aceptan tamaños de 60g o 120g.")
    else:
        cantidad = int(input("Ingrese la cantidad de huevos: "))

        totalHuevos += cantidad

        pesoTotalChocolate += tamaño * cantidad

        if tamaño == 60 and cantidad > maxCantidad60g:
            maxCantidad60g = cantidad

print("\nResultados:")
print(f"A) Total de huevos de pascua a fabricar: {totalHuevos}")
print(f"B) Peso total de chocolate necesario: {pesoTotalChocolate} gramos")
print(f"C) Máxima cantidad pedida en huevos de 60 gramos: {maxCantidad60g}")