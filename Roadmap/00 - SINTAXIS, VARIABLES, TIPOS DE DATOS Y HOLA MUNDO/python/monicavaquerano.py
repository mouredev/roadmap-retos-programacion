# Mónica Vaquerano
# https://monicavaquerano.dev

# EJERCICIO 00:
# Crea un comentario en el código y coloca la URL del sitio web oficial del
# lenguaje de programación que has seleccionado.

# https://www.python.org/


# Representa las diferentes sintaxis que existen de crear comentarios
# en el lenguaje (en una línea, varias...).

# Comentario de una línea

"""
Comentario 
de varias 
líneas usando
comillas simples
"""

"""
Comentario 
de varias 
líneas usando
comillas dobles
"""

# Crea una variable (y una constante si el lenguaje lo soporta).

variable = "Python"
CONSTANTE = 3.14159

# Crea variables representando todos los tipos de datos primitivos
# del lenguaje (cadenas de texto, enteros, booleanos...).

string = "soy una string o cadena de caracteres"
integer = 1
float = 1.5
booleano = True
tuple = (1, 2)
lista = [1, 2, 3, 4, 5, 6]
set = {"Alice", "Bob", "Charlie"}
diccionario = {
    "Alicia": {"edad": 20, "idioma": "español"},
    "Bob": {"edad": 25, "idioma": "inglés"},
}
nada = None
rango = range(9)
complejo = 1j
set_congelado = frozenset({"Alice", "Bob", "Charlie"})
bytes = b"Hello"
byteArray = bytearray(5)
memoryView = memoryview(bytes)


tipos_de_datos = [
    string,
    integer,
    float,
    booleano,
    tuple,
    lista,
    set,
    set_congelado,
    bytes,
    byteArray,
    diccionario,
    nada,
    rango,
    complejo,
    memoryView,
]

print("\tTipos de datos: ")
for dato in tipos_de_datos:
    print("\t", type(dato))
print()


#  Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print(f"¡Hola, {variable}!")
