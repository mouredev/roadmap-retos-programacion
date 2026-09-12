#Hola comunidad, el lenguaje que elegí es Python. Este es su Sitio web: https://www.python.org/ 
#Podemos dejar un comentario de esta forma, con el simbolo de numeral al inicio de la linea.
"""
Esto no es técnicamente un comentario.
Es un string multilínea y puede utilizarse
para documentar el código.

"""
print("Hola mundo, soy Salvador Villa y estoy aprendiendo Python")

#variable 

palabra = "Hola mundo"
#constante 
PI = 3.1416

#tipos de datos

#string 
d_saludo = "Buenas tardes"

#numericos
d_numero = 20
d_decimal = 3.14
d_numero_complejo = 3 + 4j

#secuencias 
d_lista = [1, 2, 3, 4, 5] #Se puede modificiar
d_tupla = ("verde", "rojo", "azul") #no se puede modificar
d_rango = range(3)

#mapeo
d_dict = {"name":"salva", 
        "age": 25,
        "lastname": "andrada"}

#establecer
d_set = set({"futbol", "basquetbol", "tenis"}) #conjunto modifiacable  
d_fronzenset = frozenset({"futbol", "basquetbol", "tenis"}) #conjunto inmodificable

#booleano 
d_verdadero = True    
d_falso = False

#binarios
d_bytes = b"Hola comunidad" #no se puede modificar
d_bytearray = bytearray(b"Hola comunidad")  #se puede modificar
d_memoryview = memoryview(d_bytearray) #permite acceder a los datos sin copiarlo

#ninguno
d_nada = None

#impresion de todos los tipos
print("Tipo de dato string: ", d_saludo)
print("Tipo de dato numerico: ", d_numero)
print("Tipo de dato decimal: ", d_decimal)
print("Tipo de dato complejo: ", d_numero_complejo)
print("Tipo de dato lista: ", d_lista)
print("Tipo de dato tupla: ", d_tupla)
print("Tipo de dato rango: ", d_rango)
print("Tipo de dato diccionario: ", d_dict)
print("Tipo de dato conjunto: ", d_set)
print("Tipo de dato conjunto inmodificable: ", d_fronzenset)
print("Tipo de dato booleano: ", d_verdadero)
print("Tipo de dato booleano: ", d_falso)
print("Tipo de dato bytes: ", d_bytes)
print("Tipo de dato bytearray: ", d_bytearray)
print("Tipo de dato memoryview: ", d_memoryview)
print("Tipo de dato none: ", d_nada)

print("¡Hola, python!")