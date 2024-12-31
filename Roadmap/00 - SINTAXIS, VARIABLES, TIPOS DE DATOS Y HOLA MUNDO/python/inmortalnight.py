# www.python.org

# Comentario en una línea
'''Comentario en """varias""" líneas'''
"""Comentario en '''varias''' líneas"""

# variable, sin constantes pero se puede declarar asi
CONSTANT = "string" 

# tipos de datos
nulo = None #no tiene valor
string = "hi"
entero = 2
entero: int = 2  # Anotación de tipo int
entero = int(2)    # Conversión a entero
float = 3.4
complex = 4j    # Número complejo
boolean = False
range = range(6) #rango
byte = b"Python"
byteArray = bytearray(byte)     # Secuencia de bytes modificable
memoryview = memoryview(byteArray)  # Secuencia de bytes que permite el acceso a la memoria
list = [1, 2, 3, ".", [1,2]]   # Lista que puede ser modificada y contiene elementos de diferentes tipos
tuple = (1, 2, 3)  # Tupla que no puede ser modificada y contiene elementos de diferentes tipos
set = {1, 2, 3}     # Conjunto que no puede contener elementos duplicados y no tiene orden
set_congelado = ({1, 2, 3}) #no se puede modificar y no tiene orden
dictionary = {"key1": 1, "key2": "dos", "key3":[1,2]}  # Diccionario que contiene pares clave-valor

#imprimir
print("¡Hola, Python!")
print(f"Número {entero}")
print("Número" + entero)
print("¡Hola, {}!".format("mundo")) #format, insertar
model = '¡Hola, {0:s}!' #format, restriccion de tipo y indice
print = model.format("string")

print(float(1)) #cambiar a float
print(int(3.4)) #cambiar a entero
print(bool(1)) #cambiar a booleano
print(type(entero)) #tipo de dato

# Objetos
class Type(): #definir una clase
    pass
object = Type() #instanciar un objeto