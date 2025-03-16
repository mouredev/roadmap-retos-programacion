"""* EJERCICIO:
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
 * - Diferencia simétrica."""

conjunto = ['a', 'b', 'c', 'd']
print(f'Mi conjunto es {conjunto}')
# Añade un elemento al final.
conjunto.append('e')
print(f'Mi conjunto es {conjunto}')
# Añade un elemento al principio.
conjunto.insert(0,'a')
print(f'Mi conjunto es {conjunto}')
# Añade varios elementos en bloque al final.
conjunto.extend(['y', 'z'])
print(f'Mi conjunto es {conjunto}')
# Añade varios elementos en bloque en una posición concreta.
conjunto[2:2] = ['d', 'h', 'r']
print(f'Mi conjunto es {conjunto}')
# Elimina un elemento en una posición concreta.
del conjunto[2]
print(f'Mi conjunto es {conjunto}')
# Actualiza el valor de un elemento en una posición concreta.
conjunto[3] = 'ñ'
print(f'Mi conjunto es {conjunto}')
# Comprueba si un elemento está en un conjunto.
print(f'¿El elemento está en el conjunto? {'t' in conjunto}')
# Elimina todo el contenido del conjunto.
conjunto.clear()
print(f'Mi conjunto es {conjunto}')

# EXTRA
conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'b', 'c', 'd'}
# - Unión.
print(conjunto1.union(conjunto2))

# - Intersección
print(conjunto1.intersection(conjunto2))

# - Diferencia
print(conjunto1.difference(conjunto2))

# - Diferencia simétrica:
print(conjunto1.symmetric_difference(conjunto2))