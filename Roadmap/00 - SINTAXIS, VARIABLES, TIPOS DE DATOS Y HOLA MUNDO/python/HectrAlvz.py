# https://python.org/
# https://peps.python.org/pep-0008/


# Sintaxis que existen para crear comentarios:

# Comentarios de una sola línea (usando #)

# Comentario de Multiples líneas, cada uno...
# se considera un comentario de una sola línea

# Los siguientes comentarios se utilizan habitualmente para los docstrings:
# - Para documentar módulos, clases, métodos y funciones.
# - Su propósito principal es proporcionar una descripción clara sobre
#   el funcionamiento y el uso del código (o comentarlo por completo).

"""
Este es un comentario 
de varias líneas,
o de bloque
"""

'''
Otra forma de
hacer comentarios
varias líneas,
o de bloque
'''

# Otra forma que no es considerada como tal un comentario son:
# - Las cadenas de texto que no estén asignadas a una variable
#   ni se utiliza son ignoradas por python:

" Comentarios de una sola línea (cadena de texto)"
' Comentarios de una sola línea (otra forma)'

# NOTE: Etiquetas en Comentarios
# Las etiquetas en comentarios son una práctica común para organizar y documentar el código.
# Nos ayudan a identificar tareas pendientes, problemas o mejoras.

# TODO: Se utiliza para indicar una tarea pendiente o una funcionalidad que falta implementar.
# Esto sirve como recordatorio para completar una tarea en el futuro.

# FIXME: Se utiliza para marcar un problema en el código que necesita ser corregido.
# Esto indica que hay un error o un comportamiento inesperado que debe ser revisado.

# Otras etiquetas comunes:
# NOTE: Para resaltar información importante o explicaciones adicionales.
# HACK: Para indicar soluciones temporales o poco elegantes que deben mejorarse.
# WARNING: Para advertir sobre posibles problemas o comportamientos riesgosos.


# Variable (y una constante si el lenguaje lo soporta).
my_variable = "Esto es una Variable"
CONSTANTE = "Esto es una constante. Por convención, se escribe en mayúscula."

# Tipos de Datos Primitivos
# No es necesario colocar type hints (anotaciones de tipo) para declarar variables,
# ya que Python es un lenguaje de tipado dinámico.

# Enteros: Número Entero
mi_int: int = 1234567890
# mi_int = 1234567890 # sin type hint
# Decimales: Número Real
mi_float: float = 1.23
# Boléanos: Lógico
mi_bool: bool = True # True / False
# String: sCadena de Texto
mi_str_1: str = "String comillas dobles"
mi_str_2: str = 'String comillas simples'
mi_char = "A" # "char" se representa como str de 1 carácter
# NoneType: Ausencia de valor
mi_NoneType: None = None
# Bytes: Secuencia de bytes (0-255)
mi_bytes_1: bytes = b"\x48\x6f\x6c\x61" # Hola
mi_bytes_2: bytes = b'abc'
# Complejos: Números complejos (parte real + imaginaria)
mi_complejo: complex = 3 + 4j

print(type(mi_int), mi_int)
print(type(mi_float), mi_float)
print(type(mi_bool), mi_bool)
print(type(mi_str_1), mi_str_1)
print(type(mi_str_2), mi_str_2)
print(type(mi_char), mi_char)
print(type(mi_NoneType), mi_NoneType)
print(type(mi_bytes_1), mi_bytes_1)
print(type(mi_bytes_2), mi_bytes_2)
print(type(mi_complejo), mi_complejo)

print("\n¡Hola, Python!")
