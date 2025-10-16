import os
os.system("cls")
###

# 02  Booleanos
# Valores logicos: True (verdadero) y False (falso).
# Fundamentos para le control de flujo y la logica en programacion
###

#los booleanos representan valores de verdad: True o False.
print("\n Valores booleanos basicos")
print(True)
print(False)

#Operadores de compracion: devulve un valor booleano.
#print("\n Operadores de compracion: ")
#print("5 > 3:", 5 > 3)
#print("5 < 3:", 5 < 3)
#print("5 == 3:", 5 == 3)
#print("5 != 3:", 5 != 3)
#print("5 >= 3:", 5 >= 3)
#print("5 <= 3:", 5 <= 3)

print("\n Comparacion de cadenas:")
print("mazana < pera", "manzana" < "pera: ") # True
#print("'Hola'" == "'hola'", "Hola" == "hola: ") # False


print("\n Tablas de la verdad:")
print("and:")
print("A    B        A and B")
print("True True ", True and True)
print("True False ", True and False)
print("False True ", False and True)
print("False False ", False and False)

print("\nor:")
print("A    B        A and B")
print("True True ", True or True)
print("True False ", True or False)
print("False True ", False or True)
print("False False ", False or False)

print("\n not:")
print("A    not A")
print("True ", not True)
print("False", not False)
