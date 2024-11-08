#https://www.python.org/#

#Esto es un comentario de una sola línea#

'''
Esto es un comentario de varias líneas
'''

#Esto es una variable#
x = "Esto es un texto" 
#Esto es una constante#
PI = 3.1416

#Varibles de diferentes tipos de datos primitivos#

# Entero #
entero = 1

# Bolleano #
booleano = True

# Flotante #
flotante = 1.5

# Cadena de texto #
cadena = "Hola mundo"

# Lista #
lista = [1,2,3,4]

# set #
conjunto = {1,2,3,4}

conjunto = set([1,2,3,4])

# Tupla #
tupla = (1,2,3,4)

tupla = tuple((1,2,3,4))

tupla = tuple([1,2,3,4])

tupla = 1,2,3,4

# Diccionario #
diccionario = {
    "nombre": "Juan",
    "edad": 25
}
diccionario = dict(nombre="Juan",
                    edad=25)

diccionario = dict(zip(('nombre', 'edad'), ('Juan', 25)))

# Conjunto congelado #
conjunto_congelado = frozenset([1,2,3,4])

#Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

print("¡Hola, Python!")