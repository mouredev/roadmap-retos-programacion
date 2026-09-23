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

numeros: set = set()

numeros.add(1)
numeros.add(2)
numeros.add(3)
numeros.add(4)
numeros.add(5)
numeros.add(6)
numeros.add(7)
numeros.add(8)
numeros.add(9)
numeros.add(0)

copy_numeros = numeros.copy()

print("\n", numeros, "\n")

numbers = {11, 12, 13, 14, 15, 16, 17, 18, 19}

numeros |= numbers

print("\n", numeros, "\n")

numeros.pop()

print("\n", numeros, "\n")

print(15 in numeros, "\n")

numeros.clear()

print("\n", numeros, "\n")

print(copy_numeros, numbers)

print("Union", copy_numeros.union(numbers))
print("Union", copy_numeros | numbers)
print(copy_numeros)
print("Intersección", copy_numeros & numbers)
print("Intersección", copy_numeros.intersection(numbers))
numbers.add(0)
print("Intersección", copy_numeros & numbers)
print("Diferencia", copy_numeros - numbers)
print("Diferencia", copy_numeros.difference(numbers))
print(numbers)

print("Diferencia simétrica", copy_numeros ^ numbers)