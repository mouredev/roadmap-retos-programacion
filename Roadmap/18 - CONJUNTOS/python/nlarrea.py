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
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

data = [1, 2, 3, 4, 5]
print(data)  # [1, 2, 3, 4, 5]

# Añadir un elemento al final
data.append("final")
print(data)  # [1, 2, 3, 4, 5, 'final']

# Añadir un elemento al principio
data.insert(0, "start")
print(data)  # ['start', 1, 2, 3, 4, 5, 'final']

# Añadir varios elementos en bloque al final
data.append(["final", "elements", 3])
print(data)  # ['start', 1, 2, 3, 4, 5, 'final', ['final', 'elements', 3]]

# Añadir varios elementos en bloque en una posición concreta
data.insert(2, ["more", "data", "position", 2])
print(data)
# ['start', 1, ['more', 'data', 'position', 2], 2, 3, 4, 5, 'final', ['final', 'elements', 3]]

# Elimina un elemento en una posición concreta
data.pop(3)
print(data)
# ['start', 1, ['more', 'data', 'position', 2], 3, 4, 5, 'final', ['final', 'elements', 3]]

# Actualiza el valor de un elemento en una posición concreta
data[1] = True
print(data)
# ['start', True, ['more', 'data', 'position', 2], 3, 4, 5, 'final', ['final', 'elements', 3]]

# Comprueba si un elemento está en un conjunto
print("dato" in data)  # False
print(5 in data)  # True

# Elimina todo el contenido del conjunto
data.clear()
print(data)  # []


"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5, 6, 7}

print("Union:", set_1.union(set_2))

print("Intersection:", set_1.intersection(set_2))

print("Difference:", set_1.difference(set_2))
print("Difference:", set_2.difference(set_1))

print("Symmetric difference:", set_1.symmetric_difference(set_2))
