# https://docs.python.org/3/

# Este es un comentario de una línea es recomendable
# por las buenas prácticas qué máximo tenga 80 caracteres.

"""
Esto también es un
comentario pero
de varias líneas
"""

'''
Esto también es un 
comentario pero 
de varias lineas
'''

# Crear una variable
hola_mundo = "Hola mundo"
hola_mundo = "Nuevo valor de mi variable"

# Python no tiene constantes, sin embargo; se puede hacer algo parecido.

MY_CONSTANTE = "Mi constante"  # por convención

entero: int = 1
flotante = 9.10
booleano1 = True
booleano2 = False
String = "Este es un str"

# También se pueden transformar algunos valores a otros.

print(float(1))
# 1.0
print(int(9.10))
# 9
print(bool(1))
# True
print(bool(15))
# True
print(bool(-4))
# True
print(bool(0))
# False
print(str(1))
# '1'
print(str(True))
# 'True'

# También se pueden transformar str a int, float y bool
# siempre y cuando sean los valores correctos.

print(int("9"))
# 9
print(int("9.10"))  # No se puede transformar.
# ValueError: invalid literal for int() with base 10: '9.10'
print(float("3.10"))
# 3.1
print(float("1"))
# 1.0
print(float("3.4, 1"))  # No se puede transformar.
# ValueError: could not convert string to float: '3.4, 1'

print(bool("0"))  # aquí pasa algo diferente, si el str tiene carácteres es True.
# True
print(bool(""))  # si no tiene devuelve False.
# False

"""
Adicional:
Por cierto si vas a ejecutar el código 
recomiendo que comentes las lineas que dan error
y también cuando hagas un proyecto en Python y uses PyCharm 
según la PeP8 debes dejar un espacio en blanco al final del código.
"""
# Por último hay una función de python que sirve para saber el tipo de dato.

print(type(entero))
print(type(flotante))
print(type(booleano1))
print(type(booleano2))
print(type(String))
