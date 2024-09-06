from random import randint

valor = int(input("Ingrese un número natural (mayor que 0): "))

while valor <= 0:
    valor = int(input("ERROR: -> Ingrese un número natural (mayor que 0): "))

i = 0 # indice de creación de números
menorNum = 999999 # mi menor número es el más grande de los posibles, y de allí voy bajando 
menorSuma = 9*6 # y el valor máximo acá es de 9 * 6 = 51
print("Los números son:\n")

while i < valor:
    auxNum = str(randint(100000, 999999))   # creo número aleatoreo
    print(f"El número {i+1} es: {auxNum}")  # imprimo el número que tocó
    j = 0  
    auxSuma = 0  
    while j < len(auxNum): # Dentro de este ciclo, sumo las cifras del número dado
        auxSuma += int(auxNum[j])
        j += 1
    print(f"La suma de sus crifas es: {auxSuma}\n")  # imprimo la suma
    if auxSuma < menorSuma: # si la suma de las cifras es menor que el menor hasta ahora...
        menorSuma = auxSuma
        menorNum = int(auxNum)   # lo reemplazo en la variable del menor número
    i += 1

print(f"El número cuya suma de cifras es la más baja es {menorNum}, pues es {menorSuma}.")