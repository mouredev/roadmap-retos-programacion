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

# https://www.python.org/

 # Este es un comentario.

"Este es un segundo comentario en una línea."

"""
Este es un tercer
comentario en
tres líneas.
"""

variable = 0  # Ejemplo de una variable.

PI = 3.14159  # Esta es una constante.
print(type(PI))

int_var = 1   # Una variable int
print(type(int_var))

float_var = 3.14  # Una variable float
print(type(float_var))

complex_var  = 3+2j  # A complex variable
print(type(complex_var))

string_var = "Hola mundo."
print(type(string_var))

bool_var = True
print(type(bool_var))

print("Hola, python!")