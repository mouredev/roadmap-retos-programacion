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
"""
# Ese es un comentario multilinea y este es de una linea

# Sitio oficial: https://www.python.org/

cadena = str("abc 123 @#$")
numeros_enteros = int("123")
numeros_con_decimales = float("12.34")
booleanos = bool(0)

print("Tipos de datos en las variables")
print("Strings:", cadena)
print("Numeros enteros:", numeros_enteros)
print("Numeros con decimales:", numeros_con_decimales)
print("Datos booleanos:", booleanos)
print("-" * 25)
numeros_enteros = "Python"
print("Hola,", numeros_enteros)
