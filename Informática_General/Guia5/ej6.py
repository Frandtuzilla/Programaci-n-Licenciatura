def mostrar_cifras_inverso(numero):
    # Convertir el número a cadena para facilitar la iteración
    numero_str = str(abs(numero))
    
    # Iterar sobre la cadena en orden inverso
    for digito in reversed(numero_str):
        print(digito)

# Ejemplo de uso
numero_ejemplo = int(input("Ingrese un número: "))
mostrar_cifras_inverso(numero_ejemplo)
