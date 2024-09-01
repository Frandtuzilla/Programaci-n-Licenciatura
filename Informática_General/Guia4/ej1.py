amountNumbers = int(float(input("¿Cuántos valores vas a introducir? ")))

if(amountNumbers < 0):
    print("imposible!")
else:
    i = 0
    negativeNumbers = 0
    while i < amountNumbers:
        selectedNumber = int(float(input(f"Escribe el número {i+1}: ")))
        if(selectedNumber < 0):
            negativeNumbers += 1
        i += 1
    print(f"Has escrito {negativeNumbers} números negativos.")