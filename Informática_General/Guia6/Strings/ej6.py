from ej1 import es_letra, es_mayuscula
from ej2 import minuscula
from ej4 import split
from ej5 import strip

def camel_case(S):
    # Eliminar espacios al principio y al final
    S = strip(S)
    
    # Dividir la cadena en palabras
    palabras = split(S, ' ')
    
    # Procesar cada palabra
    resultado = minuscula(palabras[0])
    for palabra in palabras[1:]:
        palabra = minuscula(palabra)
        if len(palabra) > 0:
            primera_letra = palabra[0]
            if es_letra(primera_letra):
                palabra = chr(ord(primera_letra) - 32) + palabra[1:]
        resultado += palabra
    
    return resultado

# Agregar el bloque if __name__ == "__main__":
if __name__ == "__main__":
    # Ejemplo de uso
    print('vamos al mar')

    print(camel_case('vamos al mar'))  # Debería imprimir: vamosAlMar
