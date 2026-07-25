"""
Ejercicio
"""

data = [1, 2, 3, 4, 5]
print(f"Estructura inicial: {data}")

data.append(6)
print(f"Añadiendo elemento al final: {data}")

data.insert(0, 0)
print(f"Añadiendo elemento al principio: {data}")

data.extend([7, 8, 9])
print(f"Añadiendo elementos al final: {data}")

data[3:3] = [-1, -2, -3]
print(f"Añadiendo elementos en una posición: {data}")

del data[3]
print(f"Eliminando un elemento concreto: {data}")

data[4] = -1
print(f"Actualizando un elemento concreto: {data}")

print(f"Comprobar si un elemento existe: {-1 in data}")

print(f"Eliminar el contenido: {data.clear()}")

"""
Extra
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

print(f"Unión: {set_1.union(set_2)}")

print(f"Intersección: {set_1.intersection(set_2)}")

print(f"Diferencia: {set_1.difference(set_2)}")
print(f"Diferencia: {set_2.difference(set_1)}")

print(f"Diferencia simétrica: {set_1.symmetric_difference(set_2)}")
