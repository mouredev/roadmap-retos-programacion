#https://www.python.org/

##SINTAXIS PARA CREAR COMENTARIOS DE UNA LINEA O DE VARIAS

#Esto es un comentario de una sola línea

#No existen una sintaxis para
#comentarios de varias líneas
# en py como en c# (/* ... */)

#Alternativa a comentarios de varias líneas
"""
No es una sintaxis como tal, pero
al ser texto que no esta asginado
a una variable, el interprete no 
tomará en cuenta este fragmento.
Que de hecho es lo recomendable por
convención para documentar funciones,
clases o módulos.
"""

##CREACION DE UNA VARIABLE Y CONTANTE*
nombre_variable = 'uisbaquiaxb18'
constante = 3.1416

#En py no se especifica el tipo de variable
#ni tampoco existen las contantes nativas

##CREACION DE VARIABLES CON TIPOS DE DATOS PRIMITIVOS

#int 
mi_edad = 27
#float
salario = 6500.50
#complex o complejos
z = 5 + 6j
#str o cadenas de texto
mi_nombre = "Luis"
#booleano
activo = False

#no primitivo

#byte
dato = b"Hello!"

##IMPRESION DE TEXTO POR TERMINAL
lenguaje = "Python"

print("!Hola, ", lenguaje, "!")


