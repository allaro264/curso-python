"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

from os import system
system("cls")

nums = [4, 5, 6, 2]
goal = 8
def find_first_sum(nums, goal):
    seen = {} #dicionario para guardar el numero y su indice

    for i, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return [seen[missing], i]
        seen[value] = i

    return None

result = find_first_sum(nums, goal)
print(result)
