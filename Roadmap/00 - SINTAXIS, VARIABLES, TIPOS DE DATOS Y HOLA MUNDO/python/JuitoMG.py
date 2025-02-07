#   EJERCICIO:
#  - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

# https://www.python.org/


#  - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

# Comentario en una línea

"""
Comentario
en varias
líneas
"""

'''
Alternativa
comentario 
en varias
líneas
'''

#  - Crea una variable (y una constante si el lenguaje lo soporta).

pajaro = "loro"

# Python no admite constantes, aunque podemos indicarlas igualmente en el código de la siguiente manera

MI_CONSTANTE = 10
PI = 3.14

#Como ejemplo, vamos a probar que es posible no solo cambiar el valor de la "constante", sino también su tipo.

print(type(MI_CONSTANTE)) #Tipo int
print(type(PI))  #Tipo float

MI_CONSTANTE = MI_CONSTANTE + PI

print(MI_CONSTANTE)
print(type(MI_CONSTANTE))  #Nos devuelve que ahora esta "constante" pasó de ser tipo int a tipo float

#  - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

string = "Nombre"
entero = 33
float = 3.56
booleano = True


#  - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

lenguaje = "Python"
print(f"Hola, {lenguaje}!")
print("Hola",lenguaje,"!")