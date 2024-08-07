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

# EJERCICIO:

mi_conjunto = set([1, 2, 3, 4])
# Añade un elemento al final
mi_conjunto.add(5)
print(mi_conjunto)
# Añade un elemento al principio
nuevo_conjunto = {1}
print(nuevo_conjunto)
# Añade varios elementos en bloque al final
elementos = {8, 9, 10}
mi_conjunto.update(elementos)
print(mi_conjunto)
# Comprueba si un elemento está en un conjunto
elemento_conjunto = 2 in mi_conjunto
print(elemento_conjunto)
# Elimina todo el contenido del conjunto
mi_conjunto.clear()
print(mi_conjunto)

# DIFICULTAD EXTRA:

st1 = {1, 2, 3}
st2 = {4, 5, 6}
# Unión
print(st1.union(st2))
# Intersección
print(st1.intersection(st2))
# Diferencia
print(st1.difference(st2))
st1.difference_update(st2)
print(st1)
