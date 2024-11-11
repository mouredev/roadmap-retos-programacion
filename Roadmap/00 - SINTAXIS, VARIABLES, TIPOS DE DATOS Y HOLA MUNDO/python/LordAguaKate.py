#Creacion de SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

#Sintaxis
'''
La sintaxis es nada mas y nada menos que el lenguaje de programacion,
que hace el conjunto de reglas que define las combinaciones de simbolos que
se consideran declaraciones o expresiones validas en ese lenguaje.
'''
#Ejemplos
x = 0
print("hola soy una sintaxis")
x < 0
2 + 3
numeros = [0, 1, 2, 3, 4, 5]
#Comentarios para una sola linea
''' comentarios para multiples lineas'''


#Varaibles
'''
Las variables son elementos de un lenguaje de programacion que tiene asignado un valor unico, 
el cual puede se puede asignar, manipular y reutilizar. Para crear una variable se necesita
el nombre de la variable asignar un valor usando = y el valor en si.
'''
#Ejemplos
#Variable normal
numero = 12
nombre = "LordAguaKate"
frio = True
#Variable con asignacion multiple
codigo = 9999
codigo2 = codigo
'''
Nota: hay que tener en cuenta que en python las variables pueden tener cualquier longitud y
pueden consistir en letras mayusculas y minusculas (A-Z, a-z), digitos (0-9) y el caracter
de subrayado(_)
'''
#Ejemplos
_variable = "Esto es correcto"
vAriable = "Esto es correcto"
variabel_2 = "Esto es correcto"

# variable$ = "Esto es incorrecto"
# 1variable = "Esto es incorrecto"


#Tipos de datos
'''
Los tipos de datos vienen de la mano con el interprete, los tipos de datos que existen
son : Integers(int), Floats (float), Strings (str), Booleanos (bool), Listas (list),
Tuplas (tuple), Diccionarios (dict), Conjuntos (set)
'''
#Ejemplo
#Integers (int)  Números enteros, como 1, 2, 3, etc.
integers = 3
#Floats (float)  Números con decimales, como 3.14 o -0.5.
floats = 9.99
#Strings (str): Cadenas de texto, como “hola” o ‘adiós’.
strings = "Con comilla doble"
strings2 = 'Con comilla simple'
#Booleanos (bool): Valores lógicos que pueden ser True o False.
booleanos = True
booleanos2 = False
#Listas (list): Conjuntos ordenados y modificables de elementos, como [1, 2, 3] o [“a”, “b”, “c”].
listas = ["Esto es", "una lista", 10]
#Tuplas (tuple): Conjuntos ordenados e inmutables de elementos, como (1, 2, 3) o (“a”, “b”, “c”).
tuplas = ("Esto es", "una tupla", 10)
#Diccionarios (dict): Colecciones no ordenadas de pares clave-valor, como {“nombre”: “Juan”, “edad”: 30}.
diccionario = {
    "nombre": "lordaguakate",
    "GitHub": "LordAguaKate",
    "Edad": 24
}
#Conjuntos (set): Conjuntos no ordenados y sin elementos duplicados, como {1, 2, 3} o {“a”, “b”, “c”}.
conjuntos = {1,2,3,"Esto es un conjunto"}


#Hola mundo
saludo = "Hola mundo"
saludo2 = saludo
print(saludo)
print(saludo2)
print("Hola mundo")
print('Hola mundo')


