# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
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
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */
"""

# Sitio oficial de Python
# https://www.python.org/
 
# Comentario de una linea

"""
   Comentario de múltiples líneas 
   con comillas dobles
"""

'''
  Comentario de múltiples líneas 
  con comillas simples
'''

# Variable
mi_variable = 'valor'
'''
Constante: No existen las constantes en Python pero se puede usar 
un nombre en mayúsculas como convención para identificarla como tal
''' 
MI_CONSTANTE = 'NO CAMBIAR'
'''
# Tipos de Datos primitivos
Strings (str).
Integers (int).
Floats (float).
Booleans (bool)
None (caso especial).
'''
string_var = 'Esta es una variable string'
print(type(string_var))

integer_var = 44
print(type(integer_var))

float_var = 16.8
print(type(float_var))

boolean_var = True
print(type(boolean_var))

none_var = None
print(type(none_var))

print ('¡Hola, Python!')