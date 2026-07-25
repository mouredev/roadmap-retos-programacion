
#Cadenas de caracteres

 #operaciones





cadena1 = "hello"
cadena2 = "world"
cadena4 = "   H e l l o  "

from operator import gt
from optparse import Values
import re
from test.dis_module import f
from test.test_operator import PyCOperatorPickleTestCase

# Concatenación / Concatenation

cadena3 = cadena1 + " " + cadena2 #los "" son importantes para mantener el espacio en esta concatenación
print(cadena3)

"""
a una cadena de texto sumarle otra, sin mas xd
Joins two strings into one.
"""

# Repetición / Repetition

print(cadena1 * 3)

"""
Repite la cadena un número determinado de veces con *.
Repeats the string a specified number of times.
"""

# Acceso a caracteres / Indexación / Indexing


print(cadena1[0] + cadena1[1] + cadena1[2] + cadena1[3] + cadena1[4])

"""Acceso a cada carácter de la cadena al índice correspondiente solo usando indexación [] """

# Acceso a caracteres inverso / Reverse Indexing
ultimo_caracter = cadena1[-1]
print(ultimo_caracter)

"""Acceso al último carácter de la cadena"""


# Longitud / Length

print(len(cadena1))

"""len mide la longitud de la cadena"""


# Slicing (porciones)

slicing = cadena1[0:5]
print(slicing)

"""
Slicing básico / Basic Slicing
Extrae una parte de la cadena.
tambien conlleva un concepto de inicio, fin y paso.
donde  
#Índice o inicio
Es donde comienza el corte (incluido). Se refiere a que incluye el carácter en esa posición, si se omite se asume que es 0.

Fin Índice donde termina el corte (excluido). Se refiere a que no incluye el carácter en esa posición, si se omite se asume que es el final de la cadena.

paso Índice que determina el salto entre cada elemento, si se omite se asume que es 1. si usas paso negativo, recorres la secuencia en orden inverso. 
(se refiere a que el último carácter tiene índice -1)

Extracts a part of the string.
It also involves a concept of start, end, and step.
Index where slicing starts (inclusive).
End index where slicing ends (exclusive).
Step index that determines the jump between each element.

"""



#busqueda de caracteres / Character Search

"""se puede buscar si un carácter o subcadena está presente en la cadena solo con la palabra clave in (seguida de la variable o iterable)- 
Detalles importantes

- Sensibilidad a mayúsculas/minúsculas: "A" no es igual a "a".
- No da posición: Si necesitas saber dónde está el carácter, debes usar .find() o expresiones regulares.
- Funciona con cualquier iterable: También puedes usarlo en listas, tuplas, sets, etc.
"""
print("H" in cadena1) #Devuelve false, ya que el carácter o subcadena no está presente en la cadena.
print("h" in cadena1) #Devuelve true, ya que el carácter o subcadena está presente en la cadena.
print("hell" in cadena1) #Devuelve true, ya que el carácter o subcadena está presente en la cadena.


"""Busca una subcadena dentro de otra cadena y devuelve el número de posición (índice) donde aparece por primera vez.
Returns the index of the first occurrence of a substring within another string.
"""

#remplazo / Replacement
print(cadena1.replace("h", "J")) #Sustituye una subcadena por otra (Replace a substring with another)
print(cadena1.replace("l", "m"))  #aqui la reemplazo en todas las apariciones ( Reemplazar múltiples veces / Replace multiple occurrences)
print(cadena1.replace("l", "m", 1)) # Solo reemplaza las primeras n veces (Reemplazo limitado / Limited replacement)
print(cadena1.replace("hello", "see u") + " " + cadena2.replace("world", "round")) #Reemplazo encadenado / Chained replacement Puedes encadenar .replace() varias veces.
if "hello" in cadena1 or "world" in cadena2: 
    print(cadena1.replace("hello", "see u") + " " + cadena2.replace("world", "round")) #Reemplazo condicional  (con lógica) / Conditional replacement Solo reemplaza si se cumple una condición.

Gt = "Paprikaistkrieg"
saludo = cadena1 + " " + cadena2
saludo = saludo.replace(cadena2, Gt)
print(saludo) # Reemplazo con variables / Replacement using variables Puedes usar variables para personalizar el reemplazo.

lista = ["toby", "wilson", "mango"]
lista1 = [michis.replace("toby", "benito") for michis in lista]
print(lista1) # Reemplazo en listas / Replacement in lists Puedes usar listas y comprensión de listas para reemplazar en múltiples cadenas.

#division

"""
La división de cadenas se puede realizar utilizando el método .split() que separa una cadena en una lista de subcadenas.
"""
print(cadena1.split("l")) # Divide la cadena en una lista usando "l's" como separador. (desecha ese criterio, aunque este depende del lenguaje)
print(cadena1.split("e")) # Divide la cadena en una lista usando "e" como separador. (desecha ese criterio, aunque este depende del lenguaje)

#Conversion a mayusculas / Conversion to uppercase /convesion a minusculas y letras mayusculas 

print(cadena1.upper()) # Convierte toda la cadena a mayúsculas. (all string)
print(cadena1.lower()) # Convierte toda la cadena a minúsculas. (all string)
print(cadena1.capitalize()) # Capitaliza la primera letra de la cadena.  (solo la primera letra de la cadena)
print(cadena3.title()) # Capitaliza la primera letra de cada palabra en la cadena. (la primera letra de cada una de las palabras)
print(cadena1.swapcase()) # Invierte las mayúsculas y minúsculas en la cadena. (invierte las mayusculas y minusculas)

# Eliminación de espacios en blanco / Whitespace Removal (al principio y al final)

