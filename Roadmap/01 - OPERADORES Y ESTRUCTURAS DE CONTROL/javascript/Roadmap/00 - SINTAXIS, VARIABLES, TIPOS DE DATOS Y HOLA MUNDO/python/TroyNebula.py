#!/usr/bin/env python

# - Crea un comentario en el cOdigo y coloca la URL del sitio web oficial del lenguaje seleccionado.
# https://www.python.org/


#  - Representa las diferentes sintaxis que existen de crear comentarios
# Este es un comentario habitual que tambien puede ir tras una linea de codigo

"""Este es un comentario
de mas de una linea.

Puedo dejar lineas vacias tambien
"""

'''Este es otro comentario
de mas de una linea.'''


# - Variable
variable=1
# - Constante: 
"""En Python las constantes no existen. 
Para guardar un valor constante se utiliza una variable pero, como buena practica, 
se utilizan las letras mayusculas para darle nombre a dicha variable. 
Asi, si al programar nos encontramos con un identificador en mayusculas 
sabremos que no debe ser alterado"""
CONSTANTE=10


# - Crea variables representando todos los tipos de datos primitivos
entero:int = 0  # anotacion de tipo 
entero= 0  # declaracion simple de variable
texto:str = "string"
booleana:bool = True  # o False
decimal:float = 0.5
lista = [1, 2, 3]  # conjunto ordenado de valores dinamico que permiten un amplio manejo de los valores
tupla = (4, 5, 6)  # conjunto ordenado de valores estatico
diccionario = {'a': 1, 'b': 2}  #claves/valores, se ordenan y son mutables, pero solo permiten entradas unicas no duplicadas
conjunto = {7, 8, 9}  # set/coleccion no ordenada de objetos unicos, pueden ser de diversos tipos objetos mutables como listas, diccionarios, e incluso otros conjuntos
none = None # Especial data type que no tiene valor
complejo:complex = 4+5j # datos complejos
''' Ver lista entera en: https://docs.python.org/3/reference/datamodel.html#set-types'''


# - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print ("¡Hola, Python! 🐍")