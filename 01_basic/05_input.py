##
#05 - Entrada de usuario (input()) - Version simplificada
# La funcion imput nos permite obtener datos del usuario a traves de la consola 
##


nombre = input("Hola como te llamas?\n")

print(nombre)

print(f"hola {nombre}, encantado de conocerte")

age = input("cuantos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives?\n").split()

print(f"vives en {country}, {city}")