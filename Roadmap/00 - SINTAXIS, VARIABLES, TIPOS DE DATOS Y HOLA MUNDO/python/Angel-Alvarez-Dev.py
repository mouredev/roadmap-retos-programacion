"""
* EJERCICIO:
   - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
   - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
   - Crea una variable (y una constante si el lenguaje lo soporta).
   - Crea variables representando todos los tipos de datos primitivos
     del lenguaje (cadenas de texto, enteros, booleanos...).
   - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

# Python URL:
# https://www.python.org/

# Este es un comentario en Python usando el "numeral".

"""
Este es un comentario
en varias líneas
usando comillas triples (simples o dobles).
"""

# Variables y Constantes
variable = "Mi variable en Python"
CONSTANTE = "Esta es una constante por convención"  # Convención

# Datos primitivos
# Tipo números
a_int = 3
a_float = 3.1415927
a_complex = 3.3 + 3j

# Tipo booleanos
a_true = True
a_false = False
a_none = None  # None es el equivalente a NULL en otros lenguajes.

# Tipo cadenas de caracteres
a_string = "Cadena de texto"  # Entre comillas simples o dobles.

# Imprimir tipos de datos
print(type(a_int))    # <class 'int'>
print(type(a_float))  # <class 'float'>
print(type(a_complex))  # <class 'complex'>
print(type(a_true))   # <class 'bool'>
print(type(a_false))  # <class 'bool'>
print(type(a_none))   # <class 'NoneType'>
print(type(a_string))  # <class 'str'>

# Imprime por terminal "¡Hola, [y el nombre de tu lenguaje]!"
print("¡Hola, Python!")
