###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

import os
os.system("cls")

print("\n Ejercicio 1: El mensaje secreto")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
mensaje_secreto = mensaje[7:]
mensaje_secreto = "".join(mensaje_secreto)  # Unir los caracteres en una cadena
print("Mensaje secreto:", mensaje_secreto)

print("\n Ejercicio 2: Intercambio de posiciones")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0]  # Intercambiar primera y última posición y se lee de la siguiente manera
# numeros[0] = numeros[-1] y numeros[-1] = numeros[0]
print("Lista después del intercambio:", numeros)

print("\n Ejercicio 3: El sándwich de listas")
pan_arriba = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan_arriba + ingredientes + pan_abajo  # Concatenar las listas y se lee de la siguiente manera
# sandwich = ["pan arriba"] + ["jamón", "queso", "tomate"] + ["pan abajo"]
# sandwich = ["pan arriba", "jamón", "queso", "tomate", "pan abajo"]
print("Sándwich:", sandwich)


print("\n Ejercicio 4: Duplicando la lista")
lista = [1, 2, 3]
lista_duplicada = lista * 2  # Duplicar la lista
print("Lista duplicada:", lista_duplicada)

print("\n Ejercicio 5: Extrayendo el centro")
lista_impar = [10, 20, 30, 40, 50]
centro = lista_impar[len(lista_impar) // 2] # Extraer el elemento del centro y se lee de la siguiente manera
# centro = lista_impar[2]  # En este caso, el índice del centro es 2
# porque la longitud de la lista es 5, y 5 // 2 = 2 
# y // significa división entera
print("Elemento del centro:", centro)  # Extraer el elemento del centro

print("\n Ejercicio 6: Reversa parcial")
lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) //2 
print("Mitad de la lista:", mitad)
lista_invertida = lista[:mitad][::-1] + lista[mitad:]  # Invertir la primera mitad
print("Lista después de invertir la primera mitad:", lista_invertida)

# esto se lee de la siguiente manera
# lista_invertida = lista[:3][::-1] + lista[3:]
# lista_invertida = en donde lista[:3] es [1, 2, 3] y [::-1] invierte la lista, y que cada punto dentro del corte [::-1] significa que se lee de derecha a izquierda
# lista_invertida = [3, 2, 1] + [4, 5, 6]
# lista_invertida = [3, 2, 1, 4, 5, 6]
