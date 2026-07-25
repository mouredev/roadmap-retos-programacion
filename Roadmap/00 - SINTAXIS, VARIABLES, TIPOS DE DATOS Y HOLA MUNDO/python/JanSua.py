# https://www.python.org/

# Comentario de una línea
"""
Comentario de
varias líneas
"""

"Creación de variables y cte"
a = None
PI_CONST = 3.141592359
b = 10
d = 'a'
e = 'Hola'
f = True
_ = "Temporal"
g = ("Tupla", "Inmutable", 123)
h = ["Lista", "Mutable", 456]
i = {"Llave1":"Diccionario",
     "Llave2":"Mutable en valores",
     "Llave3":"Inmutable en llave",
     "Llavex":1928}
# En Python todo son objetos, por lo que puedo definir hasta funciones, clases y objetos a "variables"

class P():
    pass
p_var = P
any_object = p_var() # Creé un objeto de la clase P, utilizando la variable p_var de tipo clase P.
lang_name = "Python"
print(f"Hola, {lang_name}")

