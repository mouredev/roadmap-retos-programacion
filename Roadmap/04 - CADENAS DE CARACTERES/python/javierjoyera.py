#Acceso a carácteres específicos de una cadena, se hace mediante la posición del carácter en la cadena, empezando por 0.
my_string = "Mi cadena de caracteres"
print(my_string[5])

'''
Acceso a un rango de carácteres de una cadena, 
se hace mediante la posición del primer carácter del rango y la posición del último carácter del rango, 
separados por dos puntos. '''
my_substring = my_string[3:10] #Desde la posición 3 hasta la 10, sin incluir la 10.
print(my_substring) 

#Longitud de una cadena
my_len = len(my_string)
print(my_len)

#Concatenación de cadenas
my_string_1 = "Soy"
my_string_2 = " una cadena"
my_string_3 = " de caracteres"
my_string_4 = " concatenada"

my_concatenated_string = my_string_1 + my_string_2 + my_string_3 + my_string_4
print(my_concatenated_string)

#Repetición de cadenas
my_repeated_string = my_string_1 * 3
print(my_repeated_string)

#Recorrer una cadena con un bucle for
my_for_string = "Recorriendo una cadena con un bucle for"
for character in my_for_string:
    print(character)

#Convertir una cadena a mayusculas
my_upper_string = my_string.upper()
print(my_upper_string)

#Convertir una cadena a minusculas
my_lower_string = my_string.lower()
print(my_lower_string)

#Convertir una cadena a mayusculas la primera letra de cada palabra
my_title_string = my_string.title()
print(my_title_string)

#Reemplazar una cadena por otra
my_replaced_string = my_string.replace("cadena", "frase")
print(my_replaced_string)

#Dividir una cadena en una lista de subcadenas con un delimitador 
my_split_string = my_string.split(" ")
print(my_split_string)

#Union de una lista de subcadenas en una cadena con un delimitador
my_words = ["Mi", "cadena", "de", "caracteres"]
my_joined_string = " ".join(my_words)
print(my_joined_string)

#Interpolación de variables en una cadena
my_name = "Javier"
my_age = 27
my_interpolated_string = f"Me llamo {my_name} y tengo {my_age} años."
print(my_interpolated_string)

#Interpolación de variables en una cadena con formato
my_name = "Javier"
my_age = 27
my_interpolated_string = "Me llamo {} y tengo {} años.".format(my_name, my_age)

#Interpolación de variables en una cadena con formato y posición
my_name = "Javier"
my_age = 27
my_interpolated_string = "Me llamo {1} y tengo {0} años.".format(my_age, my_name)

#Interpolación de variables en una cadena con formato y nombre [Preferible para mi]
my_name = "Javier"
my_age = 27
my_interpolated_string = "Me llamo {name} y tengo {age} años.".format(age=my_age, name=my_name)

#Verificación de cadenas
my_number = "192304"
print(my_number.isnumeric()) 
print(my_number.isdigit()) 

my_string = "Iphone"
print(my_string.isalpha())
print(my_string.isalnum()) 
print(my_string.startswith("Z")) 
print(my_string.endswith("e")) 
print(my_string.islower()) 
print(my_string.isupper()) 
print(my_string.isspace()) #Comprueba si la cadena contiene solo espacios en blanco

#Busqueda de subcadenas
my_string = "Mi cadena de caracteres de python"
print(my_string.find("de")) #Devuelve la posición de la primera coincidencia en la cadena
print(my_string.rfind("de")) #Devuelve la posición de la última coincidencia en la cadena
print(my_string.count("e")) #Devuelve el número de veces que se repite el valor buscado

#modificacion de cadena eliminando espacios
my_string = "   Mi cadena de caracteres de python   "
print(my_string.strip()) #Elimina los espacios al principio y al final de la cadena
print(my_string.rstrip()) #Elimina los espacios al final de la cadena
print(my_string.lstrip()) #Elimina los espacios al principio de la cadena

my_new_string = "esta cadena empieza en minúscula"
print(my_new_string.capitalize()) #Pone la primera letra en mayúscula

print("--------------------")
print("Ejercicio Opcional")
print("--------------------")

#Ejercicio opcional
'''
Palindromo: Es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
Anagrama: Es una palabra o frase que tiene las mismas letras que otra, pero en diferente orden.
Isograma: Es una palabra o frase que no tiene letras repetidas.


Procedimiento:
- Crear las funciones para cada uno de los tres tipos
- Pedirle al usuario una cadena de caracteres
- Llamar a las tres funciones con la cadena de caracteres
- Mostrar por pantalla el resultado de cada función
'''

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1] #Compara la palabra con la palabra invertida

def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    return sorted(palabra1) == sorted(palabra2) #Compara las dos palabras ordenadas

def es_isograma(palabra):
    palabra = palabra.lower().replace(" ", "")
    return len(set(palabra)) == len(palabra) #Compara la longitud de la palabra con la longitud de la palabra sin caracteres repetidos

#Pedimos al usuario la entrada de las palabras
palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

#Llamamos a las funciones y mostramos el resultado
print("La palabra %s ¿Es palindromo?: %s" % (palabra1, es_palindromo(palabra1)))
print("La palabra %s ¿Es palindromo?: %s" % (palabra2, es_palindromo(palabra2)))
print("La palabra %s ¿Es anagrama de %s?: %s" % (palabra1, palabra2, es_anagrama(palabra1, palabra2)))
print("La palabra %s ¿Es isograma?: %s" % (palabra1, es_isograma(palabra1)))
print("La palabra %s ¿Es isograma?: %s" % (palabra2, es_isograma(palabra2)))



