###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena
###

import re

# *: Puede aparecer 0 o más veces
text= "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

#Ejercicio 1:
#¿Cuantas palabras tienen de 0 a más "a" y despues una b?

# +: Una a más veces
text = "dddd aaa ccc bb"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

#?: Cero o una vez
text = "aaaba"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

#Ejercicio: Haz que aparezca un +34 en el siguiente ejercicio
phone = "+34 6889999999"
pattern = r"\+34\s\d{9}"
matches = re.findall(pattern, phone)
print(matches)


# {n}: Exactamente n veces
text = "aaaaaaa     aa       aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)

# {n, m}: De n a m veces
text = "u uu uuu uuuuuuu"
pattern = "u{2,3}"
matches = re.findall(pattern, text)
print(matches)

#Ejercicio:
#Encuenatra las palabras de 4 a 6 letras en el siguiente texto
words= "ala casa árbol león murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

#Ejercicio
# Encuentra las palabras de mas de 6 letras 
words= "ala casa fantastico árbol león murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)
