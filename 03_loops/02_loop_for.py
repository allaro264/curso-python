##
# 02 - Bubles (for)
#   permiter ejecutar un bloeque de cñodigo reperidamente mientras ITERA un iterable o una lista
##

from os import system
if system("clear") != 0: system("cls")

print("\n bucle for")

#iterar una lsita
frutas = ["manzana", "nanana", "pera"]

for fruta in frutas:
    print(fruta)

 # iterar sobre cualquier cosa iterable
# cadena = "Hola"
# for letra in cadena:
#     print(letra)

    #enumerate()
    # frutas = ["manzana", "nanana", "pera"]
    # for index, value in enumerate(frutas):
    #     print(f"El indice es {index} y la fruta es {value}")

# bucles anidados
# letas = ["a", "b", "c"]
# numeros = [1,2,3]
# for numero in numeros:
#     print(f"{letas}x{numero}")

#     #break
#     animales = ["perro", "gato", "raton", "loro", "pez"]
#     for idx, animal in enumerate(animales):
#         print(animal)
#         if animal == "raton":
#             print(f"En ratnos esta escondidio en {idx}")
#             break
       
#        #continue
#     animales = ["perro", "gato", "raton", "loro", "pez"]
#     for idx, animal in enumerate(animales):
#         if animal == "raton":
#             continue

     

    #compreson de listas (list comprehensions)
    # animales = ["perro", "gato", "raton", "loro", "pez"]
    # animales_mauyusculas = [animal.upper() for animal in animales]
    # print(animales_mauyusculas)

    #Muestra los numeros pares de una lista
    # pares = [num for num in [1,2,3,4,5,6,7,8] if num % 2 == 0]
    # print(pares)

    # Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

pares = [num for num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] if num % 2 == 0]
print(pares)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0;
for number in numeros:
    suma += number
media = suma / len(numeros)
print(media)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for  number in numeros:
    if number > maximo:
        maximo = number
        print(number)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras2 = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras2)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ").lower()  # Convertimos la letra a minúscula
contador = 0
for palabra in palabras:
  if palabra.lower().startswith(letra):  # Comparamos en minúsculas
    contador += 1
print(f"Hay {contador} palabras que empiezan con la letra {letra}")