##
#04 - Funciones
#Bloques de código reutilizables que parametizables para hacer tares especificas
##

#*** Definicion de funcion

# def nombre_de_la_funcion(parametro1, parametro2 ...):
#     #docstring
#     #cuerpo de la funcion
#     return valor_de_retorno

# ***

# Ejemplo de una funcion para imrimir algo en la consola
# def saludar():
#     print("Hola")

#     saludar()

    #Ejemplo de una funion con parametro
# def saludar(nombre):
#     print(f"Hola, {nombre}")

# saludar("Gold ship")
# saludar("Tokai Teio")
# saludar("Mejiro McQeen")
# saludar("Daiwa Scarlet")
# saludar("Vodka")
# saludar("Silince Suzuka")
# saludar("Special Week")
# saludar("Trainer san")

# #Funciones con mas parametros
# def sumar(a,b):
#     suma = a + b
#     return suma

# result = sumar(2,3)
# print(result)

# #Dicumetar las funciones con docstring
# def restar(a,b):
#     """Resta dos numeros y devuelve el resultado"""
#     return a - b 


#help(restar)

#pararmetros por defecto
# def multiplicar(a,b =2):
#     return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por clave
# def describir_persona(nombre, edad, sexo):
#     print(f"Nombre: {nombre}, tengo {edad}, me identifico como {sexo}")

# describir_persona("Triner san", 25 , "Masculino")
# describir_persona("Gold ship", 16, "Umamusume")

# #Argumentos por clave
# # parametros nombrados
# describir_persona(sexo="gato", nombre="Silince Suzuka", edad=15)
# describir_persona(sexo="Umamusume", edad=14, nombre="Special Weeek")

# #argumentos de longitud de varibles (*args,):
# def sumar_numros(*args):
#     suma = 0
#     for numeros in args:
#         suma += numero
#     return suma

# print(sumar_numros(1,2,3,4,5))
# print(sumar_numros(1,2))

# #Argumentos de calve-valor variable ()
# def monstrar_informacion(**kwargs):
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# describir_persona( nombre="Silince Suzuka", edad=15, sexo="Umamusume")
# print("\n")
# monstrar_informacion(nombre="Daiwa Scarlet", edad=14, sexo="Umamusume", raza="Thoroughbred")


# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora