###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código basados en condiciones.
###

import os
os.system("cls")

print("\n Sentencia simple condificional (if)")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")

    ### Es importante las tabulaciones para definir el bloque de código

edad = 17
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")

print("\n Sentencia condicional con else")
edad = 17
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("!No estas calificado!")

print("\n Condiciones múltiples")

edad = 10
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")

if edad >= 18 or tiene_licencia:
    print("Puedes conducir")
else:
    print("Paga al policía y te dejará conducir")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Hoy es un día laborable")

print("\n anidando condiciones")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes comprar una cerveza")
    else:
        print("No tienes dinero para comprar una cerveza")
else:
    print("No puedes comprar una cerveza porque eres menor de edad")

###Simplificado
#if edad < 18:
    print("No puedes comprar una cerveza porque eres menor de edad")
#elif tiene_dinero:
#    print("Puedes comprar una cerveza")
#else:
#     print("No tienes dinero para comprar una cerveza")
numero = 10
if numero: #True
    print("El número es verdadero (no es cero)")

numero = 0
if numero: #False
    print("Aqui no se ejecuta porque el número es cero")


nombre = "Python"
if nombre:  # True (no es una cadena vacía)
    print("El nombre no está vacío")


numero = 5; #Asignación
if numero == 5:  # Comparación
    print("El número es igual a 5")


#Condicion ternaria
print("\nCondición ternaria")
#Es una forma compacta de escribir una sentencia if-else
#[valor_si_verdadero] if [condición] else [valor_si_falso]
edad = 20
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)