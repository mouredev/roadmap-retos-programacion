# https://www.python.org/

# Comentario de una linea

"""
Este es un comentario
de múltiples líneas
"""

'''
Este es otro comentario
de múltiples líneas
'''

"""
Nombres de variables en Python
Según la PEP 8 los nombres de las variables de Python deben de escribirse en snake_case. Además en deben de cumplir las siguientes características:

Tienen que empezar por una letra o barra baja.
El uso de keywords como nombres está prohibido.
Los nombres deben de ser descriptivos.
Deben de estar en minúsculas y separando palabras por barras bajas ‘_’.
Las constantes se escriben en mayúsculas y SNAKE_CASE.

Fuente: https://elpythonista.com/variables-python
"""

my_variable = "Esto es una variale"
MY_CONSTANT = "Esto es una constante"

# TIPOS DE DATOS PRIMITIVOS
# Entero (int)
"""
Representa números enteros, positivos o negativos, sin parte fraccionaria.
"""
entero = 10
print(entero)
print(type(entero))

# Flotate (float)
"""
Representa números decimales, es decir, números con parte fraccionaria.
"""
flotante = 3.14
print(flotante)
print(type(flotante))

# Cadena de caracteres (str)
"""
Representa una secuencia de caracteres. Puede contener letras, números, y otros caracteres.
"""
cadena = "¡Hola, Python!"
print(cadena)
print(type(cadena))

# Booleano (bool)
"""
Representa valores de verdad, es decir, True (verdadero) o False (falso).
"""
booleano = True
print(booleano)
print(type(booleano))
booleano = False
print(booleano)
print(type(booleano))

# Numero complejo (complex)
"""
Un número complejo consta de dos partes: la parte real y la parte imaginaria. 
Se expresan en la forma a + bj, donde a es la parte real, b es la parte imaginaria 
y j es la unidad imaginaria (que es la raíz cuadrada de -1).
"""
complejo = 1 + 2j
print(complejo)
print(type(complejo))

# NoneType
"""
El tipo de dato None representa la ausencia de un valor o la falta de un objeto. 
Se utiliza comúnmente para indicar que una variable no tiene un valor asignado.
"""
nulo = None
print(nulo)
print(type(nulo))

# Lista (list)
"""
Representa una secuencia mutable de elementos. 
Puedes modificar, añadir o eliminar elementos de una lista.
"""
lista = [1, 2, 3]
print(lista)
print(type(lista))

# Tupla (tuple)
"""
Similar a una lista, pero es inmutable, lo que significa que 
no puedes modificar su contenido después de crearla.
"""
tupla = (4, 5, 6)
print(tupla)
print(type(tupla))

# Conjunto (set)
"""
Representa una colección desordenada de elementos únicos. No permite elementos duplicados.
"""
conjunto = {7, 8, 9}
print(conjunto)
print(type(conjunto))

# Diccionario (dict)
"""
Representa una colección de pares clave-valor. Cada valor está asociado con una clave única.
"""
diccionario = {"a": 1, "b": 2, "c": 3}
print(diccionario)
print(type(diccionario))

print("¡Hola, Python!")
