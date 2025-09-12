"""
EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web
oficial del lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear
comentarios en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

by adra-dev.
"""

# https://www.python.org/

# This is a coment in line

'''
This 
is 
a multi
line coment.
'''

"""
This 
is 
also
a multi
line coment.
"""

variable = 'This is a variable'

CONSTANT = 'This is a constant if you read pep8 documentation'

# Crea variables representando los tipos de datos primitivos

none = None # Especial data type that has no value
int = 5 # integral data type
bool = True or False # logic or boolean data type
float = 3.141592 # real data type
complex = 3+5j # complex data type
str = 'Hello World!' # string data type
tuple = (334, 87.156) # An arbitrary secuence of objects
list = [2, 4.5, 65] # An arbitrary secuence of objects that we can manipulate
set = {"grape", "kiwi", "tomatoe"} # Like a list but elements can not repeat or be indexed
dict= {'price': 34, 'product': 'console', 'stock': 2} # These represent finite sets of objects indexed by nearly arbitrary values.

# See the entire list in: https://docs.python.org/3/reference/datamodel.html#set-types


print("¡Hola, Python!")