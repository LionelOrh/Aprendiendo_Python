###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

import os
os.system("cls")

print("\n Ejercicio 1: Añadir y modificar elementos")
lista = [1, 2, 3, 4, 5]
lista.append(6)
print("Lista después de añadir 6:", lista)
lista.insert(2, 10)
print("Lista después de insertar 10 en la posición 2:", lista)
lista[0] = 0
print("Lista después de modificar el primer elemento:", lista)

print("\n Ejercicio 2: Combinar y limpiar listas")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print("Lista A después de extender con lista B:", lista_a)
lista_a.remove(1)
print("Lista A después de eliminar la primera aparición de 1:", lista_a)
elemento_eliminado = lista_a.pop(3)
print("Elemento eliminado en el índice 3:", elemento_eliminado)
lista_b.clear()
print("Lista B después de limpiar:", lista_b)


print("\n Ejercicio 3: Slicing y eliminación con del")
lista_numeros = list(range(1, 11))  # Lista con números del
print("Lista original:", lista_numeros)
del lista_numeros[2:5]  # Eliminar elementos desde el índice 2 hasta el 5 (sin incluir el 5)
print("Lista después de eliminar del índice 2 al 5:", lista_numeros)

print("\n Ejercicio 4: Ordenar y contar")
lista_numeros = [5, 2, 8, 1, 9, 4, 2]
lista_numeros.sort()  # Ordenar la lista de forma ascendente
print("Lista ordenada:", lista_numeros)
contador_dos = lista_numeros.count(2)  # Contar cuántas veces aparece el número 2
print("El número 2 aparece", contador_dos, "veces en la lista.")
print("¿El número 7 está en la lista?", 7 in lista_numeros)  # Comprobar si el número 7 está en la lista

print("\n Ejercicio 5: Copia vs. Referencia")
original = [1, 2, 3]
copia_1 = original[:]  # Copia usando slicing
copia_2 = original.copy()  # Copia usando copy()
referencia = original  # Referencia a la lista original
referencia[0] = 10  # Modificar el primer elemento de la referencia
print("Original:", original)
print("Copia 1:", copia_1)
print("Copia 2:", copia_2)
print("Referencia:", referencia)


print("\n Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas")
lista_cadenas = ["Manzana", "pera", "BANANA", "naranja"]
lista_cadenas.sort(key=str.lower)
print("Lista ordenada:", lista_cadenas)
# Fin de los ejercicios
