#  https://www.python.org/

# Este es un comentario.

"""
Este es un comentario
en varias
líneas
"""

'''
Este también es otra forma k
de poner 
un
comentario 
en varias 
líneas 
'''

# Creación de una variable

my_variable = ""    

# Tipos de variables

my_string = "My String in Python"
print(type(my_string))  # Tipo de variable
print(my_string)    # Impresión de la variable

my_int = 13
print(type(my_int))
print(my_int)

my_float = 1.3
print(type(my_float))
print(my_float)

my_complex = 1j
print(type(my_complex))
print(my_complex)

my_boolean = True 
print(type(my_boolean))
print(my_boolean)

my_list = []
print(type(my_list))
print(my_list)

my_tuple = ()
print(type(my_tuple))
print(my_tuple)

my_sets = {"It is set"}
print(type(my_sets))
print(my_sets)

my_dictionary = {}
print(type(my_dictionary))
print(my_dictionary)

# Cambiar tipos de datos a otro tipo de dato
# OJO ASI TAMBIÉN SE PUEDE DEFINIR UNA VARIABLE A ESE TIPO DE DATO, ES DECIR, ES LO MISMO "LIST() == []", "TUPLE() == ()", "SET() == {}"

convert_to_str = str()
convert_to_int = int()
convert_to_float = float()
convert_to_complex = complex()
convert_to_bool = bool()
convert_to_list = list()
convert_to_tuple = tuple()
convert_to_set = set()
convert_to_dictionary = dict()

language = "Python"
print("Hola %s" %(language))