# sitio web oficial de Python: https://www.python.org/ fuente sobre uso de comentarios y docstrings: https://peps.python.org/pep-0008/


# Sintaxis de comentarios:

# *Comentario de una linea (uso comun y recomendado para todo el codigo)

# Este es un comentario de varias líneas
# utilizando el símbolo de almohadilla
# en cada línea.

""" 
*Docstring segun lo que investigue su uso 
principal es para documentaciondentro del 
contexto de: funciones, métodos, clases
y módulos.
"""

'''
tambien pueden escribirse con comillas 
simples aparte de las dobles, no se 
recomienda para simples comentarios ya 
que las docstrings se almacenan como 
parte de los atributos del objeto y 
pueden ser accesibles en tiempo 
de ejecución, lo que no ocurre 
con los comentarios regulares.
'''

mi_variable = "las variables almacenan datos que pueden ser manipulados"

MI_CONSTANTE = 299792458

mi_entero = 11

mi_flotante = 99.99

mi_cadena = "¡Hola, Python!"

mi_booleano = False

mi_none = None

print(mi_cadena)



