###
# 03 - Listas
# Secunecias mitables de elmentos. Pueden contener elmentos de diferentes tipos.
###
from os import system
if system("clear") != 0: system("cls")
#Çreacion de listas 
print("/n creacion de listas")
lista1 = [1,2,3,4,5] #lista de neteros
lista2 = ["manzana", "pera", "platano"] # lista de cadenas
lsita3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lsita_vacia = []
lsita_de_listas= [[1,2], [3,4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lsita3)
print(lsita_vacia)
print(lsita_de_listas)
print(matrix)

#aceso a elmentos por indice
print("\n acceso a elementos por índice")
print(lista2[0])
print(lista1[1])
print(lista2[-1]) # platano
print(lista2[-2])#pera

print(lista1[1][0])

# Slici (rebanado) de listas
lista1 = [1,2,3,4,5]
print(lista1[1:4]) # 234
print(lista1[:3]) # 123
print(lista1[3:]) # 345
print(lista1[:]) # 12345

# hay mas magia
lsita1 = [1, 2 ,3 , 4, 5, 6]
print(lista1[::3]) # para devolver indices pares
print(lista1[::-1])# para devolver indeces inversos

#modificar una lsita
lista1[110] = 20
print(lista1)

#añadir elemntos a una lista
lista1 = [1,2,3]

# forma larga y menos eficiente
lista1 = lista1 + [4,5,6]
print(lsita1)

#forma corta y mas eficiente
lista1 += [7,8,9]
print(lista1)