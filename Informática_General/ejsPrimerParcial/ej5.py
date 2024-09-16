# Pedir al usuario que ingrese la contraseña
contraseña = input("Ingrese contraseña: ")

# Inicializamos variables para las validaciones
tieneMayuscula = False
tieneMinuscula = False
tieneNumero = False
longitudCorrecta = len(contraseña) >= 10
soloLetrasYNumeros = True
noHayDosNumerosSeguidos = True

i = 0

while i < len(contraseña):
    char = contraseña[i]

    if 'A' <= char <= 'Z':
        tieneMayuscula = True

    elif 'a' <= char <= 'z':
        tieneMinuscula = True

    elif '0' <= char <= '9':
        tieneNumero = True

        if i > 0 and '0' <= contraseña[i-1] <= '9':
            noHayDosNumerosSeguidos = False

    else:
        soloLetrasYNumeros = False

    i += 1

if longitudCorrecta and tieneMayuscula and tieneMinuscula and tieneNumero and soloLetrasYNumeros and noHayDosNumerosSeguidos:
    print("Contraseña válida")
else:
    print("Contraseña inválida")
