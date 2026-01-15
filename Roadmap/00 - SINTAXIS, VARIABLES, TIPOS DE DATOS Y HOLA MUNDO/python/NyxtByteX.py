# https://www.python.org

# Comentario en una línea

"""
Esto también es 
un comentario
en varias líneas
"""

'''
Esto también es 
un comentario
en varias líneas
'''

#¿Qué es una variable?
# Una variable es un nombre que guarda un valor en memoria.
my_variable = "Mi variable"
my_variable = "Nuevo valor de mi variable"

# Las constantes se escriben en MAYÚSCULAS por convención,
# aunque técnicamente sí se puede cambiar.
MY_CONSTANT = "Mi constante" # por convención

# Tipos de datos básicos en Python
my_int = 1 # int (entero)
my_float = 1.5 # float (decimal)
my_bool = True # bool (booleano)
my_bool = False # bool (booleano)
my_string = "Mi cadena de texto"  # str (cadena de texto)
my_other_string = 'Mi otra cadena de texto' 

# Puedes usar type() para saber el tipo de dato
print(type(my_int))  # <class 'int'>

# Imprimir mensaje en consola
print("¡Hola, Python!")

# Saber el tipo de dato
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
print(type(my_other_string))

# Concatenar texto con variables (cómo imprimir valores)
nombre = "Ana"
print("Hola " + nombre)

# Mejor forma: f-string
print(f"Hola {nombre}")
