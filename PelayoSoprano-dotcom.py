#https://www.python.org

#Tipos de comentarios

#Comentarios en una linea -> https://www.python.org

"""
Esto es 
un comentario 
en varias lineas
"""

#declarando variables
my_variable = "Mi variable"
my_variable = "Nuevo valor de mi variable"

MY_CONSTANT = "Mi constante" # por convencion

#declarando variables primitivas

my_int = 10
my_float = 10.5
my_bool = True
my_string = "Hola, mundo!"
my_other_string = 'Hola, mundo!'

#declarando variables primitivas de manera explicita

my_int: int = 10
my_float: float = 10.5
my_bool: bool = False    
my_string: str = "Hola, mundo!"
my_other_string: str = 'Hola, mundo!'

print("!Hola, python!") #syntaxis para imprimir en consola

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
print(type(my_other_string))