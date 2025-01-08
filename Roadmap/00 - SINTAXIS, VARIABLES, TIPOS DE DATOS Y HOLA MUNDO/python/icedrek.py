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

# Sitio oficial: https://www.python.org/

# Comentario de una linea con '#'

"""
Comentario de varias lineas.
En Python se pueden utilizar indistintamente comillas dobles "" o simples ''
"""

a = 1  # tras el codigo tambien se pueden incluir comentarios

# VARIABLES
# las variables se escriben con letras minúsculas
variable = "hola"

# si el nombre de la variable es compuesto, se utiliza snake_case(palabras separadas por '_'
variable_nombre_compuesto = "hola"

# también se puede definir el tipo de la variable
variable_tipo: str = 'hola'

# En python no existen las constantes.
# Se utiliza una variable escrita en mayusculas para indicar que es constante y no se debe cambiar
PI = 3.14

# TIPOS SIMPLES
variable_str: str = 'cadena de texto'  # Cadenas de texto (String)
variable_bool: bool = True  # Booleanos, pueden tener valor True o False
variable_int: int = 1  # Numero entero, en principio se puede escribir cualquier entero sin restricciones.
variable_float: float = 1.23  # Números reales (con decimales)
variable_compleja: complex = 2j  # Números complejos o imaginarios

# TIPOS COMPUESTOS
# Lista de elementos, puede contener varios tipos. Ordenada, mutable y admite duplicados
variable_lista: list = [1, 2, '3']
# Lista de elementos, puede contener varios tipos. Ordenada, inmutable y admite duplicados
variable_tupla: tuple = (1, '2', 3)
# Lista de elementos, puede contener varios tipos. Desordenada, inmutable y no admite duplicados
variable_set: set = {1, 2, 3}
# lista de clave:valor. Ordenada, mutable y no admite duplicados
variable_diccionario: dict = {1: 'a', 2: 'b', 3: 'c'}

# para mostrar un valor por pantalla se utiliza la funcion print()
print('hola Python')

# tambien podemos mostrar el valor de una variable
lenguaje = "Python"
print(f"hola {lenguaje}")
