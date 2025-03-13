import statistics

# Ejercicio 1: Programa para datos de baloncesto
apellidos = ["Perez", "Gomez", "Ruiz", "Lopez", "Sanchez"]
alturas = [1.85, 1.92, 2.10, 1.88, 1.95]
tantos = [25, 30, 35, 20, 40]

# a) Promedio de tantos por rango de altura
menor_190 = [tantos[i] for i in range(len(alturas)) if alturas[i] < 1.90]
entre_190_205 = [tantos[i] for i in range(len(alturas)) if 1.90 <= alturas[i] <= 2.05]
mayor_205 = [tantos[i] for i in range(len(alturas)) if alturas[i] > 2.05]

promedio_menor_190 = statistics.mean(menor_190) if menor_190 else 0
promedio_entre_190_205 = statistics.mean(entre_190_205) if entre_190_205 else 0
promedio_mayor_205 = statistics.mean(mayor_205) if mayor_205 else 0

# b) Tres jugadores con más tantos
indices_top = sorted(range(len(tantos)), key=lambda i: tantos[i], reverse=True)[:3]
top_jugadores = [(apellidos[i], tantos[i]) for i in indices_top]

# c) Jugador más representativo de la talla
talla_media = statistics.mean(alturas)
indice_representativo = min(range(len(alturas)), key=lambda i: abs(alturas[i] - talla_media))
jugador_representativo = (apellidos[indice_representativo], alturas[indice_representativo])

# d) Escribir archivo
with open("informeEquipo.txt", "w") as archivo:
    archivo.write(f"Promedios por rango de altura:\n")
    archivo.write(f"Menor a 1.90m: {promedio_menor_190}\n")
    archivo.write(f"Entre 1.90m y 2.05m: {promedio_entre_190_205}\n")
    archivo.write(f"Mayor a 2.05m: {promedio_mayor_205}\n")
    archivo.write(f"\nTop 3 jugadores con más tantos:\n")
    for apellido, tanto in top_jugadores:
        archivo.write(f"{apellido}: {tanto} tantos\n")
    archivo.write(f"\nJugador representativo de la talla:\n")
    archivo.write(f"{jugador_representativo[0]} con altura {jugador_representativo[1]}\n")

# Ejercicio 2: Función que devuelve iniciales
def iniciales(frase):
    palabras = frase.split()
    resultado = ""
    for palabra in palabras:
        resultado += palabra[0].upper()
    return resultado

# Ejemplo de iniciales
print(iniciales("Hola Mundo"))  # Salida: HM

# Ejercicio 3: Determinar ganador entre dos jugadores
def determinar_ganador(lista1, lista2):
    total1 = sum(lista1)
    total2 = sum(lista2)
    if total1 > total2:
        return "Jugador 1 gana"
    elif total1 < total2:
        return "Jugador 2 gana"
    else:
        return "Empate"

# Ejemplo de ganador
print(determinar_ganador([5, 10, 15], [10, 10, 5]))  # Salida: Empate

# Ejercicio 4: Palabra más repetida en un archivo
def palabra_mas_repetida(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        texto = archivo.read().split()
    palabras_unicas = list(set(texto))
    max_repeticiones = 0
    palabra_mas_repetida = ""
    for palabra in palabras_unicas:
        repeticiones = texto.count(palabra)
        if repeticiones > max_repeticiones:
            max_repeticiones = repeticiones
            palabra_mas_repetida = palabra
    return palabra_mas_repetida, max_repeticiones

# Crear archivo de ejemplo y probar
with open("texto.txt", "w") as f:
    f.write("Hola mundo mundo hola")

print(palabra_mas_repetida("texto.txt"))  # Salida: ('mundo', 2)

# Ejercicio 5: Palabras que no cambian de lugar
def palabras_ordenadas(lista):
    ordenadas = sorted(lista)
    resultado = []
    for i in range(len(lista)):
        if lista[i] == ordenadas[i]:
            resultado.append(lista[i])
    return resultado

# Ejemplo de palabras ordenadas
print(palabras_ordenadas(["apple", "banana", "cherry", "banana"]))  # Salida: ['apple', 'banana']
