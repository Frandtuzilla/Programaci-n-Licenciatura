import random

dinero = 0
repetirProceso = True

while repetirProceso:
    apuesta = int(input("¿Qué cantidad quieres apostar (€)? "))
    
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    num3 = random.randint(1, 5)

    print(f"Tirada: | {num1} | {num2} | {num3} |")
    print("-----------------------------")
    
    if num1 != num2 and num1 != num3 and num2 != num3:
        print(f"Los tres números son distintos. Has perdido todo tu dinero.")
        dinero = 0
        repetirProceso = False
    elif num1 == num2 == num3:
        dinero += apuesta * 5
        print(f"¡Has multiplicado por cinco tu dinero!")
        print(f"¡Enhorabuena! Has ganado {apuesta * 5} €. Ahora tienes {dinero} €.")
    else:
        dinero += apuesta * 2
        print(f"Dos de los tres números son iguales. Has duplicado tu dinero.")
        print(f"¡Enhorabuena! Has ganado {apuesta * 2} €. Ahora tienes {dinero} €.")
    
    if repetirProceso:
        respuesta = input("Pulsa n para terminar, otra tecla para volver a jugar: ")
        if respuesta == 'n':
            repetirProceso = False

print(f"Enhorabuena, has ganado {dinero} €.")
