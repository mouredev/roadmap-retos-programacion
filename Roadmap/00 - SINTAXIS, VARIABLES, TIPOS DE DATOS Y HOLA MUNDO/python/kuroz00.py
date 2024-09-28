"""
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

#https://www.python.org/

#comentario de una linea

"""
comentario de 
varias
lineas
"""

'''
comentario de varias lineas
pero con comillas simples
'''

#variable y constante 

caja1 = 10

felicidad = "python"

#tipos de datos primitivos

numero_numeroEntero = 25
numero_flotante = 25,5
numero_complejo = 1j #complex
lista_list = ["manzana", "platano", "naranja"]
lista_tuple = ("manzana", "platano", "naranja")
rango_range = range(25)
list_frozenSet = {{"manzana", "platano", "naranja"}}
cadenaDeTexto = "hola, desea comer un pie de limon?"
valorBooleano = True

#Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!

print("Hola,", felicidad,"!")