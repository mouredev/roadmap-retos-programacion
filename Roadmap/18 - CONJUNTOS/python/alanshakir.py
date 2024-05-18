"""
/*
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
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */
"""

my_list = [25, 36, 85, 48, 98, 74, 15, 69, 37]
my_other_list = [10, 25, 85, 19, 1]
# Añade un elemento al final.
my_list.append(20)
# Añade un elemento al principio.
my_list.insert(0, 19)
my_position = 5
#Añade varios elementos en bloque al final.
my_list.extend(my_other_list)
# Añade varios elementos en bloque en una posición concreta.
my_position = 4
my_other_list[my_position:my_position] = [85, 25, 74]
# Elimina un elemento en una posición concreta.
del my_list[my_position]
# Actualiza el valor de un elemento en una posición concreta.
my_list[my_position] = 34
# Comprueba si un elemento está en un conjunto.
my_element = 29
element = my_element in my_list
# Elimina todo el contenido del conjunto
my_other_list.clear()

#EXTRA
my_set = {20, 14, 75, 19, 85}
my_other_set = {15, 87, 24, 3, 5, 14}
print(f"union de conjuntos: ", my_set | my_other_set)
print(f"Interseccion de conjuntos: ", my_set & my_other_set)
print(f"Diferencia de conjuntos: ", my_set - my_other_set)
print(f"Diferencia simetrica de conjuntos: ", my_set ^ my_other_set)

# Funciones propias de Set
print(f"union de conjuntos: ", my_set.union(my_other_set))
print(f"Interseccion de conjuntos: ", my_set.intersection(my_other_set))
print(f"Diferencia de conjuntos: ", my_set.difference(my_other_set))
print(f"Diferencia simetrica de conjuntos: ", my_set.symmetric_difference(my_other_set))
