# RETO 18 CONJUNTOS

"""
CREAR CONJUNTO DE DATOS Y REALIZAR OPERACIONES
"""

data = [1, 2, 3, 4]
print(f"Initial structure: {data}")

# AÑADE UN ELEMENTO AL FINAL
data.append(5)
print(f"Adding element to the end: {data}")

# AÑADE UN ELEMENTO AL PRINCIPIO
data.insert(0, 0)
print(f"Adding element to the start: {data}")

# AÑADE VARIOS ELEMENTOS EN BLOQUE AL FINAL
data.extend([6, 7, 8])
print(f"Adding block elements to the end: {data}")

# AÑADE VARIOS ELEMENTOS EN BLOQUE EN UNA POSICIÓN ESPECÍFICA
data[3:3] = [-1, -2, -3]
print(f"Adding elements in bulk at a specific position: {data}")

# ELIMINA UN ELEMENTO EN UN POSICIÓN CONCRETA
del data [3]
print(f"Deleting an element at a specific position: {data}")

# ACTUALIZA EL VALOR DE UN ELEMENTO EN UNA POSICIÓN CONCRETA
data[2] = +1
print(f"Updating a specific element: {data}")
print(f"Check if an element exists: {+1 in data}")
print(f"Delete content: {data.clear()}")


# Extra

print("🧩 DIFICULTAD EXTRA - EJEMPLOS DE OPERACIONES CON CONJUNTOS 🧩")

first_set = {1, 2, 3, 4, 5, 6}
second_set = {1, 2, 3, 4, 5, 6, 7, 8}

# UNIÓN
print(f"Union: {first_set.union(second_set)}")

# INTERSECCIÓN
print(f"Intersection: {first_set.intersection(second_set)}")

# DIFERENCIA
print(f"Difference: {first_set.difference(second_set)}")
print(f"Difference: {second_set.difference(first_set)}")

# DIFERENCIA SIMÉTRICA
print(f"Symmetrical difference: {first_set.symmetric_difference(second_set)}")
