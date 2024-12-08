#https://www.python.org/

#Esto es un comentario de una sola línea

"""
Esto es un comentario 
de varias líneas
"""
#Python no tiene un delimitador especifico para comentarios en multiples lineas,
#por lo que se usan comillas triples, que funcionan como cadenas de texto no asignadas a una variable
'''
Esto tambien es un 
comentario de 
varias lineas
'''

nueva_variable = "nueva variable"
variable1 = 10
precio_con_impuesto = 19.90

CONSTANTE1 = "Constante 1"     #por convencion porque python no tiene constantes
MI_CONSTANTE_1= "100" 
PI = 3.1416

#Tipos de datos numéricos
dato_int = 10
dato_float = 3.1416
dato_complex = 2 + 3j
#Tipos de datos booleanos
dato_bool = True
dato_bool = False
#Tipos de datos secuenciales
dato_str = "nueva cadena de texto" #cadenas de caracteres
otro_dato_str = 'segunda cadena de texto'
dato_list = [1,2,3,"cuatro"]  #lista, colección ordenada y mutable de elementos
dato_tuple = (1,2,3,"cuatro") #coleccion ordenada e inmutable de elementos
dato_range = range(0,10) #secuencias de numeros enteros, comunmente usadas en bucles
#Tipos de datos conjuntos
dato_set = {1,2,3,4} #conjuntos, colección desordenadande elementos unicos
dato_frozenset = frozenset([1,2,3,4]) #conjuntos inmutables
#Tipos de dato de mapeo
dato_dict = {"clave": "valor", "edad": 25} #diccionarios, una colección desordenada de pares clave-valor
#Tipos de dato binario
dato_bytes = b"hola" #secuencia inmutable de enteros en el rango de 0 a 255
dato_bytearray = bytearray(b"hola") #secuencia mutable de enteros en el rango de 0 a 255
dato_memoryview = memoryview(b"hola") #un objeto que puede acceder a los datos subyacentes de un objeto binario sin copiarlo

#Tipo Especial
dato_NoneType = None #representa el valor none, es decir, la ausencia de valor

print("¡Hola, Python!")


