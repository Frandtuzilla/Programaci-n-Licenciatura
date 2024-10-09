def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_anio(anio):
    return 366 if es_bisiesto(anio) else 365

# Ejemplo de uso
try:
    anio_usuario = int(input("Introduce un año: "))
    dias = dias_en_anio(anio_usuario)
    print(f"El año {anio_usuario} tiene {dias} días.")
except ValueError:
    print("Error: Por favor, introduce un número entero válido para el año.")
