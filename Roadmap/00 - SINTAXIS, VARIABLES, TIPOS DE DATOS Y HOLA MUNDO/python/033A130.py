# https://python.org

# => Esto es un comentario en una línea en Python.

"""
Así se crean comentarios 
multilínea en Python.
"""

'''
También podemos usar comillas simples
para comentarios multilínea.
'''

# Variables en Python.
"""En Python, es una convención nombrar las variables en formato `snake_case`,
es decir, todo en minúsculas y separado por guiones bajos.
"""

# Tipo de variable tipo cadena de texto = string.
"""Cuando asignamos un valor entre comillas (simples o dobles), la variable
automáticamente toma el tipo `str` (cadena de texto). Incluso si parece un número.
"""

my_variable = "¡Hola, esta es mi variable!"

my_string = "¡Esta es una string!"
my_other_string = '¡También esta es una string!'

my_variable_saludos = "¡Hola Python!"
# Las variables pueden cambiar de valor. Hasta este punto, `my_variable` es:
# "¡Hola, esta es mi variable!". Ahora le asignamos un nuevo valor:
my_variable = "Ahora mi variable ha tomado este nuevo valor de texto."

# Tipo de variable tipo entero = int
"""Si creamos una variable y le asignamos un número sin comillas,
el tipo asignado será automáticamente un entero (`int`)."""

my_int = 1 

# Tipo de variable tipo flotante = float
"""Si creamos una variable y le asignamos un número decimal (separado por un punto,
no por una coma), el tipo asignado será automáticamente flotante (`float`).
"""

my_float = 1.735

# Tipo de variable tipo booleano = bool
"""Las variables booleanas (`bool`) solo pueden tener dos valores posibles:
`True` o `False` (en mayúsculas, ya que son palabras clave de Python).
"""

my_bool = True 
my_second_bool = False 

# Constantes en Python.
"""En Python, las constantes no existen como tal. Sin embargo, por convención,
se escriben con letras mayúsculas para indicar que no deberían modificarse.
Aunque técnicamente, su valor puede cambiar.
"""

MY_CONSTANTE = "Mi Constante"  # Por convención.

# Aquí cambiamos el valor de la "constante", aunque no debería hacerse.
MY_CONSTANTE = "¡Mi Constante ha cambiado de valor!"

# Maneras de imprimir un valor, una variable o una CONSTANTE por convención.
print("Hello World!")  # Si queremos imprimir un número u otro tipo, no ponemos comillas.
print(my_variable_saludos)
print(MY_CONSTANTE)

# Manera de imprimir el tipo de una variable.
# La función `type` nos muestra el tipo de una variable.
print(type(my_string))  # Salida: <class 'str'>
print(type(my_int))     # Salida: <class 'int'>
print(type(my_float))   # Salida: <class 'float'>
print(type(my_bool))    # Salida: <class 'bool'>
