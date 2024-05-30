"""
EJERCICIO #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO:

- Crea un comentario en el código y coloca la URL del sitio web oficial del
  lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
  en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
  del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

#Url: https://www.python.org


"""
Para crear un comentario de una sola linea se puede hacer con (#) 
poniendo ese signo antes de la linea que se desea comentar:
"""

# Ejemplo de comentario de una sola linea.

"""
Para comentar mas de una linea de codigo con python se tiene que untilizar 
el signo de las comillas pueden ser simples o dobles se tinen que repetir 
3 veces al inicio y al final de las lineas que se desean comentar:
"""

"""
Ejemplo de comentario
de mas de una linea.
"""

""" 
Para deifinir una varible en python solo tenemos que iniciar nombrando la variable y 
definir su valor despues de un signo igual:
"""

Variable_ejemplo = 1

"""
No se puede definir una constante en python pero es una convencción el nombrar una 
variable solo con mayusculas para establecer que no se debe modificar el valor de dicha variable:
"""

CONSTANTE_EJEMPLO = 2

"""
Estos son los tipos de datos primitivos que se pueden manejar con python:
"""

Integers = 1 # Integers o Int son tipos de datos primitivos numericos enteros.
print(type(Integers))

Floats = 0.5 # Floats son tipos de datos primitivos numericos decimales.
print(type(Floats))

Boolanos = True # Booleanos son tipos de datos primitivos cuyo valor es (0 o 1) o (True or False).
print(type(Boolanos))

Strings = "Cadenas" # Strings son tipos de datos primitivos de valor alfabetico son cadenas de texto.
print(type(Strings))

"""
El comando print siver para imprimir un mensaje o valor en la terminal "Fin".
"""

print("Hola, Python!")
