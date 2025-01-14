# #05 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
#--Asignación de Variables--
#VALOR
print("Asignación de Variables")
print("Valor")
a = 5
b = a

print("a: ", a)
print("b: ", b)

#REFERENCIA
print("Referencia")
lista1 = [1, 2, 3]
lista2 = lista1

print("lista1: ", lista1)
print("lista2: ", lista2)


lista2.append(4)
print("lista1: ", lista1)
print("lista2: ", lista2)


#--Variables a Funciones--
#VALOR
print("Variables a Funciones")
print("Valor")
def modificar_valor(x):
    x = 10

a = 5
modificar_valor(a)
print(a)

#REFERENCIA
print("Referencia")
def modificar_referencia(lista):
    lista.append(4)

lista1 = [1, 2, 3]
modificar_referencia(lista1)
print(lista1)



"""
EXTRA
"""
print("Extra Valor")
# Funciones para intercambiar valores
def intercambiar_valor(a, b):
    a, b = b, a
    return a, b

# Variables Originales
x = 5
y = 10

# Asignamos a nuevas variables
nuevoX, nuevoY = intercambiar_valor(x, y)

# Imprimir los resultado en la consola
print(f"Originales: x = {x}, y = {y}")
print(f"Nuevas: nuevo_X = {nuevoX}, nuevo_Y = {nuevoY}")


print("Extra Referencia")
# Función para intercambiar valores en lista
def intercambio_lista(lista1, lista2):
    lista1[:], lista2[:] = lista2[:], lista1[:]
    return lista1, lista2

# Variables Originales
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Creamos copias de las listas
lista_a_original = lista_a[:]
lista_b_original = lista_b[:]

# Asignación a nuevas variables
nueva_lista_a, nueva_lista_b = intercambio_lista(lista_a, lista_b)

# Imprimir los resultado en la consola
print(f"Originales: lista_a = {lista_a_original}, lista_b = {lista_b_original}")
print(f"Nuevas: nueva_lista_a = {nueva_lista_a}, nueva_lista_b = {nueva_lista_b}")