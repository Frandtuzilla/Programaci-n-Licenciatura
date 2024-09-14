mayorEdad = -1
menorAltura = float('inf')
nombreMayorEdad = ""
nombreMenorAltura = ""
sumaEdades = 0
sumaAlturas = 0
jugadores = 10
i = 0

while i < jugadores:
    print(f"Jugador {i+1}:")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura (en metros): "))

    if edad > mayorEdad:
        mayorEdad = edad
        nombreMayorEdad = nombre

    if altura < menorAltura:
        menorAltura = altura
        nombreMenorAltura = nombre

    sumaEdades += edad
    sumaAlturas += altura

    i += 1

promedioEdades = sumaEdades / jugadores
promedioAlturas = sumaAlturas / jugadores

print("\nResultados:")
print(f"Nombre del jugador de mayor edad: {nombreMayorEdad}")
print(f"Nombre del jugador de menor altura: {nombreMenorAltura}")
print(f"Promedio de edades: {promedioEdades:.2f}")
print(f"Promedio de alturas: {promedioAlturas:.2f} metros")
