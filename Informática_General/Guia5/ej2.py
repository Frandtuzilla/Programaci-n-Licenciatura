def resolver_ecuacion_lineal(a, b):
    if a == 0:
        if b == 0:
            return "infinitas"  # Infinitas soluciones (0 = 0)
        else:
            return "ninguna"  # Sin solución (0 = número distinto de 0)
    else:
        return -b / a  # Solución única: x = -b/a

# Ejemplo de uso
try:
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))

    solucion = resolver_ecuacion_lineal(a, b)

    if solucion == "infinitas":
        print("La ecuación tiene infinitas soluciones.")
    elif solucion == "ninguna":
        print("La ecuación no tiene solución.")
    else:
        print(f"La solución de la ecuación {a}x + {b} = 0 es x = {solucion:.2f}")
except ValueError:
    print("Error: Por favor, introduce valores numéricos válidos.")
