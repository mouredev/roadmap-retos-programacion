#  * EJERCICIO:
#  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
#  *   lenguaje de programación que has seleccionado.
#  * - Representa las diferentes sintaxis que existen de crear comentarios
#  *   en el lenguaje (en una línea, varias...).
#  * - Crea una variable (y una constante si el lenguaje lo soporta).
#  * - Crea variables representando todos los tipos de datos primitivos
#  *   del lenguaje (cadenas de texto, enteros, booleanos...).
#  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"


# WEB OFICIAL : https://www.python.org/
webOficial = "https://www.python.org/"
print("esta es la web oficial de Python: ", webOficial)

# COMENTARIOS EN PYTHON:
# <- comentario en linea con el 'hashtag' -> #

"""
esto tambien es un comentario
que se puede usar en varias lineas
y se usa mas que nada para describir
la funcionalidad de un bloque de codigo
no uso tilde porque mi teclado es en ingles, 
les pido mil disculpas a sus ojos
"""

# variable:
soyUnaVariable = 'de tipo string'
soyOtraVariable = 2 # <- de tipo numero

# constantes -> python no tiene :) pero por convencion en python
# si se define una variable en MAYUS estamos declarando una constante
# pero es convencion, sigue siendo variable

NO_ME_CAMBIES = 'no es constante, pero es constante'

# tipos de datos primitivos:
string = 'caracteres'           # string
enteros = 23                    # enteros
decimales = 1.2                 # float
boolean = True                  # boolean
booleanFake = False             # boolean
print("tipos de datos: string:", string, "enteros:", enteros, "y un booleano en true:", boolean)

# ultimo ejercicio:
lenguaje = "python"
print("Hola, " + lenguaje + "!")