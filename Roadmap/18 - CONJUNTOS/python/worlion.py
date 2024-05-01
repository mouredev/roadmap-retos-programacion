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

# custom function
def insert(original: list, new_elements: list, index: int) -> list:
    if(index <0 or index > len(original)):
        raise IndexError("Index out of bound error")
    return original[0:index] + new_elements + original[index:len(original)]

my_list = insert(my_list, ["D", "e", "f", "g"], 3)
print(f" - Añade varios elementos en bloque en una posición concreta: {my_list} ✅")

# Elimina un elemento en una posición concreta.
del my_list[6]
print(f" - Elimina un elemento en una posición concreta: {my_list} ✅")

# Actualiza el valor de un elemento en una posición concreta.
my_list[3] = "d"
print(f" - Actualiza el valor de un elemento en una posición concreta: {my_list} ✅")

# Comprueba si un elemento está en un conjunto.

# custom function
def contains(value, l: list) -> bool:
    try:
        l.index(value)
        return True
    except ValueError:
        # print("not found")
        return False

print(f" - Comprueba si un elemento ('g') está en un conjunto: {contains('g', my_list)} ✅")
print(f" - Comprueba si un elemento ('Z') está en un conjunto: {contains('Z', my_list)} ✅")

# Elimina todo el contenido del conjunto.
my_list.clear()
print(f" - Elimina todo el contenido del conjunto.: {my_list}")


