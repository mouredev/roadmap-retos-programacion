"""Conjuntos
"""

#Un conjunto (o set) es una colección de elementos no ordenados, sin elementos repetidos, y que admite operaciones matemáticas como unión, intersección, diferencia, etc.

data = [2,3,4,5,6]
print(f"Estructura inicial {data}")


data.append(7)
print(f"Añadiendo elemento al final {data}")


data.insert(0,1)
print(f"Añadiendo elemento al principio {data}")

data.extend([8,9,10])
print(f"Añadiendo elementos al final {data}")

data[3:3] = [3.2, 3.6, 3.8]
print(f"Añadiendo elementos en una posicion {data}")

del data[4]
print(f"Eliminando un elemento concreto {data}")

data[3] = 3.4
print(f"Actualizando un elemento concreto {data}")

print(f"Comprobar si un elemento existe {3.2 in data}")

print(f"Eliminar el contenido {data.clear()}")



""" * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica."""


sets_1 = {1,2,3,4}
sets_2 = {1,2,3,5,6,7}

#Une todos los elementos de ambos conjuntos (sin repetidos).
print(f"Union: {sets_1.union(sets_2)}")
print(f"union {sets_1 | sets_2}")

#Elementos que están en ambos conjuntos.
print(f"Intersección: {sets_1.intersection(sets_2)}")
print(f"Intersección: {sets_1 & sets_2}")

#Elementos que están en A pero no en B.
print(f"Diferencia: {sets_1.difference(sets_2)}")
print(f"Diferencia: {sets_1 - sets_2}")

#Elementos que están en A o B, pero no en ambos.
print(f"Diferencia asimetrica: {sets_1.symmetric_difference(sets_2)}")
print(f"Diferencia asimetrica: {sets_1 ^ sets_2}")


#convertir una lista conjunto
lista = [1, 2, 3, 4, 3, 2, 5]
conjunto = set(lista)

print(conjunto)








