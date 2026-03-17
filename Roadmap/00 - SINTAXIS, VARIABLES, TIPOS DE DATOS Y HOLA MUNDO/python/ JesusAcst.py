# Comentario en una línea

"""
Comentario en varias líneas
"""

# https://www.python.org/

# -----------------------------
# Variables
# -----------------------------
lenguaje = "Python"
saludo = "¡Hola, "
signo = "!"

# Concatenación
mensaje = saludo + lenguaje + signo

my_int = 3
my_float = 1.0
my_bool = True

# -----------------------------
# Constantes
# -----------------------------
MY_CONSTANT = "Este es un valor constante"

# -----------------------------
# Funciones
# -----------------------------
def suma(a, b):
    """
    Esta función recibe dos números
    y retorna su suma.
    """
    return a + b

# -----------------------------
# Salida por consola
# -----------------------------
print(mensaje)
print("La suma es:", suma(1, 2))

# -----------------------------
# Tipos de datos
# -----------------------------
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(lenguaje))
print(type(MY_CONSTANT))
print(type(suma))

# -----------------------------
# Documentación de la función
# -----------------------------
print(suma.__doc__)
