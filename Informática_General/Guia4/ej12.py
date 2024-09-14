base = int(input("Introduce la longitud de la base: "))
altura = int(input("Introduce la altura: "))

print("--- DIBUJO DE RECTÁNGULOS ---")
print(f"¿Qué dimensiones tiene el rectángulo?")
print(f"- Base: {base}")
print(f"- Altura: {altura}")

i = 0

while i < altura:
    if i == 0 or i == altura - 1:
        print('*' * base)
    else:
        print('*' + '+' * (base - 2) + '*')
    i += 1
