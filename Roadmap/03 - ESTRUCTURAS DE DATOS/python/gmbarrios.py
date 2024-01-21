# Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.

# 1. Lista
lista_1 = [14, 15, 22, 50, 77, 75, 42]
lista_2 = ['futbol', 'baseball', 'basketball', 'hockey', 'tenis']
lista_3 = [[1, 2, 3], 4, 5, 6]
lista_4 = ['lista', 9, 8, 7, 'mezclada']
print(lista_1)
print(lista_2)
print(lista_3)
print(lista_4)

# 2. Tupla
tupla_1 = (10, 11, 12, 13, 14, 15)
tupla_2 = ('a', 'b', 'c', [1, 2, 3])
print(tupla_1)
print(tupla_2)

# 3. Diccionario
dicc_1 = {
    "Ronaldo": "Real Madrid",
    "Messi": "Barcelona",
    "Busquets": "Barcelona",
    "Marcelo": "Real Madrid",
    "Casillas": "Real Madrid",
}
print(dicc_1)

# 4. Set
set_1 = {44, 55, 66, 77, 88, 99}
print(set_1)


# Utiliza operaciones de inserción, borrado, actualización y ordenación.
# 1. Listas

lista_1.append(40) # Agregar al final de la lista.
lista_1.insert(1, 5) # Agregar en una posición determinada.
print(lista_1)
lista_1.pop() # Eliminar el ultimo elemento de la lista.
lista_1.remove(75) # Eliminar un valor determinado.
print(lista_1)
lista_1.clear() # Eliminar todos los elementos de la lista.
print(lista_1)
lista_2[0] = 'football'
print(lista_2)
lista_2.sort() # Ordenar de forma ascendente.
print(lista_2)
lista_3.reverse() # Ordenar de forma descendente.
print(lista_3)

# 2. Tuplas: son inmutables

# 3. Diccionarios

dicc_1['Nazario'] = 'Real Madrid'
dicc_1.pop('Ronaldo')
del dicc_1['Busquets']
print(dicc_1)

# 4. Sets
set_1.add(111)
set_1.pop()
set_1.remove(44)
print(set_1)
