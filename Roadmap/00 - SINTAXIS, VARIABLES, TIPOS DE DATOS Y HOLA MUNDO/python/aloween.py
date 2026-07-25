#https://www.python.org/
#comentario en una linea
"""
comentario en varias lineas
Hola
Mundo 

''''
mas lineas """

'''
#crear variables
# en python no existe el concepto de constantes, pero en la comunidad se representan declarando una variable en mayusculas'''

mi_variable= "mi nombre es Alonso"

MY_CONSTANT = "No cambiar el valor de una constante"

# Existen 4 tipos de datos primitivos!!! 
my_int: int  = 10 # int es un numero entero ( podemos usar type hints para indicar el tipo de dato)
my_float: float = 2.5 # float es un numero decimal
my_oolean = True # boolean es un valor logico (True o False)
my_none = None # none es un valor nulo o ausencia de valor 
my_string = "Hola Mundo" # string es una cadena de texto y podemos usar comillas simples o dobles.  
print("Hola " + mi_variable)
print("Hola " + "https://www.python.org/")

print(type(my_int))
print(type(mi_variable))
print(type(my_float))