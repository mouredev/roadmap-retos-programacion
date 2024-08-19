'''Reto #00 Sintaxsis, variables y tipos de datos
EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"'''


'https://www.python.org'

#Este es un comentario en python creado con el simbolo de numeral
'''Este es un comentario en python creado con comillas simples'''
'''Este es un parrafo 
   comentado con comillas
   simples'''

#Creación de una variable

numero = 5

#otra forma de hacerlo

fila, columna = 4,5

#Creación de una constante

'''Python no soporta la creación de constantes,
   por lo tanto, por convención, para crear
   constantes se declara una variable
   con su nombre en mayuscula para
   indicar que no se debe modificar'''

CONSTANTE = 5

#otra forma de hacerlo

NUMERO_1, NUMERO_2 = 1,2

#Tipos de datos primitivos en python

#String (str)

string = "Hola mundo"

#Entero (int)

integer = 5

#Flotante o decimal (float)

float = 3.7

#Booleanos (bool)

true = True
false = False

#NoneType

variable = None

#Imprimimos en el terminal

print("¡Hola, Python!")