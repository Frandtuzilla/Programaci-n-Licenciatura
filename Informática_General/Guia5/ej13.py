def dectobin(decimal):
    # Si el número decimal es 0, retornamos "0" directamente
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        # Obtenemos el resto de la división por 2 (0 o 1)
        # y lo añadimos al inicio de la cadena binaria
        binario = str(decimal % 2) + binario
        # Dividimos el decimal por 2 (división entera)
        decimal //= 2
    
    return binario

# Versión original comentada
# def bintodec(binario):
#     decimal = 0
#     # Recorremos la cadena binaria de derecha a izquierda
#     for i, digito in enumerate(reversed(binario)):
#         # Si el dígito es "1", sumamos 2 elevado a la posición
#         if digito == "1":
#             decimal += 2 ** i
#     
#     return decimal

# Nueva versión sin usar enumerate
def bintodec(binario):
    decimal = 0
    potencia = 0
    # Recorremos la cadena binaria de derecha a izquierda
    for digito in binario[::-1]:
        # Si el dígito es "1", sumamos 2 elevado a la potencia actual
        if digito == "1":
            decimal += 2 ** potencia
        potencia += 1
    
    return decimal

# Ejemplos de uso
print(dectobin(13))  # Debería imprimir: 1101
print(bintodec("1101"))  # Debería imprimir: 13
