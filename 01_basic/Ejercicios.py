###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

nombre = "Lionel"
ciudad = "Ventanilla"
print(nombre)
print(ciudad)
### Completa aquí




print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")



### Completa aquí
cadena = "12345"
numero_entero= int(cadena)
numero_float = float(numero_entero)
print(numero_entero)
print(numero_float)

float_num = 3.99
print(int(float_num))

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

nombre = "Lionel"
edad = 19
estatura = 1.72

print(f"!Hola, mi nombre es {nombre} y tengo {edad}, mido {estatura} metros")

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

num = int(round(3.1416) / 2)
print("Valor de PI: ", 3.1416)
print("Valor redondeado: ", round(3.1416))
print("Division entera entre el redondeo de PI y el número 2 : " , num)