def mcd(a, b):
    """Calcula el máximo común divisor de dos números."""
    while b:
        a, b = b, a % b
    return a

def son_coprimos(a, b):
    """Determina si dos números son coprimos."""
    return mcd(a, b) == 1

def main():
    while True:
        num1 = int(input("Ingrese el primer número (mayor que 1): "))
        num2 = int(input("Ingrese el segundo número (mayor que 1): "))
        
        if num1 > 1 and num2 > 1:
            if son_coprimos(num1, num2):
                print(f"{num1} y {num2} son coprimos.")
                break
            else:
                print(f"{num1} y {num2} no son coprimos. Intente nuevamente.")
        else:
            print("Ambos números deben ser mayores que 1. Intente nuevamente.")

if __name__ == "__main__":
    main()
