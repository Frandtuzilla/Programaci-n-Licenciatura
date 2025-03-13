def split(S, c):
    resultado = ['']
    
    for caracter in S:
        if caracter == c:
            resultado += ['']
        else:
            resultado[-1] += caracter
    
    return resultado

if __name__ == "__main__":
    # Ejemplos de uso
    print(split('Es un día soleado', ' '))
    print(split('Mi primo se llama aaron', 'a'))
