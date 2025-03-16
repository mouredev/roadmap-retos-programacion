"""
* EJERCICIO:
   - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
   - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
   - Crea una variable (y una constante si el lenguaje lo soporta).
   - Crea variables representando todos los tipos de datos primitivos
     del lenguaje (cadenas de texto, enteros, booleanos...).
   - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

## Lenguaje Python ##

# URL sitio web oficial:
# https://www.python.org/

## Sintaxis para crear comentarios ##

# Comentarios en un sola linea:
# Se utiliza el caracter "#" para esto

# Comentarios en varias líneas:
"""
Esto es un comentario
en varias líneas
"""
'''
Esto tambien es
un comentario
de varias lineas
'''

## Variables y Constantes ##
var_mi_variable = "esto es una variable" # método de asignación de nombres snakecase
VALOR_CONSTANTE = 3.14 # por convención se nombra en mayusculas

## Datos primitivos ##

# Tipo numérico
entero = 8 # entero
decimal = 3.1415927 # decimales
complejo = 3.3 + 3j # complejo

# Tipo booleano
verdadero = True
falso = False
nulo = None  # None es el equivalente a NULL en otros lenguajes.

# Tipo cadenas de caracteres
string = "Cadena de texto"  # Entre comillas simples o dobles.

## Imprimir tipos de datos ##
print(type(entero))    # <class 'int'>
print(type(decimal))  # <class 'float'>
print(type(complejo))  # <class 'complex'>
print(type(verdadero))   # <class 'bool'>
print(type(falso))  # <class 'bool'>
print(type(nulo))   # <class 'NoneType'>
print(type(string))  # <class 'str'>

# Imprime por terminal "¡Hola, [y el nombre de tu lenguaje]!"
print("¡Hola, Python!")