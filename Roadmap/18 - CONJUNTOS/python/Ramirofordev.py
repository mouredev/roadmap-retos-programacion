'''
Ejercicio:
Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes operaciones:
    * Agrega un elemento al final
    * Agrega un elemento al principio
    * Agrega varios elementos en bloque al final
    * Agrega varios elementos en bloque en una posicion concreta
    * Elimina un elemento en una posicion concreta
    * Actualiza el valor de un elemento en un posicion concreta
    * Comprueba si un elemento esta en un conjunto
    * Elimina todo el contenido del conjunto
'''

data = [1, 2, 3, 4]

# Agrega un elemento al final
data.append(5)
print(data)

# Agrega un elemento al principio
data.insert(0, 0)
print(data)

# Agrega varios elementos en el bloque al final
data.extend([ 6, 7, 8])
print(data)

# Agrega varios elementos en una posicion concreta
new_data = [10, 15, 20]
for i, elemento in enumerate(new_data):
    data.insert(2 + i, elemento)
print(data)

"""
Usando slicing
data[3:5] = [1, 2, 3, 4]
"""

# Elimina un elemento de una posicion concreta
del data[2]
print(data)

# Actualiza el valor de un elemento en una posicion concreata
data[0] = -10
print(data)

# Comprueba si un elemento esa en el conjunto
esta = True if 1 in data else False
print(esta)

# Elimina todo el contenido del conjunto
data.clear()
print(data)

'''
Dificultad extra:
Muestra ejemplos de las siguientes operaciones con conjuntos:
    * Union
    * Interseccion
    * Diferencia
    * Diferencia simetrica
'''

set_a = set([1, 2, 3, 4])
set_b = set([5, 6, 7, 8])

# Union 
all_numbers = set_a.union(set_b)
print(all_numbers)

# Interseccion
names_a = set(["Marcos", "Nacho", "Cassandra", "Elissa"])
names_b = set(["Cassandra", "Nacho", "Paco", "Ismael"])
common_names = names_a.intersection(names_b)
print(common_names)

# Diferencia
print(all_numbers.difference(set_a))

# Diferencia simetrica
print(all_numbers.symmetric_difference(set_b))