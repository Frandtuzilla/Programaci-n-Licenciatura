repetirProceso = True

while repetirProceso:
    numeroDado = int(input("Ingrese un número natural mayor a 0: "))
    if numeroDado > 0:
        repetirProceso = False

i = 1
while i < numeroDado:
    aux = str(i)
    j = 0
    flag = True
    
    while j < len(aux) and flag:
        if aux[j] == '0':
            print(f"{aux}")
            flag = False
        j += 1

    i += 1  
