
#funciones

def filtrar_pals_unicas(lista_palabras):
  #IN: ["melon", "kiwi", "manzana", "kiwi","melon","pera","kiwi","manzana"]
  #OUT:["melon", "kiwi","manzana","pera"]
  pals_unicas = []
  for pal in lista_palabras:
    if pal not in pals_unicas:
      pals_unicas.append(pal)
  return pals_unicas
  

def cantidad_palabras(lista_palabras, pals_unicas):
  #IN1: ["melon", "kiwi", "manzana", "kiwi","melon","pera","kiwi","manzana"]
  #IN2:["melon", "kiwi","manzana","pera"]
  #OUT:[  2,       3,       2,       1  ]
  cantidades = []
  for elem in pals_unicas:
    cont=0
    for pal in lista_palabras:
      if elem == pal:
        cont+=1
    cantidades.append(cont)
  return cantidades
  

def ordenar_dos_listas(l1, l2):
  for i in range(len(l1)-1):
    for j in range(i+1, len(l1)):
      if l2[i] < l2[j]:
        l2[i], l2[j] = l2[j], l2[i]
        l1[i], l1[j] = l1[j], l1[i]

def mostrar_dos_lista(l1, l2):
  for i in range(len(l1)):
    print(l1[i],l2[i])


# Main
lista_palabras = ["melon", "kiwi", "Manzana", "kiwi","melon","pera","kiwi","manzana"]

#1. formo lista de pals únicas
pals_unicas = filtrar_pals_unicas(lista_palabras)

#2.Armamos la lista con la cantidades de cada palabra
lista_cants = cantidad_palabras(lista_palabras, pals_unicas)
  
#3. Ordenar por la cantidad de ocurrencias
ordenar_dos_listas(pals_unicas, lista_cants)
  
#4. Mostrar listas
mostrar_dos_lista(pals_unicas, lista_cants)

