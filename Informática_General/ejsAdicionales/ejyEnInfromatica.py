repetirProceso = True

while repetirProceso:
    cadena = input("Ingrese su nombre, edad y número de documento, separados por comas: ")

    cumpleNombre = True
    i = 0
    while i < len(cadena) and cadena[i] != ',':
        if not ('A' <= cadena[i] <= 'Z' or 'a' <= cadena[i] <= 'z'):
            cumpleNombre = False
        i += 1

    nombre = cadena[0:i]

    if len(nombre) <= 2:
        cumpleNombre = False

    if cumpleNombre:
        i += 1
        cumpleEdad = True
        j = i
        while j < len(cadena) and cadena[j] != ',':
            if not ('0' <= cadena[j] <= '9'):
                cumpleEdad = False
            j += 1

        edad = cadena[i:j]
        
        if cumpleEdad:
            edad = int(edad)
            if not (10 <= edad <= 99):
                cumpleEdad = False

        if cumpleEdad:
            j += 1 
            cumpleDNI = True
            k = j
            while k < len(cadena):
                if not ('0' <= cadena[k] <= '9'):
                    cumpleDNI = False
                k += 1

            dni = cadena[j:k]

            if cumpleDNI and (7 <= len(dni) <= 8):
                repetirProceso = False

nombreMayusculas = ""
index = 0
while index < 3 and index < len(nombre):
    letra = nombre[index]
    if 'a' <= letra <= 'z':  
        nombreMayusculas += chr(ord(letra) - 32)
    else:
        nombreMayusculas += letra
    index += 1

contrasena = nombreMayusculas + str(edad) + dni[:4]

print(f"La contraseña es: {contrasena}")