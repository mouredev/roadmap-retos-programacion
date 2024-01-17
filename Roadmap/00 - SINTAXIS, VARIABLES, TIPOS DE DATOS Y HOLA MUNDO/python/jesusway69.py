import os
os.system('clear')
#os.system('cls')

# COMENTARIO EN UN LÍNEA


"""
COMENTARIO EN VARIAS LÍNEAS:

 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
        https://www.python.org/
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

mi_variable_string = "Hola"
print(type(mi_variable_string))
MI_CONSTANTE_STRING = "Python"
print(type(MI_CONSTANTE_STRING))
mi_numero_int = 8
print(type(mi_numero_int))
mi_numero_float = 3.5
print(type(mi_numero_float))
mi_booleano = True
print(type(mi_booleano))
mi_numero_complex = 1+2j
print(type(mi_numero_complex))
mi_lista = ['¡',1,2,3,4,'!']
print(type(mi_lista))
mi_tupla = (1,2,3,4)
print(type(mi_tupla))
mi_diccionario = {"Hola":"Python"}
print(type(mi_diccionario))
mi_dato_vacio = None
print(type(mi_dato_vacio))

print (mi_lista[0] + mi_variable_string + " " + MI_CONSTANTE_STRING + mi_lista[5])
