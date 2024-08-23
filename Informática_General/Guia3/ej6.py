caracter = input("Ingrese un carácter: ")

# Verificar si es una letra mayúscula
if 'A' <= caracter <= 'Z' or caracter == 'Ñ':
    print("Es una letra mayúscula")

# Verificar si es una letra minúscula
elif 'a' <= caracter <= 'z' or caracter == 'ñ':
    print("Es una letra minúscula")

# Verificar si es una vocal
if caracter == 'a'or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == ' u' or caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U':
    print("Es una letra vocal")

# Verificar si es un dígito
if '0' <= caracter <= '9':
    print("Es un dígito")
    
    # Verificar si es par o impar
    if int(caracter) % 2 == 0:
        print("Es un dígito par")
    else:
        print("Es un dígito impar")
