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
updated_list = avances(novedades, historial_carrera)
print("Historial Carrera:", updated_list)



def top3(historial_carrera):
    distancias = {}  # Crear diccionario para almacenar la distancia de cada auto
    
    # Iterar a través del historial_carrera para obtener autos y distancias
    for i in range(0, len(historial_carrera), 2):
        auto = historial_carrera[i]
        distancia = int(historial_carrera[i + 1])
        distancias[auto] = distancia
    
    # Ordenar los autos por distancia (de mayor a menor)
    autos_ordenados = sorted(distancias.items(), key=lambda x: x[1], reverse=True)
    
    # Manejar el top 3 considerando empates
    top_valores = sorted(set(distancias.values()), reverse=True)[:3]
    
    podio = []
    with open("top3.txt", "w") as archivo:
        for auto, distancia in autos_ordenados:
            if distancia in top_valores:
                archivo.write(f"{auto}: {distancia} km\n")
                podio.append(auto)
    
    return podio

# Pruebo si funciona
podio = top3(updated_list)
