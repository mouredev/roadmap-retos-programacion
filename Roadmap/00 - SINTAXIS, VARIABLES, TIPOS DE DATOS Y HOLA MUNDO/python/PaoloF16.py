# Desarrollo del Ejercicio
#https://www.python.org/

# Para comentario de una sola linea se usa el "#"


"""
Las triples comillas simples se usan para
escribir texto em multiples lineas 
"""


''' 
Esta tambien es una linea de texto 
en multilinea solo con comillas simples 
'''

#Variables 
#¿Cómo nombrar variables?
"""
Las variables en Python pueden ser nombradas de la siguiente manera:
1. No pueden comenzar con números
2. No pueden contener espacios en blanco
3. No pueden contener caracteres especiales
4. No pueden ser iguales a palabras reservadas de Python
"""
#Por convención se recomienda utiizar snake case para nombrar variables. Esta utiliza guión bajo para separar palabras.
#Además se recomienda que el nombre sea fácil de comprender:
#Ejemplo de variable con snake case
my_user = "Paolo"
MY_CONSTANT = "12"


'''
Python admite diferentes tipos de variables sean numericas o textuales dentro de tipo de datos numericos tenemos a enteros (int) flotante
(float) o complejos (complex) que se pueden combinar mediante operadores, una parte es real y una parte es imaginaria
'''
# Ejemplos de variables numericos 
 # Enteros o int 
my_int = 3

 # Flotantes o float
my_float = 3,5
 # Complejos o complex
my_complex = 3 + 5j

#Datos booleanos 
#Se representa por verdadero o falso

my_bool = True
my_bool = False

#Strings

my_string = "My first line"
my_new_string = "My second line"


print("Hola Python")
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
print(type(my_new_string))

