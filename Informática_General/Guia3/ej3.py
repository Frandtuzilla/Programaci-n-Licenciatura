fecha = input("Ingrese una fecha para verificar si es año bisiesto: ")

anio = int(fecha[-4:])
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es año bisiesto.")
else:
    print("No es año bisiesto.")
