#1. 

# https://www.python.org/

#2.

# Comentario en una linea


# Comentarios en varias lineas
"""
Se puede con
3 comillas dobles
para abrir y cerrar
"""

'''
También se
puede con 
comillas simples
'''

#3.

#Variables
my_variable = "Mi variable"
my_variable = "Nuevo valor de mi variable"

#Constantes
MY_CONSTANT = "Mi constante" # Por convención los constantes se escriben en mayúsculas para diferenciarlas de las variables y asi evitar que modifiquemos su valor accidentalmente.


#4.

#INTEGER
my_int: int = 26 # Indicamos el tipo de dato para evitar que se ingrese otro tipo de dato en la variable y evitar casos como este: 
# my_int = "8" -- Esto no debería ser posible si hemos indicado que my_int es de tipo entero.

#FLOAT
my_float = 2.6

#BOOLEAN
my_bool = True
my_bool = False

#STRING
my_string = "Mi cadena de texto"
my_other_string = 'Mi otra cadena de texto'

#5

print("¡Hola, python!")


#PLUS - DETERMINAR EL TIPO DE DATO QUE ESTAMOS REPRESENTANDO

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))