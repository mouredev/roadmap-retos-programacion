"""
EJERCICIO:
Utilizando tu lenguaje crea un conjunto de datos y realiza las 
siguientes operaciones (debes utilizar una estructura que las soporte):

- Añade un elemento al final.
- Añade un elemento al principio.
- Añade varios elementos en bloque al final.
- Añade varios elementos en bloque en una posición concreta.
- Elimina un elemento en una posición concreta.
- Actualiza el valor de un elemento en una posición concreta.
- Comprueba si un elemento está en un conjunto.
- Elimina todo el contenido del conjunto.

DIFICULTAD EXTRA (opcional):
Muestra ejemplos de las siguientes operaciones con conjutos:
- Unión.
- Intersección.
- Diferencia.
- Diferencia simétrica.

by adra-dev
"""
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
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

set1 = {-3, -2, -1, 0, 1, 2, 3}
set2 = {0, 1, 2, 3}

print(f"Union {set1.union(set2)}")

print(f"Intersección: {set1.intersection(set2)}")
print(f"Intersección: {set2.isdisjoint(set1)}")

print(f"Diferencia: {set1.difference(set2)}")
print(f"Diferencia: {set2.difference(set1)}")

print(f"Diferencia: {set2.issubset(set1)}")

print(f"Diferencia simétrica: {set1.symmetric_difference(set2)}")