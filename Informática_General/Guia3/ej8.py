palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra3 = input("Ingrese la tercera palabra: ")

if palabra1 >= palabra2 and palabra1 >= palabra3:
    mayor = palabra1
elif palabra2 >= palabra1 and palabra2 >= palabra3:
    mayor = palabra2
else:
    mayor = palabra3

if palabra1 <= palabra2 and palabra1 <= palabra3:
    menor = palabra1
elif palabra2 <= palabra1 and palabra2 <= palabra3:
    menor = palabra2
else:
    menor = palabra3

print(f"La palabra mayor es: {mayor}")
print(f"La palabra menor es: {menor}")

if menor == menor[::-1]:
    print(f"La palabra '{menor}' es capicúa.")
else:
    print(f"La palabra '{menor}' no es capicúa.")
