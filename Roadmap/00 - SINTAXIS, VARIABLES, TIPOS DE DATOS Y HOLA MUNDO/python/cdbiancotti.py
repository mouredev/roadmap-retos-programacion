#  * EJERCICIO:
#  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
#  *   lenguaje de programación que has seleccionado.

# https://docs.python.org/3/

#  * - Representa las diferentes sintaxis que existen de crear comentarios
#  *   en el lenguaje (en una línea, varias...).

# Esto es un comentario

#  * - Crea una variable (y una constante si el lenguaje lo soporta).
PSEUDO_CONSTANTE = ('python no posee constantes por lo cual se usa por convencion este'
                    'formato para representar que la variable se quiere utilizar como constante')
variable = 'soy una variable'

#  * - Crea variables representando todos los tipos de datos primitivos
#  *   del lenguaje (cadenas de texto, enteros, booleanos...).

# los que conocia
entero = 1
flotante = 1.5
complejo = 3j
string = 'soy un string'
booleano = True  # False
lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)
conjunto = {1, 2, 3, 4}
diccionario = {
    1: 'prueba',
    '2': ['otro', 'dato']
}

# los que no conocia como primitivos
conjunto_congelado = frozenset({1, 2, 3, 4})
rango = range(5)

# los que no conocia como primitivos pero no use nunca
byte1 = b'Esto lo transformo a bytes'  # bytes
byte2 = bytes(15)  # bytes
bytearray1 = bytearray(10)  # bytearray

#  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print("¡Hola, Python!")
