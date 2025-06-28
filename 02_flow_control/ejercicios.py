###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

import os
os.system("cls")
print("\n Ejercicio 1: Determinar el mayor de dos números")

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 > numero2:
    print(f"El número mayor es: ", numero1)
elif numero1 < numero2:
    print(f"El número mayor es: ", numero2)
else:
    print("Ambos números son iguales")


print("\n Ejercicio 2: Calculadora simple")
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

print(f"Resta: {numero1} menos {numero2} es igual a = ", numero1 - numero2)
print(f"Suma: {numero1} más {numero2} es igual a = ", numero1 + numero2)
print(f"Multiplicación: {numero1} por {numero2} es igual a = ", numero1 * numero2)
if numero2 != 0:
    print(f"División: {numero1} entre {numero2} es igual a = ", int(numero1 / numero2))

print("\n Ejercicio 3: Año bisiesto")

año = int(input("Introduce un año: "))
if (año % 4 == 0 and año % 100 !=0) or (año % 400 ==0):
    print(f"El año {año} es bisiesto.")

print("\n Ejercicio 4: Categorizar edades")
edad = int(input("Introduce tu edad: "))
if 0 <= edad <= 2: # Esto lee como "0 es menor o igual que edad y edad es menor o igual que 2"
    print("Eres un bebé.")
elif 3 <= edad <= 12: # Esto lee como "3 es menor o igual que edad y edad es menor o igual que 12"
    print("Eres un niño.")
elif 13 <= edad <= 17: # Esto lee como "13 es menor o igual que edad y edad es menor o igual que 17"
    print("Eres un adolescente.")
elif 18 <= edad <= 64: # Esto lee como "18 es menor o igual que edad y edad es menor o igual que 64"
    print("Eres un adulto.")
else: # Esto lee como "edad es mayor o igual que 65"
    print("Eres un adulto mayor.")
