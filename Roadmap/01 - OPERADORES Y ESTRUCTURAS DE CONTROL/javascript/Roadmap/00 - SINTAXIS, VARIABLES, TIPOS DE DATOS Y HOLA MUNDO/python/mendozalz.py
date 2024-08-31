'''
EJERCICIO:
[X] Crea un comentario en el código y coloca la URL del sitio web oficial del
    lenguaje de programación que has seleccionado.

[X] Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...).

[X] Crea una variable (y una constante si el lenguaje lo soporta).

[X] Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...).

[X] Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"


'''


# Pagina web de python - https://www.python.org/

#--------------------------------------------------#

## Comentarios en una Linea con Python

# Esto es un comentario de una linea

#--------------------------------------------------#

## Comentarios en varias Lineas con Python

"""
Esto es un comentario
de varia Lineas con comillas dobles
"""

'''
Esto es un comentario
de varia Lineas con comillas sencillas
'''

#--------------------------------------------------#

## Variable

mi_var = "Esta es una variables"


## Constante según convención

MI_VAR = "Esta es una constante según la convención"

#--------------------------------------------------#

## Datos primitivos y sus tipos

### Entero o Int

mi_int = 44

### Float (datos flotantes o con decimales)

mi_float = 3.14

### Bool (booleanos)

mi_bool_true = True
mi_bool_false = False

### String o Str

mi_string = "Esta es una cadena de texto"

#--------------------------------------------------#

### Imprimiendo en la terminal

p = "Python"

print (f"¡Hola, {p}!")