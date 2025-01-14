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
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_list)
print("Añade un elemento al final")
my_list.append(9)
print(my_list)
print("Añade un elemento al principio")
my_list.insert(0, 0)
print(my_list)
print("Añade varios elementos en bloque al final")
my_list.extend([10, 11])
print(my_list)
print("Añade varios elementos en bloque en una posición")
my_list[2:2] = [-1, -2]
print(my_list)
print("Elimina un valor en una posición concreta")
del my_list[7]
print(my_list)
print("Actualiza el valor de un elemento en una posición concreta")
my_list[5] = "Nuevo dato"
print(my_list)
print("Comprobar si un elemento está en un conjunto")
print(4 in my_list)
print("Elmina todo el contenido del conjunto")
my_list.clear()
print(my_list)



""" 
  * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */
"""

my_set1 = {2, 3, 4, 5}
my_set2 = {3, 5, 6, 8}


print(f"Conjunto 1: {my_set1}")
print(f"Conjunto 2: {my_set2}")
print(f"Unión de conjuntos: {my_set1.union(my_set2)}")
print(f"Intersección de conjuntos: {my_set1.intersection(my_set2)}")
print(f"Diferencia de conjuntos: {my_set1.difference(my_set2)}")
print(f"Diferencia simétrica de conjuntos: {my_set1.symmetric_difference(my_set2)}")