print("@Paprikaistkrieg" + cadena4.strip()) # Elimina los espacios en blanco al principio y al final de la cadena.
print(cadena4.lstrip()) # Elimina los espacios en blanco al principio de la cadena.
print(cadena4.rstrip() + "@Paprikaistkrieg") # Elimina los espacios en blanco al final de la cadena.

#busqueda al principio y al final

print(cadena1.startswith("h")) # Devuelve True si la cadena comienza con "h".
print(cadena1.endswith("o")) # Devuelve True si la cadena termina con "o".
print(cadena1.startswith("H")) # Devuelve false 
print(cadena1.endswith("O")) # Devuelve false 

#busqueda de posicion


print(cadena1.find("H")) # Devuelve -1 si no se encuentra
print(cadena1.find("l")) # Devuelve 2 (debido a la posicion en la que se encuentra)
print(Gt.find("r")) # Devuelve 4 (debido a la posicion en la que se encuentra)
print(Gt.lower().find("i"))# Devuelve -1 (debido a la posicion en la que se encuentra, pero este devuelve la primer ocurrencia que coincide con el criterio de busqueda)



print(cadena1.find("H")) # Devuelve -1 (debido a la posicion en la que se encuentra)
print(cadena1.find("l")) # Devuelve 2 (debido a la posicion en la que se encuentra)
print(cadena1.find("o")) # Devuelve 4 (debido a la posicion en la que se encuentra)
print(cadena1.find("h")) # Devuelve 0 (debido a la posicion en la que se encuentra)


#busqueda de todas las ocurrencias
print(Gt.lower().count("a"))# Devuelve 2 (debido a las ocurrencias de "a" en la cadena)

#Formateo de cadenas / String formatting
"""
Es el proceso de insertar valores dentro de una cadena sin tener que concatenar manualmente. En lugar de hacer esto:
"""
nombre = "Paprikaistkrieg"
edad = 26
print(f"Hola, soy {nombre} y tengo {edad} años.") # Formateo con f-strings (se interpreta que todo lo que este dentro de llaves es una variable)
print("Hola, soy {} y tengo {} años.".format(nombre, edad)) # Formateo con .format()


#para evitar
print("Hola, soy " + nombre + " y tengo " + str(edad) + " años.") # concatenación de cadenas

#interpolación de cadenas (f strings)
print(f"Hola, soy {nombre} y tengo {edad} años.") # Formateo con f-strings (se interpreta que todo lo que este dentro de llaves es una variable)
print(f"{cadena1} {cadena2}")
print(f"{nombre} has {edad}.")
print("{nombre} has {edad}.") #aqui no lo imprime con las variables debido a que no esta interpolado

#transformación en lista de caracteres

print(list(cadena1)) # Convierte la cadena en una lista de caracteres.

#transformación de lista en cadena
cadena5 = [cadena1, cadena2, "iam", Gt]
print(" ".join(cadena5)) # Une/concatena los elementos de la lista en una cadena, separados por un criterio (" "  el espacio en este caso es el criterio de separación).

#transformaciones numericas
cadena6 = "12345"
cadena6 = int(cadena6)
print(cadena6)
print(type(cadena6))

cadena7 = "12345.123"
cadena7 = float(cadena7)
print(cadena7)
print(type(cadena7))

#Comprobaciones

cadena8 = "12345"
cadena8 = (cadena8)

cadena9 = "12345.123"
cadena9 = str(cadena9)
print(cadena1.isalnum()) # Devuelve True si la cadena es alfanumérica (si tiene letras o numeros)
print(cadena1.isalpha()) # Devuelve True si la cadena solo contiene letras (si son solo letras)
print((cadena8.isdigit())) # Devuelve True si la cadena solo contiene dígitos (si son solo dígitos)
print((cadena8.isdecimal())) # Devuelve True si la cadena es decimal (si son solo números decimales, osea del 0 al 9)
print((cadena8.isnumeric())) # Devuelve True si la cadena es numérica (si son solo números)


#Xtra

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos (una palabra que se lee igual al derecho que al revés)
 * - Anagramas (dos palabras que tienen las mismas letras en diferente orden)
 * - Isogramas (Cada letra aparece el mismo número de veces. Ej: todas una vez, dos veces, etc.
Heterograma: Cada letra aparece una sola vez. Es un isograma de primer orden.
Isograma de segundo orden: Cada letra aparece dos veces, etc.
Isograma de tercer orden: Cada letra aparece tres veces, etc.
"""
def check(palabra1: str, palabra2: str):
    # palíndromo
    print(f"¿'{palabra1}' es palíndromo?", palabra1 == palabra1[::-1])
    print(f"¿'{palabra2}' es palíndromo?", palabra2 == palabra2[::-1])

    # anagrama
    print(f"¿'{palabra1}' es anagrama de '{palabra2}'?", sorted(palabra1) == sorted(palabra2))

    # isograma

    print(f"¿'{palabra1}' es heterograma?", len(palabra1) == len(set(palabra1)))
    print(f"¿'{palabra2}' es heterograma?", len(palabra2) == len(set(palabra2))) # Heterograma ya que no se repite ninguna letra

    def isograma(palabra: str):
        word_dict = dict()
        for letra in palabra:
            word_dict[letra] = word_dict.get(letra, 0) + 1

        Values = list(word_dict.values())
        isogram = True
        for letra in Values:
            if letra != Values[0]:
                isogram = False
                break
        return isogram, word_dict

    isograma_result, word_dict = isograma(palabra2)
    print(f"¿'{palabra2}' es isograma?", isograma_result)
    print(f"¿'{palabra1}' es isograma?", isograma_result)

check("python", "pythonpythonpython")

