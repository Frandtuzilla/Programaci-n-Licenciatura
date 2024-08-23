precioDocena = input("Ingresar precio de la docena: $")

print(f"1. El número de pesos (la parte entera): ${str(int(float(precioDocena)))}")
print(f"2. El número de centavos: ${str(float(precioDocena) - int(float(precioDocena)))}")
print(f"3. El precio redondeado a sólo un decimal: ${str(round(float(precioDocena),1))}")
print(f"4. El precio de una unidad expresado como un valor entero: ${str(int(float(precioDocena)/12))}")