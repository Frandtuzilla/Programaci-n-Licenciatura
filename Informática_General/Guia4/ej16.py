sumaPromedios = 0
cantidadAlumnos = 0
registrarAlumnos = True

while registrarAlumnos:

    print(f"Ingrese las calificaciones de 3 parciales para el alumno {cantidadAlumnos + 1}:")
    calificacion1 = float(input("Calificación del primer parcial: "))
    calificacion2 = float(input("Calificación del segundo parcial: "))
    calificacion3 = float(input("Calificación del tercer parcial: "))

    promedioAlumno = (calificacion1 + calificacion2 + calificacion3) / 3
    print(f"Promedio del alumno {cantidadAlumnos + 1}: {promedioAlumno:.2f}")

    sumaPromedios += promedioAlumno
    cantidadAlumnos += 1

    respuesta = input("¿Desea registrar otro alumno? (s/n): ")
    if respuesta == 'n':
        registrarAlumnos = False

if cantidadAlumnos > 0:
    promedioGeneral = sumaPromedios / cantidadAlumnos
    print(f"\nPromedio general del grupo: {promedioGeneral:.2f}")
else:
    print("No se registraron alumnos.")
