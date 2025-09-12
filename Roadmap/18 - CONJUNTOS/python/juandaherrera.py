"""
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
"""

my_set = [1, 2, 3, 4, 5]
my_set.append(6)
my_set.insert(0, 0)
my_set.extend([7, 8, 9])
my_set[3:3] = [-1, -2, -3]
del my_set[3]
my_set[4] = -1
print(-1 in my_set)

print(my_set)
my_set.clear()
print(my_set)

"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

my_new_set = {1, 2, 3, 4, 5}
my_other_set = {1, 2, 3, 4, 6, 7}

print(f"{my_new_set=}, {my_other_set=}")
print("Union:", my_new_set.union(my_other_set))
print("Intersección:", my_new_set.intersection(my_other_set))
print("Diferencia:", my_new_set.difference(my_other_set))
print("Diferencia Simétrica:", my_other_set.symmetric_difference(my_new_set))
