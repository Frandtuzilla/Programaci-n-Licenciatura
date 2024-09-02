auxNum = 0
desicion = 'S'
count = 0

while desicion == 'S':
    auxNum = int(float(input("Escribe un múltiplo de 5: ")))
    
    while auxNum%5 != 0:
        auxNum = int(float(input(f"{auxNum} no es múltiplo de 5. Inténtalo de nuevo: ")))
        
    count += 1
    desicion = input("¿Quieres escribir otro número múltiplo de 5? (S/N) ")

print(f"Has escrito {count} número{ 's' if count != 1 else ''} múltiplo de 5.")
print("Programa terminado")