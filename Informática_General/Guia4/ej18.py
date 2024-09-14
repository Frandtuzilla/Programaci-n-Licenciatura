mayorSuperficie = 0
zonaMayorSuperficie = ""
totalDatos = 0
superficiesMayores100 = 0
continuar = True

while continuar:
    zona = input("Ingrese la zona (A, B, C o Z para finalizar): ").upper()

    if zona == "Z":
        continuar = False
    elif zona != "A" and zona != "B" and zona != "C":
        print("Zona inválida. Intenta de nuevo.")
    else:

        superficie = float(input("Ingrese la superficie (mínimo 40 metros cuadrados): "))

        if superficie >= 40:

            totalDatos += 1

            if superficie > mayorSuperficie:
                mayorSuperficie = superficie
                zonaMayorSuperficie = zona

            if superficie > 100:
                superficiesMayores100 += 1
        else:
            print("Superficie inválida. Debe ser al menos 40 metros cuadrados.")

if totalDatos > 0:
    porcentajeMayores100 = (superficiesMayores100 / totalDatos) * 100
else:
    porcentajeMayores100 = 0

print("\nResultados:")
print(f"A) Zona donde se registró la mayor superficie: {zonaMayorSuperficie}")
print(f"B) Cantidad total de datos ingresados: {totalDatos}")
print(f"C) Porcentaje de superficies mayores a 100 metros cuadrados: {porcentajeMayores100:.2f}%")
