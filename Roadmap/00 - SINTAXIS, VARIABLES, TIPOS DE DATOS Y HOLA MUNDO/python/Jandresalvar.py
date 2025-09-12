### 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

## Ejercicio

# - Crea un comentario en el codigo y coloca la URL del sitio web oficial del
#   lenguaje de programacion que has seleccionado.

# - Representa las diferentes sintaxis que existen de crear comentarios
#   en el lenguaje (en una linea, varias...).

# - Crea una variable (y una constante si el lenguaje lo soporta).

# - Crea variables representando todos los tipos de datos primitivos
#   del lenguaje (cadenas de texto, enteros, booleanos...).

# - Imprime por terminal el texto: "!Hola, [y el nombre de tu lenguaje]!"

## Solucion

# - La documentación oficial de Python 3 se encuentra en la url https://docs.python.org/3/

# - Para crear un comentario de una linea en python se utiliza el operador #.
#   Python no tiene un operador para comentar multiples lineas, como otros lenguajes.
#   No es recomendable utilizar cadenas multilinea (""") para comentar, pues aunque el codigo
#   no se ejecuta, si ocupa espacio en memoria. Lo mejor es usar # cuantas veces sea necesario.

# - En Python solo existe un operador de asignación para crear variables: el signo igual =. 
#   Este operador asigna el valor que está a la derecha al nombre que definimos a la izquierda. 
        my_var = "Hello, Python!"
        my_var2 = 5 * 4
#   Los nombres de las variables en Python deben cumplir ciertas reglas:
#   * No pueden ser palabras reservadas del lenguaje, como if, for, while, class, etc.
#   * Deben comenzar con una letra o un guion bajo (_), seguido de letras, números o guion bajo:
#       * Válidos: my_var, _variable, var123
#       * Inválidos: 2var, my-var, my var
#   * No pueden contener espacios ni caracteres especiales como -, $, o @.
#   * Son sensibles a mayúsculas y minúsculas: myvar, MyVar, y MYVAR son variables diferentes.
#   En python se pueden asignar multiples valores a multiples variables en una sola linea:
       x, y, z = 1, 2, 3
#   En Python, las constantes no tienen un tratamiento especial como en algunos otros lenguajes. 
#   Se suelen definir usando nombres en mayúsculas por convención, pero no hay nada que impida que su valor cambie:
        PI = 3.14159  
        MONTHS = ["January", "February", "March", ...]
# - Los tipos de datos primitivos en python y las estructuras de datos mas comunes son:
   # Tipos numéricos
    entero = 42                # int
    decimal = 3.14159          # float
    complejo = 2 + 3j          # complex

    # Tipo de texto
    cadena = "Hola, mundo"     # str

    # Tipo booleano
    verdadero = True           # bool
    falso = False              # bool

    # Tipo None
    nulo = None                # NoneType

    # Estructuras de datos:
    lista = [1, 2, 3, 4]       # list
    tupla = (5, 6, 7, 8)       # tuple
    conjunto = {9, 10, 11, 12} # set
    diccionario = {"clave": "valor"} # dict

# - En python se usa la funcion prin() para imprimir por consola:
print(¡Hola Python!)
