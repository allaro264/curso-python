###
 # 01 - Bucles (while)
# Permiten ejecutar un bloque de código repedidamente mientras se cumpla una condición
###


from os import system
if system("clear") != 0: system("cls")

# print("\n Bucle while")

# contador = 0 
# while contador < 5:
#     print(contador)
# contador += 1 # es super inportante para evitar bucles infinitos

# # utilizando break, pra romper el bucle
# while True:
#     print(contador)
#     contador += 1
#     if contador == 5:
#         break # sale del bucle

# # continue, para saltar a la siguiente iteración en concreto
# # y continuar con el bucle
#     print("\n un bucle con cotinue")
#     contador = 0
#     while contador < 10:
#         contador += 1

#         if contador % 2 == 0:
#             continue

#         print(contador)

# # else, para ejecutar un bloque de código cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
#     break
# else:
#     print("El bucle ha finalizado")

#     # pedirle al usuario un numero que tine que ser potivo
#     numero = -1
#     while numero <= 0:
#         numero = int(input("Escribe un número positivo:"))
#         if numero <= 0:
#             print("El número debe de ser positivo. Intentalo otra vez.")

# print(f"El número que has introducido es {numero}")

# numero = -1
# while numero < 0:
#     try:
#         numero = int(input("Escribe un número positivo: "))

#         if numero < 0:
#             print("El número debe ser positivo. Intentalo de nuevo.")
#     except:
#          print (" Por favor, introduce un múmero")

#     print(f"El número que has introducido es {numero}")

# ejercicios

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador = 0
while contador >= 10:
    contador += 1 
    print(contador)
 

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

contador = 0
while contador <= 20:
    contador += 1 
    if contador % 2 == 0:
        continue
    print(contador)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("Introduce un número entero positivo: "))
factorial = 1
contador = 1

while contador <= numero:
  factorial *= contador
  contador += 1

print(f"El factorial de {numero} es: {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contrasena = ""
while len(contrasena) < 8:
  contrasena = input("Introduce una contraseña (al menos 8 caracteres): ")
  if len(contrasena) < 8:
    print("La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")

print("Contraseña válida")

        

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# contador = input()
# contador1 = 0
# contador2 = 0

# while contador1 <= 10:
#     contador1 += 1
#     contador2 = int(contador) * contador1
#     print(contador2)

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

# contador = input()

# while contador >= contador:
#     contador += 1
#     contador % 2 == 0
#     print(contador)