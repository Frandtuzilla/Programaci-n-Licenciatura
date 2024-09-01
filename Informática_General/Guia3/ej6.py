caracter = input("Ingrese un carácter: ")

if 'A' <= caracter <= 'Z' or caracter == 'Ñ':
    print("Es una letra mayúscula")

elif 'a' <= caracter <= 'z' or caracter == 'ñ':
    print("Es una letra minúscula")

if caracter == 'a'or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == ' u' or caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U':
    print("Es una letra vocal")

if '0' <= caracter <= '9':
    print("Es un dígito")
    
    if int(caracter) % 2 == 0:
        print("Es un dígito par")
    else:
        print("Es un dígito impar")
