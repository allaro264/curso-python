"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la 
que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los 
números pares en la lista).
"""

from os import system
if system("clear") != 0: system("cls")

# Para ver si un número es par
# siempre usamos el módulo %
# nos da el resto de la división: eggs % 2 == 2

eggs_list = [3, 4, 2, 7, 8, 10, 5, 6, 1, 12]

def sum_carnivore_eggs(eggs):
    total_eggs = 0

    for egg in eggs:
        if egg % 2 == 0:
            total_eggs += egg
            return total_eggs
    else:
        return total_eggs
    
result = sum_carnivore_eggs(eggs_list)
print(f"Total de huevos de dinosaurios carnívoros: {result}")
