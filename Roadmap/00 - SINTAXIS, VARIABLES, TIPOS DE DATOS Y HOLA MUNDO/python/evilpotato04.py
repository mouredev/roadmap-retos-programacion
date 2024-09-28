#/*
# * EJERCICIO:
# * - Crea un comentario en el código y coloca la URL del sitio web oficial del
# *   lenguaje de programación que has seleccionado.
# * - Representa las diferentes sintaxis que existen de crear comentarios
# *   en el lenguaje (en una línea, varias...).
# * - Crea una variable (y una constante si el lenguaje lo soporta).
# * - Crea variables representando todos los tipos de datos primitivos
# *   del lenguaje (cadenas de texto, enteros, booleanos...).
# * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
# */

# https://www.python.org/

"""
Esto no es exactamente un comentario,
pero sirve como un comentario de varias líneas
o una String para la documentación del método
"""

# Tipos de datos primitivos simples
# -> numeros enteros (int)
numero_entero = 42
numero_negativo = -42

# -> numeros decimales (float)
numero_decimal = 4.2

# -> cadenas (strings)
message = 'hola mundo'
message2 = "hola mundo 2"

# -> booleanos (boolean)
esta_completo = True
se_acabo = False

# Tipos de datos primitivos compuestos (contenedores)
# -> listas (lists)
lista_de_tareas_1 = ["barrer la casa", "lavar la loza", "hacer la cena"]

# -> tuplas (tuples)
lista_de_tareas_2 = ("barrer la casa", "lavar la loza", "hacer la cena")

# -> diccionarios (dictionaries)
lista_de_tareas_3 = {
    "tarea_1": "barrer la casa",
    "tarea_2": "lavar la loza",
    "tarea_3": "hacer la cena"
}

print("¡Hola, Python!")