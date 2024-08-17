"""
* EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

# Python URL:
# https://www.python.org/

# Esto es un comentario en una linea usando el "numeral"

""" 
Esto es tambien
es un comentario 
en varias lineas usando "comillas dobles"
"""

'''
Esto tambien 
es un comentario
de varias lineas usando 'comillas simples'
'''

# Variables y Constantes:
variable = "My variable en Python"
CONSTANTE = "Esto es una constante por convención" #convención

# Datos primitivos 
# Tipo Número

a_int = 3
a_float = 3.33
a_complex = 3.3 + 3j

#Tipo boolean
a_true = True
a_false = False
a_none = None # En otros lenguajes es lo equivalente a "NULL"

# Tipo cadena caracteres
a_string = "Cadena de texto" # Entre comillas simples o dobles

# Imprimir tipos de datos 
print(type(a_int)) # <clas 'int'>
print(type(a_float)) # <clas 'float'>
print(type(a_complex)) # <clas 'complex'>
print(type(a_true)) # <clas 'true'>
print(type(a_false)) # <clas 'false'>
print(type(a_none)) # <clas 'none'>
print(type(a_string)) # <clas 'string'>

#  Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print("Hola, Python")

