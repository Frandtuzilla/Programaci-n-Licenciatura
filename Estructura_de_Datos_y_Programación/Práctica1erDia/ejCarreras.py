novedades = [1, "20", 2, "25", 3, "20", 3, "Hola", 3, "A", 1, "P", 4, "18", 2, "A", 5, "50", 5, "25", 6, "15", 7, "20", 8, "75"]

historial_carrera = []

def avances(novedades: list, historial_carrera: list):
    lista_abandono = []  # Lista para guardar los autos que ya abandonaron
    i = 0
    
    while i < len(novedades) - 1:          # Recorro la lista sin exceder el índice
        auto = novedades[i]                # Guardo el número de auto
        estado = novedades[i + 1]          # Guardo el estado asociado al auto
        
        if estado == "A":                  # Si el estado es 'A' ...
            lista_abandono.append(auto)    # ... agrego el auto a la lista negra

        if auto not in historial_carrera and auto not in lista_abandono and estado != 'P':  
            # Si el auto no está en historial_carrera, tampoco en la lista negra y su estado no es 'P', lo agrego
            historial_carrera.append(auto)
            historial_carrera.append(estado)
        elif auto in historial_carrera:  
            index = historial_carrera.index(auto)
            if estado == 'A':  
                # Si el estado es 'A', eliminamos el auto y su estado
                historial_carrera.pop(index)
                historial_carrera.pop(index)
            elif estado != 'P':  
                # Si el estado no es 'P', intentamos sumar valores
                try:
                    historial_carrera[index + 1] = str(int(historial_carrera[index + 1]) + int(estado))
                except ValueError:
                    print(f"Error: No se pudo convertir el estado '{estado}' a un número para el auto {auto}")

        i += 2  # Avanzo al siguiente par

    return historial_carrera

resultado = avances(novedades, historial_carrera)
print("Historial Carrera:", resultado)


def top3(historial_carrera):
    distancias = {}  # Creo diccionario para almacenar la distancia de cada auto
    
    # Itero a través del historial_carrera para guardar autos y distancias en el diccionario
    for i in range(0, len(historial_carrera), 2):
        auto = historial_carrera[i]
        distancia = int(historial_carrera[i + 1])
        distancias[auto] = distancia
    
    # Ordeno los autos por distancia (de mayor a menor) / Se basa en el segundo elemento (x[1], que es la distancia) / El reverse es porque sino ordena de menor a mayor
    autos_ordenados = sorted(distancias.items(), key=lambda x: x[1], reverse=True) 
    
    # Le pido los valores de los diccionarios (km), (set) eliminano los valores duplicados, los ordeno de mayor a menor, y me quedo con los 3 primeros.
    top_valores = sorted(set(distancias.values()), reverse=True)[:3]  
    
    with open("top3.txt", "w") as archivo: # Si existe el archivo, se sobreescribe. Sino, se crea.
        for auto, distancia in autos_ordenados: # Itero a través de los autos ordenados
            if distancia in top_valores: # Si la distancia está en el top 3, agregar al podio
                archivo.write(f"{auto}: {distancia} km\n")
    

top3(resultado)
