import os
os.system('cls')
from itertools import permutations
import re
from unicodedata import normalize
"""
* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación..."""

print("MÉTODOS Y MANIPULACIONES BÁSICAS CON STRINGS")
my_string = "Hola PYTHON"
print ("\"Hola Python\"")
#Para imprimir con comillas o caracteres reservados se usa backslash antes del caracter

print(r"c:\users\usuario\carpeta\archivo.txt")
#Si queremos imprimir un string que incluya backslash formateamos con una r (raw string)

print("Ho" + "la Py" + "thon") 
#Concatenación de varios strings

print ("Ding! " * 5)
 #Python admite multiplicaciones de strings

print (str(len("123456789")) + " caracteres")
 #La función len() devuelve medida en int, str castea a string y + concatena

print(len("123456789") * 9)
# La función len() devuelve cantidad de caracteres y se puede operar con el número resultante

print(my_string.find("THON"))
# .find devuelve el índice donde comienza la subcadena especificada

print(my_string.replace("PYTHON","JAVASCRIPT"))
# .replace sustituye la parte del string especificada por otra especificada

print(my_string.capitalize())
# .capitalize devuelve el string con el primer caracter en mayúsculas y el resto en minúsculas

print(my_string.upper())
# .upper devuelve todo el string en mayúsculas

print(my_string.lower())
# .lower devuelve todo el string en minúsculas

print(my_string.swapcase())
# .swapcase cambia los caracteres en minúsculas por mayúsculas y viceversa

print(my_string[2:8])
#Deja sólo los caraceteres dentro del rango, el resto los borra(en este caso borra los 0,1,9,10 y 11)

print(my_string[:8])
#En caso de omitir el primer valor equevale a 0 y solo borra a partir del valor especificado

lista_caracteres_ascii = [72,111,108,97,32,80,121,116,104,111,110]
#lista con los códigos ascii de "Hola Python"

[print(chr(i) , end='') for i in lista_caracteres_ascii]
#Con la función chr() obtenemos el caracter asociado a su código ascii

print('')
[print(my_string[i] , end='') for i in range(len(my_string))]
#Se pueden recorrer los caracteres de un string con un bucle for por índice 


print('')
[print(my_string[i] , end='') for i, char in enumerate(my_string)]
#Tambien con un bucle for por índice usando la función enumerate()

print('')
[print(char , end='') for char in my_string]
#Se pueden recorrer los caracteres de un string con un bucle foreach sin índice

print('')
print("abracadabra".count("bra"))
#El método .count devuelve la cantidad de veces que se repite un substring

print("  Hola Python  ".strip())
#El método .strip elimina los espacios que haya al principio y al final de un string

print("1001".zfill(8))
#Con .zfill rellenamos con ceros a la izqda el string pasándole el nº total de caracteres

print(my_string.split("HO"))
# .split devuelve una lista con las subcadenas divididas por el caracter especificado (que se elimina)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos clean_words diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagrams
 * - Isograms"""

def remove_diacritic (string)->str:
  string = str(string)
  string = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", string), 0, re.I
    )
  string = normalize( 'NFC', string)
#Borra los símbolos diacríticos excepto la ñ y la diéresis
  return string.lower().replace(' ', '')






def anagram (word1,word2):
    clean_word1, clean_word2 = remove_diacritic(word1), remove_diacritic(word2)
    list1, list2 = list(clean_word1), list(clean_word2)  
    list1.sort()
    list2.sort()
    sorted1, sorted2 = "".join(list1), "".join(list2)
    if sorted1 == sorted2:
        print(f"Las palabras {word1} y {word2} son anagramas")
    else:
      print(f"Las palabras {word1} y {word2} no son anagramas")

anagram("Fotolitografía", "Litofotografía")




def isogram (word1,word2):
 char_dict = {}
 clean_word = remove_diacritic(word1)+remove_diacritic(word2)
 for char in clean_word:
   if char in char_dict:     
      char_dict[char] +=1
   else:
      char_dict[char] =1
 
 char_set = set(char_dict.values())
 if len(char_set) > 1:
   print(f"Las palabras {word1} y {word2} concatenadas no son un isograma")
 else:
   print(f"Las palabras {word1} y {word2} concatenadas son un isograma")
 print("nº de veces que se repite cada letra:") 
 [print("\n",char, count , end = ' : ') for char, count in char_dict.items()] 

isogram ("paz" , "porrazo")


def palindrome (string1, string2):
  string = remove_diacritic(str((string1+string2)))
  reverse = string[::-1]
  if string == reverse:
    print (f"La frase formada por \" {string1}\" y \"{string2}\" forman un palíndromo")
  else:
    print (f"La frase formada por \" {string1}\" y \"{string2}\"  no forman un palíndromo")

palindrome("Arriba" , "la birra")






