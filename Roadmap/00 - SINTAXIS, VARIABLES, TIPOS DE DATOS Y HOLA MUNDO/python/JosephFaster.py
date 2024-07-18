#Existen diversas maneras de poner comentarios en Python como los siguientes:

#https://www.python.org/

"""
Esto tambien es 
un comentario
de varias lineas de texto
"""

'''Tambien se pueden usar comidas simples
y no pasa nada, no afecta al código'''

my_variable = 'Mi variable'
my_variable = 'Nuevo valor de mi variable'

"""Python no tiene constantes"""

MY_CONSTANT = 'Mi constante' #Por convención se utilizan las constantes en mayusculas y las variables con formato snake_case
MY_CONSTANT = 'LE PUEDO CAMBIAR EL VALOR POR QUE NO HAY CONSTANTES'

#Python tiene 4 tipo de datos primitivos
#De esta manera se ve puede especificar que a esa variable solo se le pone el tipo de datos que le antepones en la etiqueta
my_int: int = 1
my_float: float = 2.3
my_boolean: bool = True
my_bool: bool = False
my_string: str = 'hola mundo'

print(my_string)


print(type(my_int))
print(type(my_float))
print(type(my_boolean))
print(type(my_string))
