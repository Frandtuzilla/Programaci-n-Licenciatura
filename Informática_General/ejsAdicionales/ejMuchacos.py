text = input("Ingresar una cadena de más de 2 caracteres: ")
while len(text) < 2:
    text = input("Error - Ingresar una cadena de más de 2 caracteres: ")

i = 0
flag = 1
textLength = len(text)

while flag and i < textLength - 1:
    if( text[i] > text[i+1] ):
        flag = 0
        print("La cadena NO esta ordenada según el código ASCII.")
    i += 1
if flag == 1:
    print("La cadena está ordenada según el código ASCII.")