###
# 03 -Listas
# Las listas son colecciones ordenadas de elementos que pueden ser de diferentes tipos.
# Pueden contener números, cadenas, booleanos, e incluso otras listas.
import os
os.system("cls")
#Creación de una lista
print("\n Creación de una lista")
lista1 =[1, 2, 3, 4, 5] #lista de números
lista2 = ["manzanas", "peras", "cerezas", "kiwis"] #lista de cadenas
lista3 = [1, "a", True, 3.14] #lista de tipos mixtos

lista_vacia = [] #lista vacía
lista_de_listas = [[1, 2], [3, 4], [5, 6]] #lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #matriz (lista de listas)
print("Lista de números:", lista1)
print("Lista de cadenas:", lista2)
print("Lista de tipos mixtos:", lista3)
print("Lista vacía:", lista_vacia)
print("Lista de listas:", lista_de_listas)
print("Matriz:", matriz)

# Acceso a elementos de una lista
print("\nAcceso a elementos de una lista")
print("Primer elemento de lista2:", lista2[0])  # Acceso al primer elemento
print("Último elemento de lista2:", lista2[-1])  # Acceso al último elemento


print(lista_de_listas[1][0])  #Se lee como "primer elemento de lista_de_listas y segundo elemento de la lista"

# Slicing de listas (rebanado)
print("\nSlicing de listas")
lista1 =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números del 1 al 10
print("Lista original:", lista1)
print("Elementos del índice 1 al 3:", lista1[1:4])  # Elementos del índice 1 al 3 (sin incluir el 4) [2, 3, 4]

print("Los primeros 3 elementos:", lista1[:3])  # Primeros 3 elementos [1, 2, 3]
print("Los últimos 2 elementos:", lista1[3:])  # Últimos 2 elementos [4, 5]
print("Copia completa:", lista1[:])

#print(lista1[desde:hasta:paso])  # Slicing con paso
print("Lista en 2 en 2:", lista1[::2])  # Lista en 2 en 2 [1, 3, 5, 7, 9]
print("Lista en 1 en 1:", lista1[::1])  # Lista en 1 en 1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Hay mas magia
print("Lista en 3 en 3:", lista1[::3])  # Lista en 3 en 3 [1, 4, 7, 10]
print("Lista al revés:", lista1[::-1])  # Lista al revés [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Lista duplicada sin afectar la original:", lista1 * 2)  # Duplicar la lista sin afectar la original [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Modificación de elementos de una lista
print("\nModificación de elementos de una lista")
lista1[0] = 1  # Cambiar el primer elemento
print("Lista modificada:", lista1)

# Añadir elementos a una lista
print("\nAñadir elementos a una lista")
lista1 = lista1 + [11, 12]  # Añadir varios elementos al final
print("Lista después de añadir elementos:", lista1)

#Forma correcta de añadir un elemento
lista1 += [13]  # Añadir un solo elemento al final
print("Lista después de añadir un elemento:", lista1)


# Recuperar longitud de una lista
print("\nRecuperar longitud de una lista")
print("Longitud de lista1:", len(lista1))  # Longitud de la lista