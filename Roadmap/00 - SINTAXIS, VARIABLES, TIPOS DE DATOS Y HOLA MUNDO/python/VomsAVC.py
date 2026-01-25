# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

# Ejercicio
# Lo primero... ¿Ya has elegido un lenguaje?
# - Crea un comentario en el código y coloca la URL del sitio web oficial del
#   lenguaje de programación que has seleccionado.

# https://www.python.org/

# - Representa las diferentes sintaxis que existen de crear comentarios
#   en el lenguaje (en una línea, varias...).

# La forma correcta y recomendada para varias líneas de comentario es repetir # en cada línea:
# Esto es un comentario de varias líneas
# Otra línea de comentario
# Luego están las triple comillas (""" o '''), pero ojo: no son comentarios, son strings multilínea.
"""
Esto NO es un comentario real.
Es una cadena de texto que no se usa.
"""
# Python las ignora solo si no están asignadas a nada, pero técnicamente crea un string
# Resumen: 
# Una línea → #
# Varias líneas → # en cada línea
# Documentación → """ docstring """
# Comentarios tipo /* */ → no existen en Python

    
# - Crea una variable (y una constante si el lenguaje lo soporta).
mi_var = 13
MI_CONST = 3.14  # En Python no hay constantes reales, pero se usa esta convención


# - Crea variables representando todos los tipos de datos primitivos
#   del lenguaje (cadenas de texto, enteros, booleanos...).

# En Python no se habla oficialmente de “primitivos” como en C o Java, pero sí hay un conjunto de tipos básicos integrados (built-in types) que cumplen ese papel. Según la documentación oficial de Python, los fundamentales son estos:
mi_string = "Hola" # str cadenas de texto (unicode)
mi_entero = 42 # int
mi_flotante = 3.14 # float
mi_booleano = True # bool valores lógicos booleano true/false
mi_bytes = b"Hola"          # bytes secuencia inmutable de bytes
mi_bytearray = bytearray(b"Hola")  # bytearray secuencia mutable de bytes
mi_none = None # NoneType valor nulo o ausencia de valor

# - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

print("¡Hola, Python!")