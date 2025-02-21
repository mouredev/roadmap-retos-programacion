# https://www.python.org/

# Comentario de una línea.

"""
Esto es un 
comentario en 
varias líneas.
"""

'''
Esto también es un 
comentario en
varias líneas.
'''

mi_lenguaje = "Python"  # Varialbe string
mi_entero = 50  # Variable int
mi_decimales = 3.5  # Variable float
es_verdadero = True  # Varialbe bool

print(f"\nmi_lenguaje = \"Python\" --> {type(mi_lenguaje)}")
print(f"mi_entero = 50 --> {type(mi_entero)}")
print(f"mi_decimales = 3.5 --> {type(mi_decimales)}")
print(f"es_verdadero = True --> {type(es_verdadero)}\n")

"""
Las constantes no existen en Python como tal. Sin embargo, por convención, 
se utilizan variables en mayúsculas para indicar que una variable debe ser 
tratada como una constante y no debe ser modificada.
"""
NUMERO_PI = 3.1416


print("¡Hola, Python!")
