"""
/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
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
# COMENTARIOS:

# SITIO WEB OFICIAL:
# https://www.python.org/

"""
Comentario en 
varias líneas
"""

'''
Comentario en 
varias líneas
'''

# DECLARACION DE VARIABLES Y CONSTANTES:
# VARIABLE
my_variable: str = "Un string"
my_variable = "Otro string"
# CONSTANTE
MY_CONSTANT: str = "Un string constante que por convención no debe cambiarse porque está en mayúscula"

# DATATYPES PRIMITIVOS:
my_string: str = "¡Hola, Python!"
my_int: int = 1
my_float: float = 1.0
my_bool: bool = True

print(my_string)
print(type(MY_CONSTANT))
print(type(my_string))
print(type(my_int))
print(type(my_bool))