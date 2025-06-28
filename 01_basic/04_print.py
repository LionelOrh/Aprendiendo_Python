###
#04 - Variables
# Las variables son contenedores para almacenar datos en memoria
#Python es un lenguaje de tipado dinámico y de tipado fuerte
###


#Asignar una variable
#solo hace falta poner esto

#my_name="LioDev"
#print("Mi nombre es", my_name)

age = 30
#print("Tengo", age, "años")
#age = 31
#print("Ahora tengo", age, "años")

#Tipado dinámico: significa que no es necesario declarar el tipo de dato de una variable
my_name="LioDev"
print(type(my_name))

#my_name = 30
#print(type(my_name))

#Tipado fuerte: significa que no se puede hacer operaciones entre tipos de datos diferentes

#print("10" + 20)
#f-strings (literales de cadena formateados)
print(f"Hola {my_name}, tengo {age} años")

#Convensiones de nombres de variables
#snake_case: se usa para variables y funciones
#PascalCase: se usa para clases
#UPPER_CASE: se usa para constantes

