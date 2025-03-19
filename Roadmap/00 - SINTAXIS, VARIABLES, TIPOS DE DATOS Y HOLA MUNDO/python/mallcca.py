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

# Ejemplos de comentarios
# https://www.python.org/

"""
    Comentario
    en varias 
    líneas
"""

# Python no tiene sintaxis dedicada a constantes, pero como buena práctica se define en mayúsculas
PI = 3.1415

# Ejemplos de variables
var1 = 100
var2 = 'string'
var3 = 100.45
var4 = True

# Imprimir un mensaje
template = '¡Hola, {0:s}!'
language = 'Python'
message = template.format(language)
print(message)
