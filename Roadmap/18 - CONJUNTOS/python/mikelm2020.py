my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# ejercicio

print("Ejercio")
print("Conjunto a trabajar")
print(my_set)
print("\nAñade un elemento al final, añadimos el 11")
my_set.add(11)
print(my_set)

print("\nAñade un elemento al principio, añadimos el 0")
my_list = list(my_set)
my_list.insert(0, 0)
my_set = set(my_list)
print(my_set)

print("\nAñade varios elementos en bloque al final, añadimos 13,14,15,16")
my_list = [13, 14, 15, 16]
my_set.update(my_list)
print(my_set)

print("\nAñade varios elementos en bloque en una dirección concreta")
print("Añadimos en la posición 2 los valores 17,18,19,20")
my_list = list(my_set)
print(f" El conjunto convertido en lista es {my_list}")
my_list[2:4] = [17, 18, 19, 20]
print(f" La lista con los elementos insertados es {my_list}")
my_set = set(my_list)
print("El conjunto resultante")
print(my_set)

print("\nElimina un elemento en una posición concreta, eliminamos el de la posición 2")
my_list = list(my_set)
del my_list[2]
my_set = set(my_list)
print(my_set)

print(
    "\nActualiza el valor de un elemento en una dirección concreta, actualiazamos el de la posición 4"
)
my_list = list(my_set)
my_list[4] = 35
my_set = set(my_list)
print(my_set)

print("\nComprueba si un elemento está en un conjunto, comprobamos si existe el 35")
print(35 in my_set)

print("\nElimina todo el contenido del conjunto")
my_set.clear()
print(my_set)


# Extra

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
my_set2 = {4, 6, 7, 8, 12, 14, 16}

print("Dificultad extra")
print("Conjuntos para trabajar")
print(f" my_set = {my_set}")
print(f" my_set2 = {my_set2}")
print("\nUnión: ")
union = my_set | my_set2
print(union)

print("\nIntersección: ")
interseccion = my_set & my_set2
print(interseccion)

print("\nDiferencia: ")
diferencia = my_set - my_set2
print(diferencia)

print("\nDiferencia simétrica: ")
simetric_difference = my_set ^ my_set2
print(simetric_difference)
