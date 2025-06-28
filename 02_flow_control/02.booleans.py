###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo en programación.
###

import os
os.system("cls")

#los boleanos son valores lógicos que pueden ser True o False
print("\n Booleanos en Python básicos")
print("True:")
print("False:")

# Operadores de comparación: devuelven un valor booleano
print("\n Operadores de comparación")
print("5 > 3:", 5 > 3)  # True
print("5 < 3:", 5 < 3)  # False
print("5 == 5:", 5 == 5)  # True (igualdad)
print("5 != 3:", 5 != 3)  # True (no igual)
print("5 >= 3:", 5 >= 3)  # True (mayor o igual)
print("5 <= 3:", 5 <= 3)  # False (menor o igual)


print("\nComparacion de cadenas")
print("'manzana' < 'pera':", "manzana" < "pera")  # True
print("'Hola' == 'hola':", "Hola" == "hola")  # False (diferencia de mayúsculas y minúsculas)


#Operadores lógicos: combinan valores booleanos
print("\nOperadores lógicos")
print("True and False:", True and False)  # False (ambos deben ser True
print("True and True:", True and True)  # True (ambos son True)
print("False or True:", False or True)  # True (al menos uno es True
print("False or False:", False or False)  # False (ambos son False)
print("not True:", not True)  # False (negación de True)
print("not False:", not False)  # True (negación de False)

# Tablas de verdad(para entender los operadores lógicos)
print("\nTablas de verdad")
print("AND (and):")
print("A     B     A and B")
print("True  True  ", True and True)  # True
print("True  False ", True and False)  # False
print("False True  ", False and True)  # False
print("False False ", False and False)  # False

print("\nOR (or):")
print("A     B     A or B")
print("True  True  ", True or True)  # True
print("True  False ", True or False)  # True
print("False True  ", False or True)  # True
print("False False ", False or False)  # False

