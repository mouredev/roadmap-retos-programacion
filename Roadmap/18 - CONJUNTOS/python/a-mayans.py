
# conjunto de datos -> lista
my_list = [2, 4, 6, 8, 10]

# añadir un elemento al final
my_list.append(12)

# añadir un elemento al principio
my_list.insert(0, 13)

# añadir varios elementos en bloque al final
my_list.extend([14, 16, 18])

# añadir varios elementos en bloque en una posición concreta
new_elements = [27, 28, 29, 30]
position = 3
my_list[position:position] = new_elements

# eliminar un elemento en una posición concreta
my_list.pop(10)

# actualizar el valor de un elemento en una posición concreta
my_list[5] = 69

# comprobar si un elemento está en un conjunto
element = 27
is_present = element in my_list
print(is_present) # devuelve true

# eliminar todo el contenido del conjunto
## una opcion -> my_list = []
## otra opcion
my_list.clear()


'''
 * DIFICULTAD EXTRA 
'''

# Unión: unir dos conjuntos
list1 = set([1, 2, 3, 4, 5])
list2 = set([5, 6, 7, 8, 9])
united = list1.union(list2)
print(united) # devuelve {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Intersección: que elementos tienen en comun
intersection = list1.intersection(list2)
print(intersection) # devuelve {5}

# Diferencia: se queda con los diferentes del conjunto a comparar
difference = list1.difference(list2)
print(difference) # devuelve {1, 2, 3, 4, 10}

# Diferencia simétrica: se queda con todos, excluyendo los comunes
sym_diff = list1.symmetric_difference(list2)
print(sym_diff) # devuelve {1, 2, 3, 4, 6, 7, 8, 9, 10}