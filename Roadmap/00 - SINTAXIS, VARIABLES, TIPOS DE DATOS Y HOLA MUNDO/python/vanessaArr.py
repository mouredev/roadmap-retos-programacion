"""
EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web oficial del
lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

#https://www.python.org/

# Almohadilla o Numeral para comentarios sencillos de una sola linea 
"""
3 Comillas dobles para comentarios con bloques de texto 
"""
'''
3 comillas simples para comentarios con bloques de texto
'''

mi_edad = 23


"""
Python no soporta constantes pero esto se puede organizar escribiendo la variable en mayuscula 
para indicar que debe ser tratada como una constante y no debe ser modificada.
"""

MI_NOMBRE = "Vanessa" 

#Son 4 tipos de datos primitivos (int, float, str y bool)
tipos_primitivos_int: int = 12
tipos_primitivos_float: float  = 7.9
tipos_primitivos_string: str = "Hola, soy una cadena de texto"
tipos_primitivos_boolean: bool = False
tipos_primitivos_boolean: bool = True

print("Hola, soy " + MI_NOMBRE + " y estoy en python")  