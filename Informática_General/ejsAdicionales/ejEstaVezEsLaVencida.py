from random import randint

repiteProceso = True

while repiteProceso:
    numNat = int(input("Ingrese un número natural: "))
    if numNat > 0:
        repiteProceso = False

i = 0
cantidadVeintenas = 0
while i < numNat:
    mes = randint(1, 12)
    dia = 0
    cantMedialunas = 0
    if mes == 2:
        dia = randint(1, 29)
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dia = randint(1, 30)
    else:
        dia = randint(1,31)
    if mes < 10:
        print(f"La fecha n° {i+1} es {dia}/0{mes}.")
    else:
        print(f"La fecha n° {i+1} es {dia}/{mes}.")
    cantMedialunas = randint(0,6000)
    print(f"Y la cantidad de medialunas es de {cantMedialunas}.\n")
    if cantMedialunas%20 == 0:
        cantidadVeintenas += 1
    i += 1

print(f"La cantidad de porcentaje de de veintenas es de {(cantidadVeintenas/numNat)*100}%.")

# Comentario: Las fechas pueden repetirse en este caso, pero no verificar que no suceda sería un lío