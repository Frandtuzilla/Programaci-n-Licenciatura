import csv  #Importa el módulo csv para manejar archivos CSV

def mi_split(F, c):
    lista = []
    sub_cadena = ""
    
    for elemento in F:
        if elemento == c:  #Si encuentra el carácter separador
            lista.append(sub_cadena)  #Agrega la subcadena acumulada
            sub_cadena = ""  #Reinicia la subcadena para el siguiente fragmento
        else:
            sub_cadena += elemento  #Construye la subcadena
    
    lista.append(sub_cadena)  #Agrega la última subcadena
    return lista


def mi_strip(s):
    inicio = 0
    fin = len(s) - 1
    
    while inicio <= fin and s[inicio] == " ":  #Omite espacios iniciales
        inicio += 1
    
    while fin >= inicio and (s[fin] == " " or s[fin] == "\n"):  #Omite espacios finales y saltos de línea
        fin -= 1
    
    return s[inicio:fin+1]  #Retorna la subcadena sin espacios extremos


def mi_minuscula(texto):
    resultado = ""
    for letra in texto:
        #Si la letra está en mayúscula (entre 'A' y 'Z'), la convertimos a minúscula
        if 'A' <= letra <= 'Z':
            resultado += chr(ord(letra) + (ord('a') - ord('A')))
        else:
            #Si la letra ya es minúscula o no es una letra, la agregamos tal cual
            resultado += letra
    return resultado

def leer_naciones(archivo):  
    continentes = []  #Lista para almacenar los continentes
    paises = []       #Lista para almacenar los países
    atletas = []      #Lista para almacenar los atletas

    try:
        with open(archivo, 'r', encoding='utf-8') as archivo:
            archivo.readline()  #Saltar la primera línea (encabezado)
            lector = csv.reader(archivo)
            for fila in lector:
                continentes.append(mi_strip(fila[0]))  #Agrega el continente a la lista
                paises.append(mi_strip(fila[1]))       #Agrega el país a la lista
                atletas.append(mi_strip(fila[2]))      #Agrega el atleta a la lista
    except FileNotFoundError:  #Captura el error si el archivo no se encuentra
        print(f"El archivo '{archivo}' no existe.")
    except Exception as e:  #Captura cualquier otro error que pueda ocurrir
        print(f"Error al leer el archivo: {e}")

    return continentes, paises, atletas  #Devuelve las listas


def leer_ganadores(ruta_archivo):
    #Inicializar listas
    nombres = []
    paises_ganadores = []  #Cambiado de "naciones" a "paises_ganadores"
    medallas = []

    try:
        #Leer el archivo línea por línea
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = mi_strip(linea)  #Usar mi_strip en lugar de strip
                #Identificar la información en función de la estructura de la línea
                if "Nombre del Atleta:" in linea:
                    nombre = mi_split(linea, ":")[1]
                    nombres.append(mi_strip(nombre))
                elif "Pais:" in linea:
                    pais = mi_split(linea, ":")[1]
                    paises_ganadores.append(mi_strip(pais))  #Cambiado de "naciones" a "paises_ganadores"
                elif "Medallas:" in linea:
                    medallas_str = mi_split(linea, ":")[1]
                    medallas_split_str = mi_split(mi_strip(medallas_str), ',')

                    #Crear una lista vacía para las medallas
                    medallas_split = []
                    for medalla in medallas_split_str:
                        #Convertir cada valor a entero y agregarlo a la lista de medallas
                        medallas_split.append(int(medalla))

                    #Agregar la lista de medallas a la lista principal
                    medallas.append(medallas_split)
    except FileNotFoundError:  
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:  
        print(f"Error al leer el archivo: {e}")
    return nombres, paises_ganadores, medallas  #Cambiado de "naciones" a "paises_ganadores"


def filtrar_continente(continentes, paises):
    #Normaliza el nombre del continente ingresado para prevenir errores 
    continente = mi_minuscula(mi_strip(input("Continente: ")))

    #Creo una lista de países únicos pertenecientes al continente dado
    paises_filtrados = []
    
    #Itero sobre la lista de continentes y paises
    for i in range(len(continentes)):
        if mi_minuscula(continentes[i]) == continente and paises[i] not in paises_filtrados:
            paises_filtrados.append(paises[i])

    #Verifico si se encontraron países o no
    cadena_paises = ""

    if paises_filtrados:
        for i in range(len(paises_filtrados)):
            if i!=len(paises_filtrados)-1:
                cadena_paises += paises_filtrados[i] + ", "
            else:
                cadena_paises += paises_filtrados[i] + "."
        print(cadena_paises)
    else:
        print("El continente ingresado no existe.")

    return paises_filtrados

