# POR VALOR
# Asignación por valor con enteros (números inmutables)
a = 5
b = a
b = 10
print(a)  # Esto imprimirá 5, porque 'a' y 'b' son independientes

# Asignación por valor con cadenas (inmutables)
str1 = "Hola"
str2 = str1
str2 = "Mundo"
print(str1)  # Esto imprimirá "Hola", porque 'str1' y 'str2' son independientes

# POR REFERENCIA
# Asignación por referencia con listas (mutables)
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)  # Esto imprimirá [1, 2, 3, 4], porque 'lista1' y 'lista2' referencian al mismo objeto

# Asignación por referencia con diccionarios (mutables)
dict1 = {'a': 1, 'b': 2}
dict2 = dict1
dict2['c'] = 3
print(dict1)  # Esto imprimirá {'a': 1, 'b': 2, 'c': 3}, porque 'dict1' y 'dict2' referencian al mismo objeto

# FUNCIONES CON PARÁMETROS POR VALOR
def modificar_valor(x): # x es un parámetro por valor
    x = 10
    print(f"Valor de x dentro de la función: {x}") # Esto imprimirá 10

a = 5
modificar_valor(a) # Llamamos a la función con 'a' como argumento
print(f"Valor de a fuera de la función: {a}") # Esto imprimirá 5

# FUNCIONES CON PARÁMETROS POR REFERENCIA
def modificar_lista(lista): # lista es un parámetro por referencia
    lista.append(4) # Modificamos la lista
    print(f"Lista dentro de la función: {lista}") # Esto imprimirá [1, 2, 3, 4]

mi_lista = [1, 2, 3]
modificar_lista(mi_lista) # Llamamos a la función con 'mi_lista' como argumento
print(f"Lista fuera de la función: {mi_lista}") # Esto imprimirá [1, 2, 3, 4]


def modificar_lista_sin_cambiar_original(lista): # lista es un parámetro por referencia
    lista = lista.copy() # Creamos una copia de la lista
    lista.append(4) # Modificamos la lista
    print(f"Lista dentro de la función: {lista}") # Esto imprimirá [1, 2, 3, 4]

mi_lista = [1, 2, 3]
modificar_lista_sin_cambiar_original(mi_lista) # Llamamos a la función con 'mi_lista' como argumento
print(f"Lista fuera de la función: {mi_lista}") # Esto imprimirá [1, 2, 3]

"""
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
  Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
  se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
  variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
  Comprueba también que se ha conservado el valor original en las primeras.
"""

def intercambiar_por_valor(x, y):
    x, y = y, x # Intercambiamos los valores
    return x, y # Retornamos los nuevos valores

a = 10
b = 20

nuevo_a, nuevo_b = intercambiar_por_valor(a, b) # Llamamos a la función con 'a' y 'b' como argumentos

print(f"Valores originales: a = {a}, b = {b}") # Esto imprimirá "Valores originales: a = 10, b = 20"
print(f"Nuevos valores: nuevo_a = {nuevo_a}, nuevo_b = {nuevo_b}") # Esto imprimirá "Nuevos valores: nuevo_a = 20, nuevo_b = 10"

def intercambiar_por_referencia(lista1, lista2):
    lista1, lista2 = lista2.copy(), lista1.copy() # Intercambiamos las listas creando copias
    return lista1, lista2 # Retornamos las nuevas listas

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

nueva_lista_a, nueva_lista_b = intercambiar_por_referencia(lista_a, lista_b) # Llamamos a la función con 'lista_a' y 'lista_b' como argumentos

print(f"Listas originales: lista_a = {lista_a}, lista_b = {lista_b}")
print(f"Nuevas listas: nueva_lista_a = {nueva_lista_a}, nueva_lista_b = {nueva_lista_b}")
