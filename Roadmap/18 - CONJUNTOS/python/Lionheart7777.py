# EJERCICIO con Listas
data = [1, 2, 3, 4, 5]
print(f"Estructura inicial:{data}")

data.append(6)
print(f"Añadiendo elemento al final:{data}")

data.insert(0, 0)
print(f"Añadiendo elemento al inicio:{data}")

data.extend([7, 8, 9])
print(f"Añadiendo elementos al final:{data}")

data[3:3] = [-1, -2, -3]
print(f"Añadiendo elementos en una posicion:{data}")

del data[3]
print(f"Eliminando en elemento concreto: {data}")

data[4] = 99
print(f"Actualizando el elemento posición 4: {data}")

print(f"Comprobar si el elemento 99 existe: {99 in data}")

print(f"Comprobar si el elemento 100 existe: {100 in data}")

data.clear()
print(f"Eliminar el contenido:{data}")

# EXTRA con sets

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

# UNION
print(f"Unión: {set_1.union(set_2)}")
print(f"Unión: {set_1 | set_2}")

# INTERSECCIÓN
print(f"Intersección: {set_1.intersection(set_2)}")
print(f"Intersección: {set_1 & set_2}")

# DIFERENCIA set_1 - set_2
print(f"Diferencia set_1 con set_2: {set_1.difference(set_2)}")
print(f"Diferencia: {set_1 - set_2}")

# DIFERENCIA set_2 - set_1
print(f"Diferencia set_2 con set_1: {set_2.difference(set_1)}")
print(f"Diferencia: {set_2 - set_1}")

# DIFERENCIA SIMÉTRICA, lo que no tienen los conjutos,uno del otro
print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}")
print(f"Diferencia simétrica: {set_1 ^ set_2}")
