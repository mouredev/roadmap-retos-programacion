# 00 Sintaxis, Variables, Tipos de Datos y Hola Mundo

"""
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 """

# URL del sitio web oficial del lenguaje: https://www.python.org/

# Comentarios en una línea
# Este es un comentario en una línea

# Comentarios en varias líneas
""" 
Este es un comentario
en varias líneas
"""

# Variable
mi_variable = "Hola, Python"

# Constante (en Python, por convención, se usa mayúsculas)
MI_CONSTANTE = 42

# Tipos de datos primitivos
cadena_texto = "Python"
entero = 100
flotante = 3.14
booleano = True
lista = [1, 2, 3]
diccionario = {"clave": "valor"}
my_byte = b"byte"
my_none = None
print(type(my_none))  # Verifica el tipo de dato
print(type(my_byte))  # Verifica el tipo de dato
print(type(diccionario))  # Verifica el tipo de dato
print(type(lista))  # Verifica el tipo de dato
print(type(booleano))  # Verifica el tipo de dato
print(type(flotante))  # Verifica el tipo de dato
print(type(entero))  # Verifica el tipo de dato

# Imprimir el mensaje
print(f"¡Hola, {cadena_texto}!")  # Imprime el mensaje en la terminal

MI_CONSTANTE = 33
print(MI_CONSTANTE) #Para confirmar que la constante se ha modificado

print("Fin del reto. ¡Sigue practicando y aprendiendo!")
