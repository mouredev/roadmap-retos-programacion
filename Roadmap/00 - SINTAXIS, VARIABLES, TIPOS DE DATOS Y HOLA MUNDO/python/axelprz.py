""" EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" """
 
#URL del sitio web oficial de Python: https://www.python.org
#Lenguaje seleccionado: Python
#Estos son los distintos tipos de comentarios que existen en Python:

""" Comentarios Inline
Los comentarios inline proporcionan descripciones breves de variables y operaciones sencillas, y se escriben en la misma línea que la sentencia del código: """

x = 0
border = x + 10  # Haz un desplazamiento de 10px.

""" Comentarios Block
Los comentarios block se utilizan para describir la lógica compleja del código. Los comentarios block en Python se construyen de forma similar a los comentarios inline, la única diferencia es que los comentarios block se escriben en una línea aparte: """

#Realizar una suma
x = 15 + 10

""" Comentarios Multilínea
Python no admite de forma nativa los comentarios multilínea, lo que significa que no hay ninguna disposición especial para definirlos. A pesar de ello, a menudo se utilizan comentarios que abarcan varias líneas.

Puedes crear un comentario multilínea a partir de varios comentarios de una sola línea precediendo cada línea con #: """

#Sumar
#Restar
#Multiplicar
#Dividir

""" También puedes utilizar la sintaxis de cadenas multilínea. En Python, puedes definir cadenas de varias líneas encerrándolas entre comillas dobles triples, o comillas simples triples: """

""" 
Este 
String 
es 
Multilínea 
"""

"""Variables y constantes en Python"""

#Variable en Python:
numero = 10

#Constante en Python
NUMERO_DOCUMENTO = 12345678

"""Tipos de variables en Python"""

# Entero
entero = 42

# Punto flotante
flotante = 3.14

# Cadena de texto
cadena = "Hola, mundo!"

# Booleano
booleano = True

# Lista
lista = [1, 2, 3, 4]

# Tupla
tupla = (5, 6, 7, 8)

# Conjunto
conjunto = {9, 10, 11, 12}

# Diccionario
diccionario = {"clave1": "valor1", "clave2": "valor2"}

# None (tipo nulo)
nulo = None

print("¡Hola, Python!")


