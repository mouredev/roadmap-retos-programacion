'''
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
'''

# https://python.org

"""
Comentario de 
varias líneas
"""

'''
Comentario de
varias líneas
'''

variable = "Buenos días"
variable = "Estoy aprendiendo Python. Y aprendiendo / recordando lógica. Deséame éxito."

CONSTANTE = "Que le vaya bien" # Las constantes se suelen poner en mayúsculas, eso no lo vuelve una constante como tal. No hay constantes en Python, todas son variables.

# Datos primitivos:

mi_entero = 1 # Si quiero especificar que es un entero, escribo "mi_entero: int = 1" 
mi_flotante = 1.5 # float
mi_booleano = True # bool
mi_booleano = False # bool
mi_string = "Una cadena de texto" # str
mi_otra_string = 'Una cadena de texto con comilla simple, se abre y se cierra igual' # igual, str 

print("¡Hola, Python!")

print(type(mi_entero))
print(type(mi_flotante))
print(type(mi_booleano))
print(type(mi_string))