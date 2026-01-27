from os import system
if system("clear") != 0: system("cls")
##
# 01 - Expresines regulares
#

"Las expresiones regulares son una secuancia de caracteres que forman un patrón de búsqueda."
"Se utilizan para la búsqueda de cadenas de texto, validacion de datos, etc. "

" ¿Por que aprender Regex?"
""
"- Búsquda avanzada: Encontrar patrones específicos en texto grandes de forma rápida y precisa. (un editor de sólo usando Regex)"
""
"- validación de datos: Asegurarte que los datos que ingresa un usuario como el email, telefono, etc. "

"-Extrarcion de información: Permitir obtener y aprovechar datos específicos de un texto, como nombres, fechas o direcciones"

"-Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto"

#1. primer paso importar el modulo de expresionres regulares "re"
import re
# 2. crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
# 3. El texto donde  queremos buscar
text = "Hola mundo"
#4. Usar la funcion de búsqueda de "re" 
result = re.search(pattern, text)

if result:
    print("He encontrado el patrón en el texto")
else:
    print("No he encontrado el patrón en el texto")

# .group() devulve la cadena que coincide con el pattern
result.group()

# .start() devolver la posicion inicial de la councidencia
print(result.start())

# .end devolver la posicion finalde la coincidencia
print(result.end())

#Ejercicio 01
# Encontrar la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posicion empieza la conincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con la Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
    print(f"He encontrado el patrón en el texto en la posicion {found_ia.start()} y termina en la posicion {found_ia.end()}")
else:
    print("No he encontrado el patrón en el texto")


    ## Encontrar todas las coincidnecias de un patrón
    # .findall() devuelve una lista con todas las coincidencias

    text= "Me gusta Phthon. Python es lo máximo. Aunque Python no es tan dificil, ojo con Python"
    pattern = "P.thon"

    matches = re.findall(pattern, text)

    print(len(matches))
   