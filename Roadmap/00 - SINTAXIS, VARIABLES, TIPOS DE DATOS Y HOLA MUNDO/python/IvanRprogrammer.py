# https://www.python.org/

# comentarios en python

# Comentarios de una sola línea:

# Este es un comentario de una sola línea
x = 10  # Tambien se puede incluiral final de una línea de código

# Comentarios multilínea:

# tres comillas dobles ("""):

"""
Este bloque se usa para escribir notas largas o explicaciones complejas.
Se elige cuando queremos detallar qué hace un programa sin saturar el código.
Sirve para que cualquier persona que lea el archivo entienda el contexto general.
"""


# tres comillas simples ('''):

'''
Este formato de tres comillas simples hace exactamente lo mismo.
Se usa principalmente cuando el texto incluye comillas dobles en su redacción.
Sirve para evitar errores de sintaxis al citar o mencionar textos encomillados.
'''

# Así se deben definir las variables en Python:

my_variable = "ivan" # unavariable que almacena una cadena de texto
my_number = 38 # una variable que almacena un número entero
my_boolean = True # una variable que almacena un valor booleano (True o False)

"""
 el fin de la variable es que todos los datos pueden mutar,
 es decir, cambiar su valor a lo largo del programa.
"""

# constantes en python

"""
Segun lo que he investigado en python las constantes,
técnicamente no existen a nivel de lenguaje: 
el valor de cualquier variable se puede cambiar en cualquier momento.
Sacado de: 'https://pythonscouts.com/constantes-python/'
"""
"""
sin embargo, por convención, 
se utilizan nombres de variables en MAYUSCULAS,
para indicar que son constantes y no deben modificarse.
"""
#ejemplo de constante en python

PI = 3.14159  # constante que representa el valor de pi
PUERTO_SERVIDOR = 5174 # constante que representa el puerto del servidor
IMPUESTO_VENTA = 0.15 # constante que representa el impuesto de venta

# un ejemplo de uso de constantes en una función:

# Esto es una CONSTANTE, por convención, la tratamos como inmutable:
IMPUESTO_IVA = 0.19 # iva sacado de colombia 

# Esto es una VARIABLE, su valor cambia con el tiempo:
total_compra = 100.00
total_con_iva = total_compra * (1 + IMPUESTO_IVA)

# Agregamos print() para ver el resultado en pantalla:

print(total_con_iva) # por lo cual debe arrojar un resultado de 119.0, ya que 100 * (1 + 0.19) = 119.0

"""
Los tipos de datos primitivos o básicos,
ya que son las formas más elementales
que tiene un lenguaje para almacenar información.
"""
# En Python existen 4 tipos de datos primitivos principales:

# 1. cadenas de texto (str):
my_name = "Ivan"
my_last_names = 'Rodriguez Ulloa'

# 2. numeros enteros (int):
my_age = 38

# 3. numeros decimales (float):
my_height = 1.75

# 4. booleanos (bool):
my_is_student = True
my_is_employed = False

"""
Para imprimir ese mensaje en Python,
se utiliza la función print(),
y se puede definir el nombre del lenguaje,
en una variable en snake_case,
para esta caso voy a dar dos opciones:
"""

my_language = "Python"
print(f"Hola, estoy aprendiendo, {my_language}!") # f-string (Recomendada)
print("Hola, estoy aprendiendo, " + my_language + "!") # concatenación tradicional de cadenas de texto

# EXtra para tener en cuenta:

"""
Con concatenación (+),
si intentas unir texto con un número,
Python lanza un error de tipo (TypeError):
"""
my_age = 38
print("Tengo " + my_age) # Esto generará un error de tipo (TypeError), para qe funcione debe ir print("Tengo " + str(my_age))

"""
En cambio, Con f-strings,
Python convierte automáticamente cualquier,
número o tipo de dato a texto:
"""

print(f"Tengo {my_age}") # Esto funcionará correctamente
