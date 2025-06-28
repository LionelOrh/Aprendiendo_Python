###
#✅ Ejercicio 6: Suma y resta de números
#Crea dos variables numéricas, una con tu edad y otra con una #cantidad de años que han pasado.
#Resta esos años a tu edad y muestra el resultado.
#Luego, suma 10 años más y muestra la nueva edad.
###

#edad = 19
#cant_years = 4
#primer_r= edad - cant_years
#segundo_r= primer_r + 10
#print(f"Edad actual {edad}")
#print(f"Años que pasaron : {cant_years}")
#print("Restamos el tiempo que paso: ", primer_r)
#print("Sumamos 10 años más y el resultado es: ", segundo_r )

#✅ Ejercicio 7: Cadenas de texto
#Crea una variable frase con el texto "Hola, soy Lionel y me gusta #programar"
#Imprime:

#El número total de caracteres.

#La misma frase toda en mayúsculas.

#Solo la palabra "programar", usando slicing.

frase="Hola, soy Lionel y me gusta programar"
print(len(frase))
print(frase.upper())
inicio = frase.find("programar")
fin = inicio + len("programar")

print(frase[inicio:fin])