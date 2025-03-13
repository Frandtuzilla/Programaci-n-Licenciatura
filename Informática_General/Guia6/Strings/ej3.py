def buscar_subcadena(S, sub):
    """
    Busca una subcadena dentro de una cadena principal.
    
    Args:
    S (str): La cadena principal en la que buscar.
    sub (str): La subcadena a buscar.
    
    Returns:
    bool: True si la subcadena se encuentra en la cadena principal, False en caso contrario.
    """
    return sub in S

if __name__ == "__main__":
    # Ejemplos de uso
    print(buscar_subcadena('Yo tomo sólo Pepsi', 'Coca-Cola'))  # Debe imprimir False
    print(buscar_subcadena('Yo tomo sólo Pepsi', 'Pepsi'))      # Debe imprimir True
