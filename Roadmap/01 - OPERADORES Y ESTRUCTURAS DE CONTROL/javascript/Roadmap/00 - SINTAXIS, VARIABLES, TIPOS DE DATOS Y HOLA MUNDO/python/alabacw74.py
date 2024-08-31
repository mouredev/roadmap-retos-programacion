'''
# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
> #### Dificultad: Fácil | Publicación: 26/12/23 | Corrección: 02/01/24

Author: Alfredo Aburto Alcudia: https://github.com/alabacw74

## Ejercicio

```
/*
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
 */
```
'''

# Ejercicio 1
# Documentación oficial
# https://python-docs-es.readthedocs.io/es/3.12/

# Ejercicio 2

"""
Este es un comentario
de varias líneas en Python.
Puede abarcar múltiples líneas
sin necesidad de agregar el carácter "#" en cada línea.
"""

'''
Tambien se pueden utilizar comillas simples 
para crear comentarios multilinea
'''

# Ejercicio 3

'''
En python se incluyen valrores a muchas constantes universales, para hacer
uso de ellas es necesario importar librerias por ejemplo, math.

Si deseamos crear nuestras propias constantes podemos usar una sintaxis especial
en la definición de nuestras variables, un ejemplo sería utilizar un nombre que
solo incluya letras mayusculas
'''

MICONSTANTE = 12.2545
print(f'La variable MICONSTANTE es de tipo {type(MICONSTANTE)}')


# Ejercicio 4

# Definición de variables nativas en Python

# Numericas (int y float)

numero_entero = 27
print(f'La variable numero_entero es de tipo {type(numero_entero)}')

numero_decimal = 6.685
print(f'La variable numero_entero es de tipo {type(numero_decimal)}')

# Texto (string)
caracter = "Cadena de texto en Python" # Podemos usar comillas simples o dobles
print(f'La variable caracter es de tipo {type(caracter)}')

# Booleanas
aprendo_python = True
print(f'La variable aprendo_python es de tipo {type(aprendo_python)}')

# Ejercicio 5
print("¡Hola, Python!")
