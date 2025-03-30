"""
Conjuntos:

"""

my_list = [1, 2, 3]

# Añade un elemento al final.
my_list.append(4)
print(my_list)

# Añade un elemento al principio.
my_list.insert(0, 0)
print(my_list)

# Añade varios elementos en bloque al final.
my_list.extend([5, 6, 7])
print(my_list)

# Añade varios elementos en bloque en una posición concreta.
my_list[3:3] = [4, 3, 2]
print(my_list)

# Elimina un elemento en una posición concreta.
del my_list[3]
print(my_list)

# Actualiza el valor de un elemento en una posición concreta.
my_list[0] = 2
print(my_list)

# Comprueba si un elemento está en un conjunto.
print(2 in my_list)

# Elimina todo el contenido del conjunto.
#del my_list[:]
my_list.clear()
print(my_list)

"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

elements_1 = {1, 2, 3, 4}
elements_2 = {1, 3, 7, 5}

# Unión
print(f"Unión: {elements_1.union(elements_2)}")

# Intersección
print(f"Intersección: {elements_1.intersection(elements_2)}")

# Diferencia
print(f"Diferencia: {elements_1.difference(elements_2), elements_2.difference(elements_1)}")

# Diferencia simétrica
print(f"Intersección: {elements_1.symmetric_difference(elements_2)}")