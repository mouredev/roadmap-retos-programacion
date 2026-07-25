"""
¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
- Recuerda que todas las instrucciones de participación están en el
  repositorio de GitHub.

Lo primero... ¿Ya has elegido un lenguaje?
- No todos son iguales, pero sus fundamentos suelen ser comunes.
- Este primer reto te servirá para familiarizarte con la forma de participar
  enviando tus propias soluciones.

EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web oficial del
  lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
  en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
  del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
debemos comenzar por el principio.
"""

# https://www.python.org/

# This is a single-line comment

# This 
# is 
# a 
# multi-line 
# comment

"""This is a single-line comment"""

"""
This 
is 
a 
multi-line 
comment
"""

my_variable = 'Python'
MY_CONSTANT = 23

print(f'{my_variable = }')
print(f'{MY_CONSTANT = }')

my_str = 'Jesús'
my_int = 21
my_float = 1.623
my_complex = 1j
my_boolean = True
# my_bytes = b'Hello'
# my_bytearray = bytearray(23)
# my_memoryview = memoryview(bytes(b'Hello'))

print(type(my_str))           # <class 'str'>
print(type(my_int))           # <class 'int'>
print(type(my_float))         # <class 'float'>
print(type(my_complex))       # <class 'complex'>
print(type(my_boolean))       # <class 'bool'>
# print(type(my_bytes))       # <class 'bytes'>
# print(type(my_bytearray))   # <class 'bytearray'>
# print(type(my_memoryview))  # <class 'memoryview'>

print('¡Hola, Python!') # ¡Hola, Python!
