firstNum = input("Escribe un número entero: ")

secondNum = input(f"Escribe un número entero mayor que {firstNum}: ")

while secondNum <= firstNum:
    secondNum = input(f"{secondNum} no es mayor que {firstNum}. Vuelve a intentarlo: ")

print(f"\nLos números que has introducido son el {firstNum} y el {secondNum}.")
print("Programa finalizado")