"""
Respuesta al ejercicio 00
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

# https://python.org/

# Comentario en una línea

"""
Esto es 
un comentario
en varias líneas
"""

'''
Esto también es 
un comentario 
en varias líneas
'''
# Declaración de variables y constantes
my_variable: str = "Ejemplo de variable"
my_variable: str = "Nuevo valor de mi variable"

MY_CONSTANT: float = 3.1416 # por convención las constantes se escriben en mayúsculas

# Tipos de datos primitivos
my_int: int = 7
my_float: float = 7.1
my_bool: bool = True
my_bool: bool = False
my_string: str = "Ejemplo de string"
my_other_string: str = 'Ejemplo de string con comillas simples'

print("¡Hola, Python!")

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))