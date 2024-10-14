# https://www.python.org/

# Con una almohadilla indicamos un comentario de una linea.
'''
De esta forma, con comillas simples o dobles, tres en orden seguido, podemos indicar un comentario
que puede llenar varias lineas.
'''
# * - Crea una variable (y una constante si el lenguaje lo soporta).
github_name = 'LittleMabbit' # Variable 'github_name' asignado el valor de 'LittleMabbit'.
CONSTANTE = 21 # A pesar de que el lenguaje no soporta constantes, se puede indicar entre la comunidad escribiendo en mayúsculas.

# * - Crea variables representando todos los tipos de datos primitivos
# del lenguaje (cadenas de texto, enteros, booleanos...).

name = 'StringyThingy' # Valor tipo string, puede ser indicado con comillas dobles o simples.
name = "StringyThingyy" # Valor tipo string, en este caso usando doble comilla.
edad = 99 # Valor tipo integer.
edad = 99.9 # Valor tipo float/decimal.
edad = 99 + 4j # Valor tipo complex / complejo.
boolean_is_true = True # Valor tipo booleano, verdadero (True) o un sí, por así decirlo.
boolean_is_false = False # Valor tipo booleano, falso (False) o un no, por así decirlo.
any_value = None # Valor tipo None o Null, donde literalmente no hay ningún valor dentro de la variable.

# * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
language = 'Python'
print(f'¡Hola, {language}!')
