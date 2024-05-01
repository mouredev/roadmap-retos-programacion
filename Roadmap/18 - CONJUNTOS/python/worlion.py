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
