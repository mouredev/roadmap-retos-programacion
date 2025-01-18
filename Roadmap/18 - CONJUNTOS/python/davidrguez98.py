""" /*
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
 */ """

#EJERCICIO

data_base = [1, 2, 3, 4, 5]

data_base.append(6)
print(data_base)

data_base.insert(0, 0)
print(data_base)

data_base.extend([7, 8, 9])
print(data_base)

data_base[2:2] = [-1, -2, -3]
print(data_base)

data_base.pop(2)
print(data_base)

data_base[2] = 2
print(data_base)

print(data_base.index(4))

data_base.clear()
print(data_base)

#DIFICULTAD EXTRA

data_base_1 = {1, 2, 3, 4, 5}
data_base_2 = {1, 2, 6, 7, 8}

print(data_base_1.union(data_base_2))

print(data_base_1.intersection(data_base_2))

print(data_base_1.difference(data_base_2))

print(data_base_1.symmetric_difference(data_base_2))