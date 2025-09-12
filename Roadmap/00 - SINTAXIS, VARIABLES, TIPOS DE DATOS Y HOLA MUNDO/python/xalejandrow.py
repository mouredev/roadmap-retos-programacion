'''
 EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del
   lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios
   en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos
   del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
'''

#https://www.python.org/

#one line
'''
mutliple line comments 
in python
'''

#variable
i=100 #integer
text='Hello World' #string

#constantes
CONSTANTE = 10 #por convencion en mayuscula

#tipos de datos en python

#integer
year=2021

#float
pi=3.1416

#boolean
is_boolean= True

#string
text="this is a text variable"
text2='this is a text variable other form'
text_multi_line="""
this is a multiple line
text variable
in python
"""
#null
var_nulo=None
#lists
lista=[1,"dos",3,"cuatro",5]

#tuple
tupla=(1,2,3,4,5)

#conjunto - Set
conjunto={"negro","cyan","magenta","amarillo"}

#diccionary
dicc={
    "nombre":"Juan",
    "edad":40,
    "casado":True,
    "list_hijos":["Maria", "Pedro"],
    "var_tup":(-1,"tres",10,True)
}

#Set


print("¡Hola, Python!")
#Another way
'''lang='Python'
print("¡Hola,", lang ,"!")'''