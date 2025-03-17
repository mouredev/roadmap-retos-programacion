'''
ESTRUCTURA DE DATOS
python ofrece diferentes estructuras que permiten organizar, almacenar y manipular datos de diferentes maneras
'''

#listas

my_list = [1,2,3,"hola", 4.2, True] #se puede almacenar elementos de cualquier tipo se pueden modificar
print(my_list) 

#tuplas
my_tuple = (1,2,3,"adios", 3.2, False) #se puede almanar cualqueir elemento pero no se pueden modificar
print(my_tuple)

#diccionario
#tipo de almacenamieto en par donde se almacena su clave y su valor y se puede modificar
my_dictionary = {"uno" : 1, "dos" : 2, "hello": "hola", "estado": False, "decimal" : 3.2} 
print(my_dictionary)

#conjuntos
#se puede almacenar cualquier valor y modificar pero con elementos unicos y su orden siempre varia
my_set = { 3, 3, 5, 1, 2, 2, "hola", "hola", False, False}
print(my_set)

my_frozenset = frozenset([1, 2, 3, 3, 4, "hello", False]) #esto es un conjunto pero en este cambia que se pueda modificar
print(my_frozenset)

#cadenas

my_string = "esto tambien es una estructura de datos" #secuencia inmutable de caracteres
print(my_string)