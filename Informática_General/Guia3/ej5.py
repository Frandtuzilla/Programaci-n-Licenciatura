cantidad = int(input("Ingrese cantidad de euros: "))

if cantidad >= 500:
    billetes500 = cantidad // 500
    cantidad -= billetes500 * 500
    print(f"{billetes500} billete{'s' if billetes500 > 1 else ''} de 500 €")

if cantidad >= 200:
    billetes200 = cantidad // 200
    cantidad -= billetes200 * 200
    print(f"{billetes200} billete{'s' if billetes200 > 1 else ''} de 200 €")

if cantidad >= 100:
    billetes100 = cantidad // 100
    cantidad -= billetes100 * 100
    print(f"{billetes100} billete{'s' if billetes100 > 1 else ''} de 100 €")

if cantidad >= 50:
    billetes50 = cantidad // 50
    cantidad -= billetes50 * 50
    print(f"{billetes50} billete{'s' if billetes50 > 1 else ''} de 50 €")

if cantidad >= 20:
    billetes20 = cantidad // 20
    cantidad -= billetes20 * 20
    print(f"{billetes20} billete{'s' if billetes20 > 1 else ''} de 20 €")

if cantidad >= 10:
    billetes10 = cantidad // 10
    cantidad -= billetes10 * 10
    print(f"{billetes10} billete{'s' if billetes10 > 1 else ''} de 10 €")

if cantidad >= 5:
    billetes5 = cantidad // 5
    cantidad -= billetes5 * 5
    print(f"{billetes5} billete{'s' if billetes5 > 1 else ''} de 5 €")

if cantidad >= 2:
    monedas2 = cantidad // 2
    cantidad -= monedas2 * 2
    print(f"{monedas2} moneda{'s' if monedas2 > 1 else ''} de 2 €")

if cantidad >= 1:
    monedas1 = cantidad // 1
    cantidad -= monedas1 * 1
    print(f"{monedas1} moneda{'s' if monedas1 > 1 else ''} de 1 €")
