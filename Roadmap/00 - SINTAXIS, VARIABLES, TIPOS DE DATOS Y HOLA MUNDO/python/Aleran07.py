# 00
#https://www.python.org/

"""
Esto es un comentario
"""

'''
Esto es otro comentario
'''

mi_variable = "Una variable"

MY_CONSTANT = "Un constante" # Se una como indicador de constante el mayuscula

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'


a = 4
A = "Sally"
#A will not overwrite a

x, y, z = "Orange", 2, "Cherry" # se pueden guardar multiples valores en una sola line
print(x)
print(y)
print(z)

x = y = z = "Orange" # tambien varias variables con el mismo
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "2"
z = "awesome"
print(x, y, z) # se puede imprimir texto concatenando en el print


x = "Python "
y = "is "
z = "awesome"
print(x + y + z) # concatenar pero con el + no le agrega espacios por defecto

x = 5
y = 10
print(x + y)

x = 5
y = "John"
#print(x + y) # Esto es un error porque no se puede sumar diferente variables
print(x, y)

x = "awesome"

def myfunc():
  global x  #Existen variables globales
  x = "fantastic"

myfunc()

print("Python is " + x)