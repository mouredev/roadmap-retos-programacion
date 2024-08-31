'''
* EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del
   lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios
   en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos
   del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
'''

# Link de web oficial python : https://www.python.org/  

# Comentario en una línea

"""
Esto es un comentario de varias líneas
"""

'''
Esto es otra forma de un comentario
de varias líneas
'''

my_variable = "Hola"
my_variable = "Hola dios soy yo denuevo"

print(my_variable)


# Escribirlo en mayusculas ayuda a saber que esta variable es una cosntante por lo que no habria que cambiarla. 

MY_CONSTANT = "Mi constante" # por convención


# Datos Primitivos

variable_int = 2
variable_float = 2.5
variable_string = "Colo-colo"
variable_bool = True
variable_bool = False

print("Hola, python!")


# Para poder ver los tipos de datos de la variable podemos ocupar type()

print(type(variable_int))
print(type(variable_float))
print(type(variable_string))
print(type(variable_bool))

saludo = "Hola Mundo!"
print(saludo)
