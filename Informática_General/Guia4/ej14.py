import random

puntajeJugador1 = 0
puntajeJugador2 = 0
repetirProceso = True

while repetirProceso:

    tiradaJugador1 = random.randint(1, 6)
    puntajeJugador1 += tiradaJugador1
    print(f"Primer jugador: Tirada actual: {tiradaJugador1}  Total acumulado: {puntajeJugador1}")

    tiradaJugador2 = random.randint(1, 6)
    puntajeJugador2 += tiradaJugador2
    print(f"Segundo jugador: Tirada actual: {tiradaJugador2}  Total acumulado: {puntajeJugador2}")

    respuesta = input("Para generar un nuevo número pulsa S o s, otra tecla para terminar: ")
    if respuesta != 's':
        repetirProceso = False

print("**************************************")
if puntajeJugador1 > puntajeJugador2:
    print(f"Vencedor: Primer jugador. Resultado final: Jugador1: {puntajeJugador1} - Jugador2: {puntajeJugador2}")
elif puntajeJugador2 > puntajeJugador1:
    print(f"Vencedor: Segundo jugador. Resultado final: Jugador1: {puntajeJugador1} - Jugador2: {puntajeJugador2}")
else:
    print(f"Primer jugador y segundo jugador han empatado a {puntajeJugador1} puntos.")
print("**************************************")
