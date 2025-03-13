def find(S, sub):
    n = len(S)
    m = len(sub)
    
    for i in range(n - m + 1):
        if S[i:i+m] == sub:
            return i
    
    return -1

# Ejemplos de uso
print(find('Hola, qué haces por acá', 'qué'))  # Debería imprimir 6
print(find('Hola, qué haces por acá', 'Hola'))  # Debería imprimir 0
print(find('Hola, qué haces por acá', 'como'))  # Debería imprimir -1