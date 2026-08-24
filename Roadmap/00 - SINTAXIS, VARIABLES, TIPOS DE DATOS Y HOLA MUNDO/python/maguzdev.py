# ╔═══════════════════════════════════════╗
# ║ Autor:  maguzdev                      ║
# ║ GitHub: https://github.com/maguzdev   ║
# ║ 2026 -  Python                        ║
# ╚═══════════════════════════════════════╝

# -----------------------------------------------------
# 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
# ----------------------------------------------------- 

# SOLUCIONES DE EJERCICIO:

# 1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
"""
URL del sitio web oficial del lenguaje de programación Python.
https://www.python.org/
"""

# 2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

# Agregando un numeral (#) al inicio de la línea se crea un comentario de una línea

""" 
Agregando 3 comillas dobles 
al inicio y al final de la línea
se crea un comentario
de varias líneas
"""

'''
Agregando 3 comillas simples 
al inicio y al final de la línea
se crea un comentario
de varias líneas
'''
# 3. Crea una variable (y una constante si el lenguaje lo soporta).

name = "Manuel"
language = "Python"
age = 38;

# 4. Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

# Hay 4 tipos de datos primitivos:

# - Cadenas de texto (string):
text_strings = "Retos de Programación";

# - Números enteros (integer):
numbers_integers = 87;

# - Números flotantes (float):
numbers_floats = 87.5;

# - Booleanos lógicos (boolean):
booleans_true = True;
booleans_false = False;

# 5. Imprime por terminal el texto: "¡Hola, [y el nombre del lenguaje]!"
print(f"¡Hola, {language}!")