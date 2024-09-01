
flagSells = input("Ingresá \"NO\" si queres dejar de comprar: ")
countEntries = 0

while flagSells != "NO":
    print("Elija entre las siguientes opciones SOLO poniendo el número:")

    entryType = int(input("¿Cuál quieres?\n1.Campo - 2.Campo VIP - 3.Platea\n"))
    while entryType < 1 or entryType > 3:
        entryType = int(input("Ingrese un número correcto:\n1.Campo - 2.Campo VIP - 3.Platea\n"))
    
    entryAmount = int(input("¿Cuántas quieres? Podes elegir entre 0 a 4 entradas: "))
    while entryAmount < 0 or entryAmount > 4:
        entryAmount = int(input("Ingrese un número correcto.\nPodes elegir entre 0 a 4 entradas: "))

    paymentMethod = int(input("¿Cuál método de pago quieres?\n1.Efectivo\t2.Tarjeta de Débito\t3.Tarjeta de Crédito\n"))
    while paymentMethod < 1 or paymentMethod > 3:
        paymentMethod = int(input("Ingrese un número correcto:\n1.Efectivo\t2.Tarjeta de Débito\t3.Tarjeta de Crédito\n"))

    clientType = int(input("¿Qué tipo de cliente eres?\n1.General\t2.Jubilado\t3.Estudiante\n"))
    while clientType < 1 or clientType > 3:
        clientType = int(input("Ingrese un número correcto:\n1.General\t2.Jubilado\t3.Estudiante\n"))

    flagSells = input("Ingresá \"NO\" si queres dejar de comprar: ")