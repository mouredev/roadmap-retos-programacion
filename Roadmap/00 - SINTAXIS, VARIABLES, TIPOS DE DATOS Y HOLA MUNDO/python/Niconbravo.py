#https://www.python.org/
lenguaje_escogido= "Python"

#Así se crea un comentario simple de una línea en Python
"También pueden usarse doble comillas"
'Y también son funcionales las comillas simples'
#Se puede combinar las comillas y doble comillas sin problemas para hacer énfasis:
"Esta es una 'frase' que combina ambas sin problemas"

#Se puede hacer un comentario de varias lineas con triple comillas
'''
Esto es un comentario de bloque de varias líneas
que puede ser utilizado para explicar código
'''
#También se puede hacer con doble comilas:
"""
Esto es un comentario de bloque de varias líneas
que puede ser utilizado para explicar código
"""
#¿Cómo nombrar variables?
"""
Las variables en Python pueden ser nombradas de la siguiente manera:
1. No pueden comenzar con números
2. No pueden contener espacios en blanco
3. No pueden contener caracteres especiales
4. No pueden ser iguales a palabras reservadas de Python
"""
#Por convención se recomienda utiizar snake case para nombrar variables. Esta utiliza guión bajo para separar palabras.
#Además se recomienda que el nombre sea fácil de comprender:
#Ejemplo de variable con snake case
nombre_usuario = "Juan"


#Tipo de datos:
"Datos numéricos:"
numeros_enteros = 1
numeros_flotantes = 3.14

"Datos de caracteres:"
cadena_de_texto = "Esta es una cadena de texto"

"Datos booleanos"
boleanos_verdadero = True
boleanos_falso = False

variable = "Carlos"
"""En python no existen las constantes pero por convención.
Se pueden utilizar mayúsculas y guiones bajos 
 para indicar que es una constante"""
CONSTANTE_NOMBRE = "Carlos"

print("¡Hola, {}!".format(lenguaje_escogido))
