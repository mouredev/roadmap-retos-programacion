#* EJERCICIO:
# * - Crea un comentario en el código y coloca la URL del sitio web oficial del
#*   lenguaje de programación que has seleccionado. ---
#* - Representa las diferentes sintaxis que existen de crear comentarios
#*   en el lenguaje (en una línea, varias...). ---
#* - Crea una variable (y una constante si el lenguaje lo soporta). ---
#* - Crea variables representando todos los tipos de datos primitivos
#*   del lenguaje (cadenas de texto, enteros, booleanos...). 
#* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
#*
#* ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
#* debemos comenzar por el principio.

#----------------------- Solución

#1---
#Crea un comentario en el código y coloca la URL del sitio web oficial del
#lenguaje de programación que has seleccionado. ---

# * Comentario sitio web oficial de python:
#   sitio web python: https://www.python.org/

#2---
#Representa las diferentes sintaxis que existen de crear comentarios
#*   en el lenguaje (en una línea, varias...)

#Con el "#" podemos crear comentarios que el interprete obveará, también se puede
# utilizar para comentar el código

"""
Forma para crear
comentarios en multiples lineas de código.
3 comillas dobles.
Funciona para comentar también
python ignora esto al no estar asignado a algún tipo de variable
utilizamos comillas '' simples

"""
'''
Casi similar a lo anterior, pero en este caso utilizamos comillas dobles
"hola mundo"

'''

#3---
#Crea una variable (y una constante si el lenguaje lo soporta)

#El valor de la variable es suceptible a cambio
variable= input("Inserte el valor de la variable: ")#Directamente pido al usuario un valor aleatorio

constant= 23 #Un valor constante, permanece.

#4---
#Crea variables representando todos los tipos de datos primitivos
#del lenguaje (cadenas de texto, enteros, booleanos...)
#Cabe aclarar que los tipos de datos primitivos son cuatro: 
# int(enteros), floats(flotantes), booleanos y strings(cadenas)

#tipo de dato entero
data_type_int= 23
age= data_type_int #edad es un tipo de dato entero.


#tipo de dato flotante
data_type_float= 2.5

#el f-string imprime multiples variables en cadena de texto.
temperature= f"La temperatura es de; {data_type_float} C" #f-string permite incluir cadenas con datos 
print(temperature) 

#booleanos
#True & False
verdadero= True
falso= False #Siempre en mayúsculas


#Cadenas - Strings
str= """

Str de Multiples líneas, se realiza con 'tres' comillas 'dobles'.

"""
print(str)

str= '''

Str de múltiples líneas realizado con "tres" comillas "dobles".

'''
print(str)

str= "Comillas 'dobles' utilizadas 'una' sola vez, comentario para una sola línea"
print(str)

#5---
#Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

print("¡Hola, Python!")
