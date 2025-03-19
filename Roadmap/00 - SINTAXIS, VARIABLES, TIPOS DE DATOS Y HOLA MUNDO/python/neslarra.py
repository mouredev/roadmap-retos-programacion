"""
Ésto es un comentario multilínea:

EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del
   lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios
   en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos
   del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 debemos comenzar por el principio.
"""

# Ésto es un cometario en una línea => Aprende sobre Python en su web oficial: https://www.python.org/

# las constantes en Python son variables, que por convención, se crean en MAYÚSCULA y se asume NO alterarlas.
CONSTANTE_URL_LENGUAGE: str = "https://www.python.org/"

# Tipos primitivos
entero: int = 1
flotante: float = 1.1
cadena: str = "Python"
booleano: bool = True

print(f"""Tipos primitivos:
      Entero {entero} <= nombre de la clase: {entero.__class__.__name__}
      Flotante {flotante} <= nombre de la clase: {flotante.__class__.__name__}
      Cadena {cadena} <= nombre de la clase: {cadena.__class__.__name__}
      Booleano {booleano} <= nombre de la clase: {booleano.__class__.__name__}
      """)

print(f"Hola {cadena}!!!")   # Ah, también puedo comentar al margen de la instrucción.
print(f"Disponible en {CONSTANTE_URL_LENGUAGE}")
