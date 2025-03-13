novedades = [ 1, "20", 2, "25", 3, "20", 3, "A", 1, "P", 4, "18", 2, "A", 5, "50", 5, "25", 6, "15", 7, "20", 8, "75"]

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
                lista_aux.pop(index)  # Remover su estado (que se corrío un lugar por el pop anterior)
            elif estado != 'P':
                # Si el estado no es 'P', sumamos valores
                lista_aux[index + 1] = str(int(lista_aux[index + 1]) + int(estado))
        
        i += 2  # Avanzo al siguiente par

    historial_carrera.extend(lista_aux)  # Copio los nuevos valores

    return historial_carrera



# Pruebo si funciona
nueva_lista = avances(novedades, historial_carrera)
print("Historial Carrera:", nueva_lista)



def top3(historial_carrera):
    distancias = {}  # Creo diccionario para almacenar la distancia de cada auto
    
    # Itero a través del historial_carrera para guardar autos y distancias en el diccionario
    for i in range(0, len(historial_carrera), 2):
        auto = historial_carrera[i]
        distancia = int(historial_carrera[i + 1])
        distancias[auto] = distancia
    
    # Ordeno los autos por distancia (de mayor a menor) / Se basa en el segundo elemento (x[1], que es la distancia) / El reverse es porque sino ordena de menor a mayor
    autos_ordenados = sorted(distancias.items(), key=lambda x: x[1], reverse=True) 
    
    # Le pido los valores de los diccionarios (km), los ordeno de mayor a menor, y me quedo con los 3 primeros.
    top_valores = sorted(set(distancias.values()), reverse=True)[:3]  
    
    with open("top3.txt", "w") as archivo: # Si existe el archivo, se sobreescribe. Sino, se crea.
        for auto, distancia in autos_ordenados: # Itero a través de los autos ordenados
            if distancia in top_valores: # Si la distancia está en el top 3, agregar al podio
                archivo.write(f"{auto}: {distancia} km\n")
    
    return

# Pruebo si funciona
podio = top3(nueva_lista)
