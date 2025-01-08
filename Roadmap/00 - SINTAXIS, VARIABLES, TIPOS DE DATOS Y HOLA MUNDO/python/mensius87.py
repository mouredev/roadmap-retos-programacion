"""
 * EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del
    lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""


# Sitio oficial de Python: https://www.python.org/

# Comentario de una línea

"""
Este es un comentario multilínea. Aunque Python no tiene una forma de generar este tipo de comentarios, si a una cadena
de texto envuelta entre estas comillas triples no se le asigna una variable, Python la ignorará y servirá de comentario.
"""

variable = "Hola MoureDev"

CONSTANTE = 3,14 # en Python no hay constantes, pero por convención si la variable está en mayúsculas se tomará como tal

entero = 20

flotante = 1.4

texto = "Python"

Booleano = True


print(f"Hola {texto}")
