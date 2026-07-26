 #*   EJERCICIO:
 #* 1 Crea un comentario en el código y coloca la URL del sitio web oficial del
 #*   lenguaje de programación que has seleccionado.
 #* 2 Representa las diferentes sintaxis que existen de crear comentarios
 #*   en el lenguaje (en una línea, varias...).
 #* 3 Crea una variable (y una constante si el lenguaje lo soporta).
 #* 4 Crea variables representando todos los tipos de datos primitivos
 #*   del lenguaje (cadenas de texto, enteros, booleanos...).
 #* 5 Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

#Respuesta:
#1 Sitio web oficial de Python: https://www.python.org/

#2 Comentarios:

#Comentario en una sola línea

"""
   Esto es un comentario de varias líneas de python, también conocido como docstring.
   Se utiliza para documentar el código y explicar su funcionamiento y tambien no tire errores de sintaxis 
   al escribir varias líneas de texto. 
"""

'''Este es otro comentario de varias líneas, al igual que comillas dobles'''

#3 Crear una variable y una constante:

variable = "Esta es una variable"
variable: str = "Esta es una variable con tipo de dato especificado"
CONSTANTE: str = "Esta no es una constante, pero se suele escribir en mayúscula para indicar que no debe ser modificada."

#4 Tipos de datos:

Cadenas_de_texto: str = "Hola, mundo" #Strings
Enteros: int = 42 #Integers(Numeros enteros)
Flotantes: float = 3.14 #Floats(Numeros decimales)
Booleanos: bool = True #Booleans(Valores lógicos, Verdadero o Falso)
Nulos: None = None #NoneType(Valores nulos)

#5 Imprimir por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

print("Hola, Python!")