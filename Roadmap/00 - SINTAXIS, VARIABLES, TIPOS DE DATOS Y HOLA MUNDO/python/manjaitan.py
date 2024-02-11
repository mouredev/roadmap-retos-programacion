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
 
# URL del sitio oficinal Python. 
# https://www.python.org/

# Diferentes sintaxis para crear comentarios:
# Comentario de única línea.

# Comentario en bloque:
"""
El texto incluido entre las tres comillas, es un texto comentario, y podemos incluir bloque de texto como utilidad para comentar nuestro código.
"""

# Crea una variable ( y una constante si el lenguaje lo soporta)
variable1="Esto es una variable"

# En python no existen como tal y para diferenciarlas tenemos que ponerlas en mayúsculas.
CONSTANTE1="Esto es una conStante"

# Crea variables representando todos los tipos de datos primitivos
# del lenguaje (cadenas de texto, enteros, booleanos...).

var_cadena1="Python"
var_int=3
var_decimal=2.2
var_boolean=True

print (type(var_cadena1))
print (type(var_int))
print (type(var_decimal))
print (type(var_boolean))

# Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

print ("¡Hola, " + var_cadena1 + "!")

