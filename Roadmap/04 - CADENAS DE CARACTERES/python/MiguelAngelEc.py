### OPERACIONES

from ast import If, IfExp
from socket import if_indextoname
import string


t1 = "Hola"
t2 = "Miguel Angel"
t3 = "Python"
t4 = "1234"

#Concatenación
saludo = t1 + ", " + t2
print(saludo)

#Repetición
print(saludo * 3)

#Indexación
print(saludo[1])

#Longitud
print(len(saludo))

#Slicing
print(t2[0:5])
print(t2[0:])
print(t2[:-1])

#Busqueda
print("a" in saludo)
print("i" in saludo)

#Reemplazo
print(saludo.replace("l", ""))

#Division
split1 = saludo.split(" ")
for i in range(len(split1)):
    print(split1[i])

#Mayuscuals y Minisculas
print(saludo.upper())
print(saludo.lower())
print("miguel angel castillo enriquez".title())
print("miguel angel castillo enriquez".capitalize())

#Eliminacion de espacios
print(" Miguel Angel ".strip())
print(" Miguel Angel ".lstrip())
print(" Miguel Angel ".rstrip())

#Busqueda al inicio y al final
print(saludo.startswith("Hola"))
print(saludo.endswith("Miguel"))

#Busqueda de posicion
print(saludo.find("Miguel"))
print(saludo.find("Angel"))
print(saludo.find("Hola"))

#Busqueda de ocurrencia
print(saludo.count("l"))

#Formateo
print("Saludo: {}, Lenguaje: {}!".format(saludo, t3))

#Interpolación
print(f"Saludo: {saludo}, Lenguaje: {t3}!")

#Transformación en lista de caracteres
print(list(t1))

#Transformación de lista en cadena
print("".join(list(saludo)))

#Transformaciones numéricas
print(t4.isnumeric())
print(t1.isnumeric())
print(int(t4))
print(float(t4))

# Comprobaciones
print(t1.isalnum())
print(t1.isalpha())
print(t1.islower())
print(t1.isdecimal())


"""
/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
*/
"""

def check(word1: string, word2: string):
   #Palindormos
   if word1 == word1[::-1]:
      print(f"La palabra {word1} es un palíndromo")
   else:
      print(f"La palabra {word1} no es un palíndromo")

   #Anagramas
   if sorted(word1) == sorted(word2):
      print(f"La palabra {word1} es un anagrama de {word2}")
   else:
      print(f"La palabra {word1} no es un anagrama de {word2}")

   #Isogramas
   if len(word1) == len(set(word1)):
      print(f"La palabra {word1} es un isograma")
   else:
      print(f"La palabra {word1} no es un isograma")

check("radar", "python")
check("amor", "roma")
check("python", "python")