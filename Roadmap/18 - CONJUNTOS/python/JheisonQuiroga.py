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
"""

# 1. Creando un Conjunto de datos
data = [1, 2, 3]

# 2. Agregando un elemento al final
data.append(4)

# 3. Añade un elemento al principio
data.insert(0, 0)

# 4. Añade varios elementos al final.
data.extend([5, 6])
print(data) 

# 5. Añadiendo varios elementos en una posición concreta
data[0:0] = [-2, -1]

# 6. Eliminando un elemento en una posición concreta
deleted_element = data.pop(0)
print("Elemento eliminado:", deleted_element) # Elemento eliminado: -2

# 7. Actualiza el valor de un elemento en una posición concreta
data[3] = 7
print(data) # [-1, 0, 1, 7, 3, 4, 5, 6]

# 8. Comprueba si un elemento existe en un conjunto
cero_exists = 0 in data
print("El cero existe dentro de data?:", cero_exists)

# 9. Elimina todo el contenido

data.clear()
print(data) # []


"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */
"""

print("-" * 5, "Operaciones con Conjuntos", "-" * 5)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. Unión

c = a.union(b)
print(c) # {1, 2, 3, 4, 5, 6}

# 2. Intersección

inter = a & b
print(inter) # {3, 4}

# 3. Diferencia
dif = a.difference(b)
print(dif)  # {1, 2}

dif = a - b
print(dif)

# 4. Diferencia simétrica
sim_difference = a.symmetric_difference(b)
print(sim_difference) # {1, 2, 5, 6}