# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

## Ejercicio

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
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.

'''
# https://python.org

# hola soy un comentario

'''
    Hola soy un 
    comentario de varias lineas
    con el uso de 3 comillas simples.
'''

"""
    Hola soy un 
    comentario de varias lineas
    con el uso de 3 comillas dobles.
"""

# Variable:
mi_variable = 12

# Constante:
CONSTANTE_EULER = 2.71

# Tipos de datos primitivos
mi_entero = 16
mi_flotante = 1.25
mi_cadena = "Hola Mouredev!"
mi_otra_cadena = 'Buen día Mouredev'
mi_booleano = True
mi_complejo = 2 + 3j
mi_nulo = None

# Impresión por terminal:
lenguaje = "Python"
print(f"¡Hola, {lenguaje}!")