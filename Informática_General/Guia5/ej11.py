def mcd(a, b):
    # Esta función calcula el Máximo Común Divisor (MCD) de dos números
    # Usa el método de resta sucesiva
    while a != b:
        if a > b:
            a = a - b  # Si a es mayor, le restamos b
        else:
            b = b - a  # Si b es mayor, le restamos a
    # Cuando a y b son iguales, hemos encontrado el MCD
    return a

def mcm(a, b):
    # Esta función calcula el Mínimo Común Múltiplo (MCM) de dos números
    # Usa la fórmula: MCM(a,b) = (a * b) / MCD(a,b)
    mcd_valor = mcd(a, b)  # Calculamos el MCD primero
    return (a * b) // mcd_valor, mcd_valor  # Devolvemos tanto el MCM como el MCD

# Solicitar entrada del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calculamos el MCM y el MCD usando nuestra función
resultado_mcm, resultado_mcd = mcm(num1, num2)

# Mostramos los resultados
print(f"El MCM de {num1} y {num2} es: {resultado_mcm}")
print(f"El MCD de {num1} y {num2} es: {resultado_mcd}")
