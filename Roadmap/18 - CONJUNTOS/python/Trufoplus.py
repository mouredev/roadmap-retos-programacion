###############################################################################
### CONJUNTOS
###############################################################################

my_set = {1, 2, 3, 4, 5}

print("\nAñade un elemento al final")
my_set.add(6)
print(my_set)


print("\nAñade un elemento al principio")
my_set.add(0)
print(my_set)


print("\nAñade varios elementos en bloque al final")
my_list = [7, 8, 9, 10]
my_set.update(my_list)
print(my_set)


print("\nElimina un elemento en una posición concreta")
my_set = list(my_set)
position = my_set[1]
my_set.remove(position)
my_set = set(my_set)
print(my_set)


print("\nActualiza el valor de un elemento en una posición concreta")
my_set = list(my_set)
my_set[0] = 1
my_set = set(my_set)
print(my_set)


print("\nComprueba si un elemento está en un conjunto")
element = 2
if element in my_set:
    print(f"El numero '{element}' esta en mi conjunto")
else:
    print(f"El '{element}' no esta en mi conjunto")


print("\nElimina todo el contenido del conjunto.")
my_set.clear()
print(my_set)

###############################################################################
### DIFICULTAD EXTRA
###############################################################################
my_set_1 = {1,2,3,4,5,6}
my_set_2 = {5,6,7,8,9,10}

print("\nUnion: ")
union = my_set_1 | my_set_2
print(union)
union2 = my_set_1.union(my_set_2)
print(union2)

print("\nInterseccion: ")
interseccion = my_set_2 & my_set_1
print(interseccion)
intesect = my_set_1.intersection(my_set_2)
print(intesect)  

print("\nDiferencia: ")
diferencia = my_set_1 - my_set_2
print(diferencia)
diferencia = my_set_2.difference(my_set_1)
print(diferencia)

print("\nDiferencia Simetrica: ")
simetric_difference = my_set_1 ^ my_set_2
print(simetric_difference)
simetric_difference2 = my_set_1.symmetric_difference(my_set_2)
print(simetric_difference2)

  
