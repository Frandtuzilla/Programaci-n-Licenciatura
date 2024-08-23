persona1 = int(float(input("Ingrese edad de la primera persona: ")))
persona2 = int(float(input("Ingrese edad de la segunda persona: ")))

if(persona1 <= persona2):
    print("La primera persona es más joven.")
elif(persona1 >= persona2):
    print("La segunda persona es más joven.")
else:
    print("Ambas personas tienen la misma edad.")