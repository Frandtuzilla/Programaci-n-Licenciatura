repitoProceso = True
frase = ""
lenFrase = 0

while repitoProceso:
    frase = input("Ingrese una frase de al menos 10 caracteres que solo deben ser mayúsculas y minúsculas: ")
    
    lenFrase = len(frase)
    if lenFrase >= 10 and frase.isalpha():
        repitoProceso = False
    else:
        print("Ingrese una frase de al menos 10 caracteres que solo deben ser mayúsculas y minúsculas: ")

repitoProceso = True
numeroEntero = 0

while repitoProceso:
    numeroEntero = int(input(f"Ingrese un número mayor que 2 y como máximo la tercera parte del largo de la frase ingresada (máx {lenFrase//3}): "))
    if numeroEntero > 2 and numeroEntero <= lenFrase // 3:
        repitoProceso = False
    else:
        print(f"Ingrese un número mayor que 2 y como máximo la tercera parte del largo de la frase ingresada (máx {lenFrase//3}): ")

menor = None
mayor = None

i = 0
print("")

while i <= lenFrase - numeroEntero:
    subcadena = frase[i:i + numeroEntero]
    
    if 'A' <= subcadena[0] <= 'Z':
        print(f"{subcadena}")
        if menor is None or subcadena < menor:
            menor = subcadena
        if mayor is None or subcadena > mayor:
            mayor = subcadena

    i += 1

print("")

if menor and mayor:
    print(f"La menor es: {menor} y la mayor es: {mayor}\n")
else:
    print("No se encontraron subcadenas que comiencen con mayúscula.\n")