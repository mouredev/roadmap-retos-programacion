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
 *
"""
from datetime import datetime, timezone

# https://www.python.org/

# Comentario de linea

""" Comentario de multiples lineas """

variable = 'Soy una variable'
CONSTANTE = 'Soy una constante'

# str
str_var = 'Hola'
print(f"la variable {str_var} es de tipo {type(str_var)}")

# int
int_var = 5
print(f"la variable {int_var} es de tipo {type(int_var)}")

# float
float_var = 3.4
print(f"la variable {float_var} es de tipo {type(float_var)}")

# Boolean
bool_var = True
print(f"la variable {bool_var} es de tipo {type(bool_var)}")

# Complex
complex_var = 3 + 5j
print(f"la variable {complex_var} es de tipo {type(complex_var)}")

# List
list_var = [5,4,'a']
print(f"la variable {list_var} es de tipo {type(list_var)}")

# Dictionary
dict_var = {'1':'a', '2':'b'}
print(f"la variable {dict_var} es de tipo {type(dict_var)}")

# Set
set_var = {'1','a',8,(5,'e')}
print(f"la variable {set_var} es de tipo {type(set_var)}")

# Tuple
tuple_var = (5,6,'a',(6,9))
print(f"la variable {tuple_var} es de tipo {type(tuple_var)}")

# Datetime
date_var = datetime.now()
print(f"la variable {date_var} es de tipo {type(date_var)}")

print("¡Hola, Python!")