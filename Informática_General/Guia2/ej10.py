numero = input("Ingrese un número entero: ")

if  numero[0] == '0':
    print("El primer diígito no puede ser \"0\".")
else:
    print(f"El número tiene {len(numero)} dígitos.")
    numero = int(float(numero))
    print(f"El número introducido es par y múltiplo de 10: {bool(numero%2 == 0 and numero%10 == 0)}")    
