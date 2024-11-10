"""
EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 """


# Esta es la web oficial de python https://python.org

# Sintaxis de comentarios:

# Este es un comentario de una sola linea

"""
Este es un comentario de varias lineas
"""

'''Este es otro comentario de varias lineas'''

# Definicion de variables:
my_variable = "Soy una variable"

#definicion de constantes por convencion se escriben en MAYUSCULAS.
MY_CONSTANT = "Soy una constante"

# Tipos de datos primitivos:
my_int = 42
my_float = 6.22
my_string = "Hola, Python"
another_string = 'Python, Hola!'
my_bool = True
another_bool = False    

# Imprimir por consola:
print("Hola, Python!")
print(my_variable)
print(MY_CONSTANT)
print(my_int)
print(my_float)
print(another_string)
print(type(my_bool))
print(type(my_string))