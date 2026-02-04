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


# Cómo usar la barra invertida para anular el significado especial de un símbolo
    text = "Mi cas es banca. Y el coche es negro."
    pattern = r"\."

    matches = re.findall(pattern, text)

    print(matches)


# \d: coincide con cualquier dígito (0-9)

text = "El nuero de telefono es 123456789"
found = re.findall(r'\d{9}', text)

print(found)

#Ejercicio: Detectar si hay un número de España en el text gracias al prefijo +34

text = "Mi número de teléfono es +34 6889999999 apúntado?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
if found: print(f"Encontré el número de teléfono {found.group()}")

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "el_marcos_21)/&"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)


# \s: Coincide con cualquier espacio en blanco (espacio, tabulaciñon, salto de línea )
text = "Hola mundo\n¿Cómo estás\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el principio de una cadena
username = "423_name%22"
pattern = r"^\w" #validar nombre de usuario

valid = re.search(pattern, username)

# numres de telefono
if valid: print("El nombre de usuario es válido")
else: print("El nombre de usuario no es válido")

phone = "+34 6899999999"
pattern = r"^\+\d{2,3} "

valid = re.search(pattern, phone)

if valid: print("El número de teléfono es válido")
else: print("El número de teléfono no es válido")

# $: Coincide con el final de un cadena
text = r"mundo$"

valid = re.search(pattern, text)

if valid: print("La cadena es valida")
else: print("La cadena no es válida")

# Ejercicio
# Valida que un correo se gmail
text = "prueba@gmail.com"
pattern = r"@gmail.com$"

valid = re.search(pattern, text)

if valid: print("el correo es válido")
else: print("el correo no es válido")

# Ejercicio:
# Tenemos una lista de archivos, nevesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf gif.webp secreto.txt"

pattern = r"\b.txt\b"

valid = re.findall(pattern, files)
print(valid)

# \b: Coincide con el principio o final de una palabra
text = "casa casado cansado casa"
pattern = r"casa"

found = re.findall(pattern, text)
print(found)

# or: Coincidir con una opción u otra
fruits = "limon, manzana, naranja, kiwi, platano, aguacate"
pattern = r"kiwi|platano|P..a|\b\w{7}\b"

found = re.findall(pattern, fruits)
print(found)