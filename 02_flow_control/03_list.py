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

#print(lista1[1][0])

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
#lista1[110] = 20
#print(lista1)

#añadir elemntos a una lista
lista1 = [1,2,3]

# forma larga y menos eficiente
lista1 = lista1 + [4,5,6]
print(lsita1)

#forma corta y mas eficiente
lista1 += [7,8,9]
print(lista1)

#recuperar longitud de una lista
print("longitud de una lista", len(lista1))

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\n ejercicio 1")

mensaje = ["C"+"o"+"d"+"i"+"g"+"o"+" "+"s"+"e"+"c"+"r"+"e"+"t"+"o"]
print(mensaje)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\nejecicio 2")

numeros = [10, 20, 30, 40, 50]
print(numeros[::-1])

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

print("\nejecicio 3")

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sanwich = [pan, ingredientes, pan_abajo]

print(sanwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("\nejecicio 4")

lista = [1, 2, 3]
lista += lista
print(lista)
# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\nejercicio 5")

lista = [10, 20, 30, 40, 50]

print("el centro es:", lista[2:3])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("\n ejercicio 6")
lista = [1, 2, 3, 4, 5, 6]
print(lista[2::-1]+ lista[3:6])