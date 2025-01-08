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


#https://www.python.org/



# One line comment

"""
multiline 
comment
"""

#var
num = 1


# Data types
my_int = 1
my_float = 0.1
my_str = "Hello Programming Challenges"
my_bool = True
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dictionary = {"key1": 1, "key2": "value2"}
my_null = None

# List with all values
list_with_all = [my_int, my_float, my_str, my_bool, my_list, my_tuple, my_set, my_dictionary, my_null]

print("-----Python Data Types-----")
for datatype in list_with_all:
    print(type(datatype).__name__,)
    print("-------------------")

print("hello, python")