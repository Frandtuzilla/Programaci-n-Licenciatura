def ident_izq(texto, n):
    """Indenta el texto a la izquierda en n espacios."""
    if len(texto) > n:
        return texto[:n]
    return texto + ' ' * (n - len(texto))

def ident_der(texto, n):
    """Indenta el texto a la derecha en n espacios."""
    if len(texto) > n:
        return texto[:n]
    return ' ' * (n - len(texto)) + texto

def ident_cen(texto, n):
    """Centra el texto en n espacios."""
    if len(texto) > n:
        inicio = (len(texto) - n) // 2
        return texto[inicio:inicio+n]
    espacios_izq = (n - len(texto)) // 2
    espacios_der = n - len(texto) - espacios_izq
    return ' ' * espacios_izq + texto + ' ' * espacios_der

if __name__ == "__main__":
    # Ejemplos de uso
    print(ident_izq('12345', 10))  # '12345     '
    print(ident_der('12345', 10))  # '     12345'
    print(ident_cen('12345', 10))  # '  12345   '
    print(ident_izq('1234567891011', 10))  # '1234567891'
    print(ident_der('1234567891011', 10))  # '1234567891'
    print(ident_cen('1234567891011', 10))  # '4567891011'
