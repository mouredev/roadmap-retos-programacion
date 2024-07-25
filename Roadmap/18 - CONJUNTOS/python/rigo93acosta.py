'''
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
'''

'''
Ejercicio:
'''

# Crear un conjunto de datos
data = [1, 2, 3, 4, 5]
print(f"Estructura incial: {data}")

# Añadir un elemento al final
data.append(6)
print(f"Añadiendo elemento al final: {data}")

# Añadir un elemento al principio
data.insert(0, 0)
print(f"Añadiendo elemento al principio: {data}")

# Añadir varios elementos en bloque al final
data.extend([7, 8, 9])
print(f"Añadiendo elementos en bloque: {data}")

# Añadir varios elementos en bloque en una posición concreta
data[3:3] = [10, 11, 12] # Slice: Inserta en la posicion 3
print(f"Añadiendo elementos en posición concreta: {data}")

# Eliminar un elemento en una posición concreta
del data[3]
# data.pop(3) # Otro método
print(f"Eliminando elementos en posición concreta: {data}")

# Actualizar el valor de un elemento en una posición concreta
data[3] = 13
print(f"Actualizando elementos en posición concreta: {data}")

# Comprobar si un elemento está en un conjunto
print(f"El elemento 13 está en el conjunto: {13 in data}")

# Eliminar todo el contenido del conjunto
data.clear()
print(f"Eliminando todo el contenido del conjunto: {data}")

'''
Dificultad extra:
'''

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

# Unión
print(f"Unión de conjuntos: {set_1.union(set_2)}")

# Intersección
print(f"Intersección de conjuntos: {set_1.intersection(set_2)}")

# Diferencia
print(f"Diferencia de conjuntos: {set_1.difference(set_2)}")
print(f"Diferencia de conjuntos: {set_2.difference(set_1)}")

# Diferencia simétrica
print(f"Diferencia simétrica de conjuntos: {set_1.symmetric_difference(set_2)}")