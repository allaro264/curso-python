###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas 
###

from os import system
if system("clear") != 0: system("cls")

lista1 = ['a', ' b','c', 'd']

lista1.append('e') # añade un elemento al final
print(lista1)

lista1.insert(1, '@') #inserta un elemento en la posicion que le indiques como primer argumento
print(lista1)

lista1.extend('h')# agrega elementos al final de una lista
print(lista1) 

#Eliminar elmentos de una lista
lista1.remove('@') #Elimina la primera aparicion de la codena de texto @
print(lista1)

ultimo =lista1.pop() #Eliminar el ultimo elmeto de la lista y devolverlo
print(ultimo)
print(lista1)

lista1.pop(1)#Elimmar el segundo elemento de la lista (es el indice 1)
print(lista1)

#Eliminar a lo biestia
del lista1[-1]
print(lista1)

lista1.clear() # eliminar todos los elemtos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['h', 'o', 'l', 'a']
del lista1[1:3]
print(lista1)

# Mas métodos útiles
print('Ordenar listas modifiacando la original')
numbers= [3,10,2,8,8,101]
numbers.sort()
print(numbers)

print("Ordernar listas creando una nueva lista")
numbers= [3,10,2,8,8,101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar lista de codes de texto (todo minuscula)")
frutas = ['manzana', 'pera', 'lista', 'manzana', 'pera']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar lista de codes de texto (mezcla mayuscula y minuscula )")
frutas = ['manzana', 'Pera', 'Lista', 'manzana', 'pera']
frutas.sort(key=str.lower)
print(frutas)

#mas metodos utiles
animals = ['dog', 'dog', 'zebra', 'monkey']
print(len(animals)) # tamaño de la lista -> 4
print(animals.count('dog')) # cuantas veces aparece el elemento 'dog' -> 2
print('panda' in animals) # Comprueba si hay un 'panda' en la lista -> false


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
print("\nejercicio 1")
list = [1,2,3,4,5]
list.append(6)
print(list)
list.insert(2, 10)
print(list)
list.pop(0)
list.insert(0, 0)
print(list)

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
print("\nejercicio 2")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
lista_a.pop(3)
print(lista_a)
lista_b.clear()
print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print("\nejercicio 3")
list = [1,2,3,4,5,6,7,8,9,10]
del list[2:4]
print(list)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

print("\nejercicio 4")
list = [5, 2, 8, 1, 9, 4, 2]
list.sort()
print(list)
print(list.count(2))
print(7 in list)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
print("\nejercicio 5")
original = [1, 2, 3]
copia_1 = sorted(original)
copia_2 = copia_1.copy()
referencia = original
referencia.insert(1,10)
referencia.remove(1)
print("Lista original: ", original, "Lista copia_01: ", copia_1, "Lista copia_2: ", copia_2, "Lista referencia: ", referencia)

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

print("\nejercicio 6")
frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort()
print(frutas)