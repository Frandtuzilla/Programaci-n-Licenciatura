# A. Definir una variable mensaje de tipo string que informe el porcentaje que representan las ventas del 2do trimestre sobre el total.
# B. Escribir una expresión para evaluar si el mayor monto de ventas ocurre en el último trimestre
# C.  Dada la cantidad de ventas en el año en la variable cantidadVentas, calcular el importe promedio de las ventas del año

Trimestre1 = 40
Trimestre2 = 50
Trimestre3 = 20
Trimestre4 = 30

cantidadVentas = Trimestre1 + Trimestre2 + Trimestre3 + Trimestre4

mensaje = "Porcentaje de ventas del 2do trimestre: " + str(round((Trimestre2*100)/cantidadVentas,2)) + "%"

aux1 = "no fue"

if( Trimestre4 > Trimestre1 and Trimestre4 > Trimestre2 and Trimestre4 > Trimestre3):
    aux1 = "fue"

mayorMontoVentas = "El mayor monto de ventas " + aux1 + " en el último trimestre."

promedioVentas = cantidadVentas/4

aux2 = "El promedio de ventas es " + str(promedioVentas)

print(f"\nEjercicio A: {mensaje} \nEjercicio B: {mayorMontoVentas} \nEjercicio C: {aux2} \n")