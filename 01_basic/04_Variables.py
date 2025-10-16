##
# 04 - Variables
# Las variables sirven para guardar datos de memoria
# Python es un lenguaje de tipado y de tipado fuerte
##

# Asignar variable
# solo hacefalta poner esto
My_name = "Alex"

#print(My_name)

#age = 32
#print(age)

age= 39
print(age)

#Tipado dinámico: el tipo de dato se determina en tipo de ejecucion
# que no tienes que declararlo explicitamente

name = "Alex"
print(type(name))

name = 32
print(type(name))

#Tipado fuerte: Python no realiza conversiones de tipo automatico
#pirnt(10 + "2")

# f-sting (literal de formato)
# desde la version 3.6
print(f"Hola {My_name}, tengo {age+ 5} años")

#No recomendada forma de asignar variables
name, age, city = "Alex", 32, "Bogota"

#Convenciones de nombres de variables
mi_nombre_de_varible = "ok" #snake_case
minombredevariable = "ko" #todojunto

mi_nombre_de_varible123 = "ok"

MI_CONSTANTE = 3.14 #Upper_Case --> constantes


# Nobres no validos de variables
# 123213_varibale = "ko"
# mi-varible = "ko"
# mi variblae = "ko"
# true = False

is_user_logged_in: bool = True
print(is_user_logged_in)


