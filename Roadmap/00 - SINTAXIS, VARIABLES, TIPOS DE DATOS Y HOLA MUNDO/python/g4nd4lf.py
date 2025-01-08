# https://www.python.org/

# Este carácter sirve para comentar una sola línea

"""Con triples comillas simples o dobles se pueden
comentar varias lineas.
"""

'''Ejemplo para comentar múltiples lineas
con las triples comillas simples.
'''

#Creación de una variable
vble_name="Hello world"

#No existen constantes como tal, pero por convenio se usan mayúsculas para identificar una varible que se usará como constante
MY_CONSTANT="Esto se usará como constante" #Aunque en realidad es también una variable (es mutable), al ponerla en mayúscula hacemos ver que se va a usar como constante.

#Tipos primitivos de python:
integer_vble=4
float_vble=2.345
boolean_vble=False
boolean_vble=True
string_vble="Hello world"
binary_vble=b'\x68\x65\x6c\x6c\x6f'
none_vble=None

#Impresión por pantalla:
print("¡Hola, Python!")

print(type(integer_vble))
print(type(float_vble))
print(type(boolean_vble))
print(type(string_vble))
print(type(binary_vble))
print(type(none_vble))