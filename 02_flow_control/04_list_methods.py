###
#04 - Lista Métodos
# Los métodos de lista son funciones que permiten manipular listas de manera eficiente.
###

import os
os.system("cls")

lista1 =['a', 'b', 'c'] #lista de letras


lista1.append('f')  # Añadir un elemento al final
print("Lista después de append('f'):", lista1)

lista1.insert(2, '@')  # Insertar un elemento en una posición específica
print("Lista después de insert(2, '@'):", lista1)

lista1.extend(['g', 'h', '@'])  # Añadir varios elementos al final
print("Lista después de extend(['g', 'h', '@']):", lista1)

#Eliminar elementos de una lista
lista1.remove('@')  # Eliminar la primera aparición de un elemento
print("Lista después de remove('@'):", lista1)

ultimo = lista1.pop()  # Eliminar el último elemento y devolverlo
print("Lista después de pop():", ultimo)
print("Lista después de pop():", lista1)

lista1.pop(1)  # Eliminar un elemento en una posición específica
print("Lista después de pop(1):", lista1)

del lista1[0]  # Eliminar un elemento en una posición específica
print("Lista después de del lista1[0]:", lista1)

lista2 = ['a', 'b', 'c', 'd', 'e']  # Reiniciar la lista para el siguiente ejemplo
print("Lista original lista2:", lista2)
del lista2[1:3] # Eliminar un rango de elementos
print("Lista después de del lista2[1:2]:", lista2)
# La diferencia entre pop y del es que pop devuelve el elemento eliminado, mientras que del no lo hace, solamente elimina el elemento de la lista.


# Más metods utiles
print('Ordenar una listas modicando la lista original')
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()  # Ordenar la lista en orden ascendente, lo modifica la lista original
print("Lista después de sort():", numeros)

print('Ordenar listas creando una nueva lista')
numeros2 = [5, 2, 9, 1, 5, 6]
numeros2 = sorted(numeros2)  # Crear una nueva lista ordenada
print("Lista después de sorted():", numeros2)


# Más métodos útiles
animales = ['🐶', '🐱', '🐰', '🐹','🐶']
print(len(animales))  # Longitud de la lista
print(animales.count('🐶'))  # Contar cuántas veces aparece un elemento
print('🐱' in animales)  # Verificar si un elemento está en la lista


print("\nOrdenar una lista de cadenas de texto (todo en minúsculas)")
cadenas = ['manzanas', 'pera', 'limón', 'manzana', 'naranja']
sorted_frutas = sorted(cadenas)  # Crear una nueva lista ordenada
print("Lista después de sorted():", sorted_frutas)

print("\nOrdenar una lista de cadenas de texto (mezclas de mayúsculas y minúsculas)")
cadenas = ['manzanas', 'Pera', 'limón', 'manzana', 'naranja', 'BANANA']
cadenas.sort(key=str.lower)
print("Lista después de sort():", cadenas)