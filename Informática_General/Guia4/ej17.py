import math

continuarPrograma = True

while continuarPrograma:
    print("\n--- Menú Principal ---")
    print("1. Perímetros")
    print("2. Áreas")
    print("3. Salir")
    opcionPrincipal = int(input("Elige una opción: "))

    if opcionPrincipal == 1: 
        regresarPerimetros = False
        while not regresarPerimetros:
            print("\n--- Menú de Perímetros ---")
            print("1. Triángulo")
            print("2. Cuadrado")
            print("3. Círculo")
            print("4. Regresar al menú principal")
            opcionPerimetros = int(input("Elige una opción: "))
            
            if opcionPerimetros == 1:
                lado1 = float(input("Introduce el lado 1 del triángulo: "))
                lado2 = float(input("Introduce el lado 2 del triángulo: "))
                lado3 = float(input("Introduce el lado 3 del triángulo: "))
                perimetro = lado1 + lado2 + lado3
                print(f"El perímetro del triángulo es: {perimetro}")
            elif opcionPerimetros == 2:
                lado = float(input("Introduce el lado del cuadrado: "))
                perimetro = 4 * lado
                print(f"El perímetro del cuadrado es: {perimetro}")
            elif opcionPerimetros == 3:
                radio = float(input("Introduce el radio del círculo: "))
                perimetro = 2 * math.pi * radio
                print(f"El perímetro del círculo es: {perimetro:.2f}")
            elif opcionPerimetros == 4:
                regresarPerimetros = True
            else:
                print("Opción inválida. Intenta de nuevo.")
    
    elif opcionPrincipal == 2: 
        regresarAreas = False
        while not regresarAreas:
            print("\n--- Menú de Áreas ---")
            print("1. Triángulo")
            print("2. Cuadrado")
            print("3. Círculo")
            print("4. Regresar al menú principal")
            opcionAreas = int(input("Elige una opción: "))
            
            if opcionAreas == 1:
                base = float(input("Introduce la base del triángulo: "))
                altura = float(input("Introduce la altura del triángulo: "))
                area = (base * altura) / 2
                print(f"El área del triángulo es: {area}")
            elif opcionAreas == 2:
                lado = float(input("Introduce el lado del cuadrado: "))
                area = lado ** 2
                print(f"El área del cuadrado es: {area}")
            elif opcionAreas == 3:
                radio = float(input("Introduce el radio del círculo: "))
                area = math.pi * (radio ** 2)
                print(f"El área del círculo es: {area:.2f}")
            elif opcionAreas == 4:
                regresarAreas = True
            else:
                print("Opción inválida. Intenta de nuevo.")
    
    elif opcionPrincipal == 3:
        print("Saliendo del programa...")
        continuarPrograma = False
    else:
        print("Opción inválida. Intenta de nuevo.")
