#18 CONJUNTOS

"""
/*
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
 */
"""

datos: list = [1, 2, 3, 4]
print("Lista inicial:", datos)

# Añadir datos
datos.append(5)
print("Después de añadir 5:", datos)

# Añadir dato al inicio
datos.insert(0, 0)
print("Después de insertar 0 al inicio:", datos)

# Añadir varios datos al final
datos.extend([6, 7, 8])
print("Después de extender con 6, 7 y 8:", datos)

# Añadir dato en posición específica
datos[4:4] = [5, 8, 13]
print("Después de insertar 5, 8 y 13 en la posición 4:", datos)

# Eliminar un dato concreto
del datos[4]
print("Después de eliminar el dato en la posición 4 con 'del':", datos)

datos.pop(4)
print("Después de eliminar el dato en la posición 4 con 'pop':", datos)

# Actualizar elemento
datos[4] = 10
print("Después de actualizar el elemento en la posición 4 a 10:", datos)

# Comprobar si un elemento está en el conjunto
comprobando = 8 in datos
print("Comprobando si 8 está en la lista:", comprobando)

# Eliminar elementos de la lista
datos.clear()
print("Después de limpiar la lista:", datos)

# EXTRA

conjunto1: set = {1, 1, 2, 3, 5, 8}
conjunto2: set = {8,13, 21, 34, 55, 89, 144}

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# Unión de conjuntos
union = conjunto1.union(conjunto2)
print("Unión de conjunto1 y conjunto2:", union)

# Intersección de conjuntos
interseccion = conjunto1.intersection(conjunto2)
print("Intersección de conjunto1 y conjunto2:", interseccion)

# Diferencia de conjuntos
diferencia = conjunto1.difference(conjunto2)
print("Diferencia de conjunto1 y conjunto2:", diferencia)

# Diferencia simétrica de conjuntos
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica de conjunto1 y conjunto2:", diferencia_simetrica)
