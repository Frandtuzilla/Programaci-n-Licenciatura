import random

repetirProceso = True

while repetirProceso:

    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    num3 = random.randint(1, 5)

    print(f"Tirada: | {num1} | {num2} | {num3} |")
    
    if num1 == num2 == num3:
        print("Los tres números son iguales")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("Dos de los tres números son iguales")
    else:
        print("Los tres números son distintos")
    
    respuesta = input("Pulsa n para terminar, otra tecla para volver a jugar: ")
    if respuesta == 'n':
        print("Programa terminado")
        repetirProceso = False
