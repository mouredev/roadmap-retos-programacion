"""
EJERCICIO:
1) Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
2) Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
3) Crea una variable (y una constante si el lenguaje lo soporta).
4) Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

# 1) https://www.python.org/

# 2) Comentario de una linea y varias

"""
Comentario de varias lineas
"""

''' 
Otro comentario de varias lineas
'''

# 3) variable y constante
variable = "texto"
CONSTANTE = "texto constante"

# 4) Tipos de variables primitivas https://docs.python.org/es/3/library/stdtypes.html    
# Los nombre:int= 123 son anotaciones para especificar el tipo de una variable es opcional.
# Tipos numericos, int,float,complex
numero:int = 123
flotante:float = 3.1416
complejo:complex = 3j

# Tipos boleanos
verdadero:bool = True
falso:bool = False

# Tipos secuencia, list,tuple, range
lista:list = [1,2,3,4,4,4]
tupla:tuple = (1,2,3,4)
rangos = list(range(10))

# Tipo de dato string
texto:str = "string"
texto1,texto2 = "str",'str'
texto_multilinea:str = """
Texto multilinea en python
"""
# Tipo de dato bytes
byte = b'valor binario' 

# Tipo de dato set frozenset y dict
conjunto:set = {1,2,3}
conjunto_inmutable:frozenset = {1,2,3,4}
dicionario:dict = {"one":1,"two":2,"three":3}

# Tipo de dato NULL o None
null = None

# 5) print() hola Python
print("¡Hola, Python!")