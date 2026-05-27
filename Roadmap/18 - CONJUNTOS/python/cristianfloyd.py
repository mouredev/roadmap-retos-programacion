 # EJERCICIO:
 # Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 # operaciones (debes utilizar una estructura que las soporte):
 # - Añade un elemento al final.
 # - Añade un elemento al principio.
 # - Añade varios elementos en bloque al final.
 # - Añade varios elementos en bloque en una posición concreta.
 # - Elimina un elemento en una posición concreta.
 # - Actualiza el valor de un elemento en una posición concreta.
 # - Comprueba si un elemento está en un conjunto.
 # - Elimina todo el contenido del conjunto.

from typing import Any
from random import randint

mi_lista: list[Any] = [randint(1, 5) for _ in range(7)]
mi_conjunto_1 = set[Any](mi_lista)
print(f"Lista de numeros enteros: {mi_lista}")
print(f"Mi set: {mi_conjunto_1}")

# Inicio ejercicio

# Añade un elemento al final.
mi_lista.append("final")
print(f"Lista con el elemento al final: {mi_lista}")

# Añade un elemento al principio.
mi_lista.insert(0, "A")
print(f"Lista con el elemento al principio: {mi_lista}")

# Añade varios elementos en bloque al final.
mi_lista.extend([randint(1, 5) for _ in range(3)])
print(f"Lista con los elementos en bloque al final: {mi_lista}")

# Añade varios elementos en bloque en una posición concreta.
mi_lista[2:2] = [randint(20,29) for _ in range(3)]
print(f"Lista con los elementos en bloque en una posición concreta: {mi_lista}")

# comprobar si un elemento esta en la lista
print(f"El elemento 3 esta en la lista: {"Si" if 3 in mi_lista else "NO"}")

# eliminar todo el contenido de la lista
mi_lista.clear()
print(f"Lista con todo el contenido eliminado: {mi_lista}")


 #
 # DIFICULTAD EXTRA (opcional):
 # Muestra ejemplos de las siguientes operaciones con conjuntos:
 # - Unión.
 # - Intersección.
 # - Diferencia.
 # - Diferencia simétrica.

mi_set_1 = set(["A", "B", "C", "D", "E"])
print(f"Mi set inicial: {mi_set_1}")

mi_set_2 = set(["B", "D", "F", "G", "H"])
print(f"Mi set inicial: {mi_set_2}")

# Unión de conjuntos
mi_set_union = mi_set_1 | mi_set_2
print(f"Unión de conjuntos: {mi_set_union}")
print(f"Unión de conjuntos: {mi_set_1.union(mi_set_2)}")


# Intersección de conjuntos
print(f"Intersección de conjuntos: {mi_set_1 & mi_set_2}")
print(f"Intersección de conjuntos: {mi_set_1.intersection(mi_set_2)}")

# Diferencia de conjuntos
print(f"Diferencia de conjuntos: {mi_set_1 - mi_set_2}")
print(f"Diferencia de conjuntos: {mi_set_1.difference(mi_set_2)}")

# Diferencia simétrica de conjuntos
print(f"Diferencia simétrica de conjuntos: {mi_set_1 ^ mi_set_2}")
print(f"Diferencia simétrica de conjuntos: {mi_set_1.symmetric_difference(mi_set_2)}")