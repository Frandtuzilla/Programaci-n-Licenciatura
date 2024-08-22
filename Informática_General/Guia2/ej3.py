lado1 = float(input("Introduce el valor del lado 1: "))
lado2 = float(input("Introduce el valor del lado 2: "))

def datosRectangulo(lado1, lado2):
		perimetro = 2 * ( lado1 + lado2 )
		area = lado1 * lado2
		return perimetro, area

perimetro, area = datosRectangulo(lado1, lado2)
print(f"El perímetro es {perimetro}, y el área es {area}")