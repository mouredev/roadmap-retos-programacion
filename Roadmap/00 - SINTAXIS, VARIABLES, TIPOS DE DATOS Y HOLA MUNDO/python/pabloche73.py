### http:\\python.org ###

# Esta es una de las formas de comentar en Python
# Podemos usar el símbolo numeral (#) para comentar una sola línea
# Podemos usar tres comillas dobles para comentar varias líneas

"""
Este es un comentario multilínea
¿Se nota?¿No?
Ua línea mas.
"""

# Podemos usar comillas simples tambien en comentarios multilínea

'''
Este
también
es un
comntario multilinea
'''

# Tipos de Variables

my_str = "Hola, mundo!" # String
my_int = 52 # Integer
my_float = 1.80 # Float
my_bool = True # Boolean
my_list = [35, 24, 62, 52, 30, 30, 17] # List
my_tuple = (52, 1.80, "Pablo", "Demonte", "Pablo") # Tupla
my_set = {"Pablo", "Demonte", 52} # Set
my_dict = {"Nombre": "Pablo", "Apellido": "Demonte", "Edad": 52, 1: "Python"} # Dictionario

# Para saber el tipo de variable podemos usar la funcion type()
print(type(my_str))
print(type(my_int))
print(type(my_float))
print(type(my_bool))

# Como en Python las constantes no existen como tal, se usa la convención de escribir las variables en mayúsculas
MY_CONST = "Soy una constante" # O al menos eso intento

my_str = "Hola, Python!"
print(my_str)