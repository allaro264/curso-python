import re

# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match: 
    print("El nombre de usuario es válido: ", match.group())
else:
    print("El nombre de usuario no es valido")


# Buscar todas las bocales vocales de una palbra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
#Nos han complicado el asusnto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman, fanatico, man bandana"
# \b
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png
url= "https://www.computerhope.com/jargon/r/regular-expression.png"

pattern = r"https?://[\w.-]+(?:\.[\w.-]+)+[/\w._%+-]*\.(?:jpg|jpeg|png|gif|bmp|svg)"
matches = re.findall(pattern, url)
print(matches)


## Buscar corner cases que no pasa y arreglarlo:
email ="lo.que+sea@shopping.online"

local, domain = email.split("@", 1)
local = local.split("+", 1)[0].replace(".", "")
clean = f"{local}@{domain}"
print(clean)

email2 = "michael@gov.co.uk"

local, domain = email2.split("@", 1)
domain = domain.replace(".", "", 1)
print(f"{local}@{domain}")

# [^]: Coincide con cualquier caracter que no esté dentro de los caracteres
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)