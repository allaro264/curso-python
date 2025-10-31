###
# 03 - range()
# Permite crear un secuencia de números. Puede ser útil para for, pero solo para eso
##

print("\nrange():")

# nums = range(2, 5)# no es una lista
# print(type(nums)) 
#Generado una secuencia de números del 0 al 4
# for num in range(5):
#     print(num)

#     #range(inicio, fin)
#     for num in range(5,10):
#         print(num)

# range(inicio, fin, paso)
# for num in range(0,10,2):
#     print(num)

#negativos
for num in range(-5, 0):
     print(num)

#cuenta atras
for num in range(10, 0, -1):
     print(num)