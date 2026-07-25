## Ejercicio 00 Sintaxis, Variables, Tipos de Datos y Hola Mundo

## Documentación Oficial de Python: https://docs.python.org/3/


## Comentario de una sola línea
"""
   Esto es un comentario de varias líneas de python, también conocido como docstring.
   Se utiliza para documentar el código y explicar su funcionamiento y tambien no tire errores de sintaxis 
   al escribir varias líneas de texto. 

"""

## Crear una variable

mi_nombre = "Francisco"
mi_edad = 45
DOLAR = 800.20 ## Las constantes no existen en python, pero se suele escribir en mayúscula para indicar que no debe ser modificada.

## Datos primitivos en python str, int, float, bool,

## String con tipo de dato especificado
mi_nombre: str = "Francisco Riquelme"

## Int con tipo de dato especificado
mi_edad_actual: int = 26

## Float con tipo de dato especificado
precio_dolar: float = 800.20

## Bool con tipo de dato especificado
es_mayor_de_edad: bool = True
es_menor_de_edad: bool = False

## Imprimir en consola saludo en el lenguaje
print("¡Hola, {}!".format("Python"))## Utilizamos el método format para insertar el nombre del lenguaje en el saludo.



