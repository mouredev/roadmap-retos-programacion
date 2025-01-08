# #18 CONJUNTOS


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
"""
data_set = [1,2,3,4,5,6]
print (f"Datos de la lista: {data_set}")

data_set.append(7)
print (f"Elemento añadido al final de la lista: {data_set}")

data_set.insert(0,0)
print (f"Elemento añadido al principio de la lista: {data_set}")


data_set.extend([8,9,10])
print (f"Elementos añadidos en bloque un posición específica de la lista: {data_set}")


data_set[2:2]=["a","b"]
print (f"Elementos añadidos en bloque un posición específica de la lista: {data_set}")

del data_set[3]
print (f"Elimina un elemento en una posición concreta de la lista: {data_set}")

data_set[10]="z"
print (f"Actualiza el valor de un elemento en una posición concreta de la lista: {data_set}")

print (f" Comprueba si un elemento está en la lista {'a' in data_set}")

print (f"Conjunto eliminado, contenido de la lista:  {data_set.clear()}")
"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 """


set_a = {'a','b','c','d'}
set_b = {'a','b','e','f'}

print (set_a)
print (set_b)
print (f"Unión : {set_a.union(set_b)}")
print (f"Intersección : {set_a.intersection(set_b)}")
print (f"Diferencia a - b : {set_a.difference(set_b)}")
print (f"Diferencia b - a : {set_b.difference(set_a)}")
print (f"Diferencia simétrica : {set_a.symmetric_difference(set_b)}")