"""
    Reto de programación #00  SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
"""

'''EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"'''

# URL del sitio oficial de Python: https://www.python.org/

"""En el lenguaje Python existen 2 tipos de comentarios:
    -Comentarios en linéa, cuya sintaxis es agregar un signo "Numeral"(#) antes
     del comentario, con el cual, se puede, comentar toda una linéa, o solo parte de ella.
     los mismos, no llevan un "cierre", ya que se "cierran" automaticamente al hacer un salto de linea.
    
    -Comentarios en bloque, los cuales, tienen 2 sintaxis posibles, 
        estos son el uso de 3 comillas seguidas para su apertura, y estas pueden ser
        simples(') o dobles("), y nuevamente, 3 comillas para el cierre(del mismo tipo usado para la apertura).
        Este tipo de comentario permite que el interprete "ignore" una o varias linéas consecutivas.
        Todo lo que este entre una apertura y el proximo cierre, sera un comentario.
"""

# Esto es un comentario en linéa (de linéa completa).

lenguaje = 'Python' # Esto es un comentario en linéa (parcial).

"""Esto es un comentario de bloque con comillas dobles."""

'''Esto es un comentario de bloque con comillas simples.'''

# Creación de una variable
edad = 38

# Creación de una constante
'''Si bien, python no cuenta con "Constantes" como tales
    Se utiliza la sintaxis de nombrar a la variable con mayusculas
    cuando se requiere de una constante. Esta, igualmente, podra ser 
    modificada posteriormente, pero el uso de mayusculas, le deberia
    recordar al programador que no se debe modificar su valor
'''
PI = 3.14159265

# Variable del tipo entero (int)
numeroReto = 0

# Variable del tipo decimal (float)
temperatura = 28.37

# Variable del tipo caracter (char)
letra = 'a'

# Variable del tipo cadena de caracteres (String)
saludo = '¡Hola,'

# Variable del tipo booleano (bool)
estado = True

# Impresión de "Hola mundo!!!"
print(saludo,lenguaje+'!')