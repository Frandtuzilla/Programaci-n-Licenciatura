numero = float(input("Ingrese un número: "))
mitadNumero = numero / 2

# Verificar si el número es entero
if numero != int(numero):
    print("No ingresó un número entero.")
else:
    # Convertir a entero para continuar la verificación
    numero = int(numero)
    mitadNumeroEntero = int(mitadNumero)

    # Verificar si la mitad es impar y el doble de un número impar
    if (mitadNumero == mitadNumeroEntero) and (mitadNumeroEntero % 2 == 1):
        print(f"{numero} es el doble de {mitadNumeroEntero}, que es impar.")
    else:
        print("No cumple ninguna de las consignas.")
