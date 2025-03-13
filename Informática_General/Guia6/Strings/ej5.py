def strip(S):
    # Eliminar espacios al principio
    inicio = 0
    while inicio < len(S) and S[inicio] == ' ':
        inicio += 1
    
    # Eliminar espacios al final
    fin = len(S) - 1
    while fin > inicio and S[fin] == ' ':
        fin -= 1
    
    # Retornar la subcadena sin espacios al principio ni al final
    return S[inicio:fin+1]

if __name__ == "__main__":
    # Ejemplo de uso
    print(strip('  Hola che  '))  # Debería imprimir: 'Hola che'
