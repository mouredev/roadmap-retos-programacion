# Asignacion de variables en python
# En python los enteros, flotantes, cadenas y tuplas, sea signan por valor.
# Esto significa que cuando asignas una variable a otra, se crea una copia independiente del valor.

# Asignacion por valor
a = 10
b = a
print(f'a: {a}, b: {b}') # 'b' recibe una copia de del valor de 'a'

# Modificamos b
b = 20
print(f'a:{a}, b:{b}') # 'a' no se ve afectada ya que los enteros son inmutables.


# Asignacion por referencia
# En python las listas, diccionarios y conjuntos, se asignan por referencia.
# Esto significa que cuando asignas una variable a otra, ambas apuntan al mismo objeto en memoria.

lista_1 = [1, 2 ,3]
lista_2 = lista_1
print(f'Lista 1: {lista_1}, Lista 2: {lista_2}')

# Modificamos la lista 2
lista_2.append(4)
print(f'Lista 1: {lista_1}, Lista 2: {lista_2}') # Al modificar la lista 2, tambien se modifica la lista 1

# Crear una copia independiente de un objeto mutable
lista_1 = [1, 2 ,3]
lista_2 = lista_1.copy() # Lista 2 es una copia independiente de lista 1
print(f'Lista 1: {lista_1}, Lista 2: {lista_2}') 

lista_2.append(4)
print(f'Lista 1: {lista_1}, Lista 2: {lista_2}') # Lista 1 no se ve afectada por los cambios de lista 2


# Extra

# Función para intercambiar valores por valor
def intercambiar_por_valor(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = 10
y = 20

nuevo_x, nuevo_y = intercambiar_por_valor(x, y)

print(f"Originales: x = {x}, y = {y}")
print(f"Nuevos: nuevo_x = {nuevo_x}, nuevo_y = {nuevo_y}")




# Función para intercambiar valores por referencia
def intercambiar_por_referencia(lista1, lista2):
    temp = lista1[:]
    lista1[:] = lista2[:]
    lista2[:] = temp  
    return lista1, lista2

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

nueva_lista_a, nueva_lista_b = intercambiar_por_referencia(lista_a, lista_b)

print(f"Originales: lista_a = {lista_a}, lista_b = {lista_b}")
print(f"Nuevas: nueva_lista_a = {nueva_lista_a}, nueva_lista_b = {nueva_lista_b}")