#Funcion para mostras la cantidad de medallas que tiene los paises del continente ingresado anteriormente
def mostrar_medallas(paises_filtrados, paises_ganadores, medallas):
    #Verifica si el continente existe
    if not paises_filtrados:
        print("No se encontraron países para el continente especificado.")
    
    else:
        
        #Recorre la lista de los paises del continente ingresado anteriormente
        for i in paises_filtrados:
            
            total_medallas = 0
            
            #Recorre la lista de los paises de todos los participantes
            for a in range(len(paises_ganadores)):
                
                #Verifica si el pais filtrado es igual al pais del participante de la lista de paises_ganadores
                if i == paises_ganadores[a]:
                    
                   #Suma las medallas del participante a la variable total_medallas
                   total_medallas += (int(medallas[a][0]) + int(medallas[a][1]) + int(medallas[a][2]))
            
            #Imprime el pais con las medallas totales    
            print(str(i) + ": " + str(total_medallas))


#Función para transformar los datos en un medallero por país
def transformar_datos_a_medallero(paises_ganadores, medallas):
    #Crear una lista para acumular las medallas por país
    medallero = []
    
    for i in range(len(paises_ganadores)):  #Recore cada pais en la lista de ganadores 
        pais = paises_ganadores[i]
        oro, plata, bronce = medallas[i]

        #Creamos una variable para verificar si el país fue encontrado
        encontrado = False
        
        for pais_medallas in medallero:
            if pais_medallas[0] == pais:
                #Si el país ya está en la lista, sumar las medallas
                pais_medallas[1] += oro
                pais_medallas[2] += plata
                pais_medallas[3] += bronce
                encontrado = True
        
        #Si el país no está en la lista todavía, se agrega
        if not encontrado:
            medallero.append([pais, oro, plata, bronce])
    
    return medallero


#Función para ordenar y mostrar el ranking de países
def ranking_olimpico(paises_ganadores, medallas):

    medallero = transformar_datos_a_medallero(paises_ganadores, medallas)
    
    n = len(medallero)
    #Ordena usando el método de burbujeo
    for i in range(n):
        for j in range(0, n - i - 1):
            #Compara los países por medallas siguiendo el orden de prioridad oro > plata > bronce
            if (medallero[j][1] < medallero[j + 1][1] or (medallero[j][1] == medallero[j + 1][1] and medallero[j][2] < medallero[j + 1][2]) or (medallero[j][1] == medallero[j + 1][1] and medallero[j][2] == medallero[j + 1][2] and medallero[j][3] < medallero[j + 1][3])):
                #Intercambia los países si están en el orden incorrecto
                medallero[j], medallero[j + 1] = medallero[j + 1], medallero[j]
    
    #Construye el formato de salida
    resultado = ""
    posicion = 1
    for pais_medallas in medallero:
        resultado += str(posicion) + ". " + pais_medallas[0] + ": Oro: " + str(pais_medallas[1]) + ", Plata: " + str(pais_medallas[2]) + ", Bronce: " + str(pais_medallas[3]) + "\n"   
        posicion += 1
    #Devuelvo el ranking
    print(resultado)

#Funcion para buscar un atleta con una determinada cantidad de medallas
def ingrese_cant_medallas(medallas, naciones, nombres):
    n = 1 # Declaro variable "n" con un valor aleatoreo fuera del while para poder utilizarla en mi funcion
    
    repito_proceso = True

    while repito_proceso:

        verifica_num = True
        n = input("Ingrese un numero de medallas mayor o igual a cero (Con dígitos): \n")
        
        if n == '':
            verifica_num = False
        else:
            for caracter in n:
                if caracter < "0" or caracter > "9":
                    verifica_num = False

        if verifica_num:
            repito_proceso = False

    atletas_encontrados = []  #Lista para almacenar los atletas que cumplen el criterio

    #Recorre la lista de medallas
    for i in range(len(medallas)):
        #Verifica si la suma de todas las medallas es igual a la cantidad ingresada (n)
        if int(n) == (int(medallas[i][0]) + int(medallas[i][1]) + int(medallas[i][2])):
            atletas_encontrados.append(nombres[i] + " (" + naciones[i] + ")")

    #Si hay atletas, crea el archivo TXT
    if atletas_encontrados:
        with open("atletas.txt", "w") as archivo:
            for atleta in atletas_encontrados:
                archivo.write(atleta + "\n")
        print("Archivo 'atletas.txt' creado con éxito.")
    else:
        print("No se encontraron atletas con la cantidad de medallas especificada.")


#EJEMPLOS DE USO PARA PROBAR LAS FUNCIONES

continentes, paises, atletas = leer_naciones('naciones_olimpicas.csv')

nombres, paises_ganadores, medallas = leer_ganadores('ganadores.txt')

if atletas and medallas:
    #########################################################

    paises_filtrados = filtrar_continente(continentes, paises)

    print("\nImprimo Medallas: \n")

    mostrar_medallas(paises_filtrados, paises_ganadores, medallas)

    ###########################################################

    print("\nImprimo Ranking Olímpico: \n")

    ranking_olimpico(paises_ganadores, medallas)

    ###########################################################

    print("\nImprimo Atletas por Cantidad de Medallas: \n")

    ingrese_cant_medallas(medallas, paises_ganadores, nombres)