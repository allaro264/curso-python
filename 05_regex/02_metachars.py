from os import system
if system("clear") != 0: system("cls")

import re

###
# 02 - Meta caracteres
# Los metacatacteres som simbolos especiales con significados especiales especificos en las expresiones regulares.
###

# 1. el punto (.)
#coincidit con un coracter exceto el una nueva linea

text = "Hola mundo, H0la de nuevo, H0la otra vez"
pattern = "H.ola"

found = re.findall(pattern, text)

if (found):
    print(found)
else: 
    print("No se ha encontrado el patrón")

    text="casa caasa cosa cisa cesa causa"
    pattern = "c.sa"

    matches = re.findall(pattern, text)
    print(matches)

    # -----------------------

    ext = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.ola" # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
    print(found)
else: 
    print("No se ha encontrado el patrón")


    text = "Mi cas es banca. Y el coche es negro."
    pattern = "."

    matches = re.findall(pattern, text)

    print(matches)
