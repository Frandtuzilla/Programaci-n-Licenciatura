novedades = [1, "30", 2, "A", 3, "50", 4, "23", 3, "P", 5, "A", 1, "20", 2, "10", 3, "P", 4, "A", 5, "30"]

historial_carrera = []

def avances(novedades, historial_carrera):

    lista_aux = []  # Lista auxiliar para guardar los valores
    i = 0
    
    while i < len(novedades) - 1:  # Recorro la lista sin exceder el índice
        auto = novedades[i]         # Guardo el número de auto
        estado = novedades[i + 1]   # Guardo el estado asociado al auto
        
        if auto not in lista_aux and estado not in ['A', 'P']:   # Si el auto no está en lista_aux y su estado no es 'A' ni 'P', lo agrego
            lista_aux.append(auto)
            lista_aux.append(estado)
        elif auto in lista_aux:
            # Si el auto ya está en lista_aux...
            index = lista_aux.index(auto)
            if estado == 'A':
                # Si el estado es 'A', eliminamos el auto de la lista
                lista_aux.pop(index)  # Remover el auto
                lista_aux.pop(index)  # Remover su estado
            elif estado != 'P':
                # Si el estado no es 'P' y el auto no ha sido eliminado antes, sumamos valores
                if lista_aux[index + 1] != 'A':  
                    lista_aux[index + 1] = str(int(lista_aux[index + 1]) + int(estado))

        i += 2  # Avanzo al siguiente par

    # historial_carrera.clear()  # Si quisiera borrar el historial anterior
    historial_carrera.extend(lista_aux)  # Copio los nuevos valores

    return historial_carrera

# Ejecutar función
updated_list = avances(novedades, historial_carrera)
print("Historial Carrera:", updated_list)
