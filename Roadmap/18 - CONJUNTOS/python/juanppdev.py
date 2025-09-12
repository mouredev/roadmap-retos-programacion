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

# Crear un conjunto de datos (lista)
datos = [1, 2, 3, 4, 5]

# Añadir un elemento al final
datos.append(6)
print("Añadir al final:", datos)

# Añadir un elemento al principio
datos.insert(0, 0)
print("Añadir al principio:", datos)

# Añadir varios elementos en bloque al final
datos.extend([7, 8, 9])
print("Añadir varios al final:", datos)

# Añadir varios elementos en bloque en una posición concreta
datos[3:3] = [10, 11, 12]
print("Añadir varios en posición 3:", datos)

# Eliminar un elemento en una posición concreta
del datos[4]
print("Eliminar en posición 4:", datos)

# Actualizar el valor de un elemento en una posición concreta
datos[2] = 99
print("Actualizar en posición 2:", datos)

# Comprobar si un elemento está en el conjunto
elemento = 99
print(f"¿Está {elemento} en el conjunto?:", elemento in datos)

# Eliminar todo el contenido del conjunto
datos.clear()
print("Eliminar todo el contenido:", datos)


"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

# Crear dos conjuntos de datos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Unión
union = conjunto1.union(conjunto2)
print("Unión:", union)

# Intersección
interseccion = conjunto1.intersection(conjunto2)
print("Intersección:", interseccion)

# Diferencia
diferencia = conjunto1.difference(conjunto2)
print("Diferencia:", diferencia)

# Diferencia simétrica
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferencia simétrica:", diferencia_simetrica)
