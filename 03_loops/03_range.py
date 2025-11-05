###
# 03 - range()
# Permite crear un secuencia de números. Puede ser útil para for, pero solo para eso
##

from os import system
if system("clear") != 0: system("cls")


print("\nrange():")

# nums = range(2, 5)# no es una lista
# print(type(nums)) 
#Generado una secuencia de números del 0 al 4
# for num in range(5):
#     print(num)

#     #range(inicio, fin)
#     for num in range(5,10):
#         print(num)

# range(inicio, fin, paso)
# for num in range(0,10,2):
#     print(num)

#negativos
# for num in range(-5, 0):
#      print(num)

# #cuenta atras
# for num in range(10, 0, -1):
#      print(num)

# nums = range(10)
# list_of_nums = list(nums)
# print(list_of_nums)


# for _ in range(5):
#     print("Hacer algo")

    ###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

for nums in range(1,11):
    print(nums)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

for nums in range(1,21,2):
    print(nums)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

for nums in range(5,51,5):
    print(nums)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

for nums in range(10,0,-1):
    print(nums)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

for nums in range(1,101,+1):
    suma = 0
    suma += nums
    print(suma)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

num = int(input("Introduzca un número para mostrar su tabla de multiplicar:"))
for i in range(1,11):
    print(f" {num * i}")