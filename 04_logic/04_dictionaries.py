###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")


persona = {
    "nombre": "Alex",
    "edad": 21,
    "es_estudiante": True,
    "Calificaciones": [7,8,9],
    "socials": {
        "twitter": "@falso123",
        "instagram": "@falso123"
    }
}

# acceder a valores
#print(persona["nombre"])
#print(persona["Calificaciones"][2])
#print(persona["socials"]["instagram"])

#cambiar valores al acceder 
persona["nombre"] = "Umapoy"
persona["Calificaciones"][2] = 10

#eliminar completamente una propiedad
del persona["edad"]
#print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = {"name": "Alex", "age" : 25}
b = {"name": "Umapoy", "city": "CDMX"}

a.update(b)
print(a)

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

#obtener todas las claves
print("\nkeys:")
print(persona.keys())

# ontener todos los valores
print("\nvalues:")
print(persona.values())

# obtner tanto clave como valor
print("\nitems:")
print(persona.items())

for key, value in persona.items():
    print(f"{key}: {value}")