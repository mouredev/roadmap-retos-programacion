"""
 * EJERCICIO: Conjuntos
"""

my_list = ["b", "c"]
print(f"Mi lista: {my_list}")

# Añade un elemento al final.
my_list.append("g")
print(f" - Añade un elemento al final: {my_list} ✅")

# Añade un elemento al principio.
my_list = ["a"] + my_list
print(f" - Añade un elemento al principio: {my_list} ✅")

# Añade varios elementos en bloque al final.
my_list.extend(["h", "i"])
print(f" - Añade varios elementos en bloque al final: {my_list} ✅")

# Añade varios elementos en bloque en una posición concreta.
index = 3
my_list[index:index] = ["D", "e", "f", "g"]
print(f" - Añade varios elementos en bloque en una posición concreta: {my_list} ✅")

# Elimina un elemento en una posición concreta.
del my_list[6]
print(f" - Elimina un elemento en una posición concreta: {my_list} ✅")

# Actualiza el valor de un elemento en una posición concreta.
my_list[3] = "d"
print(f" - Actualiza el valor de un elemento en una posición concreta: {my_list} ✅")

# Comprueba si un elemento está en un conjunto.

print(f" - Comprueba si un elemento ('g') está en un conjunto: {'g' in my_list} ✅")
print(f" - Comprueba si un elemento ('z') está en un conjunto: {'z' in my_list} ✅")

# Elimina todo el contenido del conjunto.
my_list.clear()
print(f" - Elimina todo el contenido del conjunto.: {my_list}")


"""
 * DIFICULTAD EXTRA (opcional):

"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

set_1 = {'a', 'b', 'c'}
print(f"Set A: {set_1}")
set_2 = {'c', 'e', 'f'}
print(f"Set C: {set_2}")

# Unión: ...otro conjunto, cuyos elementos son los mismos de los conjuntos iniciales.
print(f"Unión (Están en A o en B): { set_1.union(set_2)}")

# Intersección: ... otro conjunto que contiene los elementos comunes a los conjuntos partida
print(f"Intersección (Están en A y en B): { set_1.intersection(set_2)}")

# Diferencia: ...otro conjunto con los elementos del primer conjunto sin los elementos del segundo conjunto
print(f"Diferencia (Están en A pero no en B): { set_1.difference(set_2)}")

# Diferencia simétrica: otro conjunto que contiene a aquellos elementos que pertenecen a cada uno de los conjuntos iniciales, pero no a ambos a la vez
print(f"Diferencia simétrica (Están en A pero no en B o viceversa): { set_1.symmetric_difference(set_2)}")