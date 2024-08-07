"""
EJERCICIO:
* - Crea un comentario en el código y coloca la URL del sitio web oficial del
*   lenguaje de programación que has seleccionado.
* - Representa las diferentes sintaxis que existen de crear comentarios
*   en el lenguaje (en una línea, varias...).
* - Crea una variable (y una constante si el lenguaje lo soporta).
* - Crea variables representando todos los tipos de datos primitivos
*   del lenguaje (cadenas de texto, enteros, booleanos...).
* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
"""

#Link de la pagina web del lenguaje de programacion seleccionado: https://www.python.org/
#Link de la pagina web de la documentacion del lenguaje de programacion: https://docs.python.org/3/

#Comentario de una linea

"""
Comentario de
varias lineas
"""

# 2 formas de representar variables
nombre = "Python"
nombre, apellido = "Python", "Developer"

#Constante
#Para representar constantes en python se utiliza el nombre de la variable en mayusculas para indicar que no se debe modificar su valor o se usa snake_case para indicar que es una constante de esta manera: CONSTANTE = "Valor" o VARIABLE_CONSTANTE = "Valor"
CONSTANTE = "Valor"
VARIABLE_CONSTANTE = "Valor"


#Tipos de datos primitivos
#String-Cadena de texto
saludo = "Hola mundo"
#Entero-Integer
edad = 23
#Decimal-Float
pi = 3.1416
#Booleano-Boolean
verdadero = True
falso = False

print(f"¡Hola, {nombre}!")