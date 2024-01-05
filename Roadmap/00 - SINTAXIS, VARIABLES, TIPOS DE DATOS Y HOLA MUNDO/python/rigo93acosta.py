# Reto 00
''' 
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
'''

# web_page_python: https://www.python.org

# Comentario one line

""" 
Comentario
multi
line
"""

# Variables y constantes
first_var = "Hi, I'm Rigo"
# No existen constantes, pero se llegó a convención de que se usaran MAYÚSCULAS
MY_CONST = "Rigo"

# Tipos de datos primitivos
first_str = "I's a string"
entero = 7
decimal = 3.14
complejo = 1993 + 25j 
booleano = False
lista = ["rigo", 25, False, [1, 2, 3]]
tuple = ("rigo", 25, True, [4, 5, 6])
my_set = {"rigo", 25, True}
diccionario = {
    "name": "Rigoberto  ",
    "age": 30
}
first_none = None

print('¡Hola, Python!')