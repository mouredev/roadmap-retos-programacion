"""/*
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

data = [1,2,3,4,5]

print(f"Conjunto de datos inicial {data}")

data.append(6)

print(f"Añadiendo un dato al final {data}")

data.insert(0,0)

print(f"Añadiendo un dato al inicio {data}")

data.extend([7,8,9])

print(f"Añadiendo elementos al final {data}")

data[3:3]=[3.1,3.2,3.3]

print(f"Añadiendo elementos en una posicion {data}")

del data[3]

print(f"Eliminando un elemento {data}")

data[5]=3.2

print(f"Modificando un elemento {data}")

print(f"Comprobando si un elemento existe {3.2 in data}")
print(f"Comprobando si un elemento existe {3.5 in data}")

data.clear()

print(f"limpiando los datos de la estructura {data}")

"""
Extra
"""

Conjunto01={0,1,2,3,4,5}
Conjunto02={1,2,3,4,6,7}

print(f"Conjunto de elementos iniciales Conjunto01 {Conjunto01}")
print(f"Conjunto de elementos iniciales Conjunto02 {Conjunto02}")

Conjunto03=Conjunto01.union(Conjunto02)

print(f"union de conjuntos 01 y 02 {Conjunto03}")

Conjunto03=Conjunto01.intersection(Conjunto02)

print(f"Intersección de conjuntos 01 y 02 {Conjunto03}")

Conjunto03=Conjunto01.difference(Conjunto02)

print(f"Diferencia de conjuntos 01 y 02 {Conjunto03}")

Conjunto03=Conjunto01.symmetric_difference(Conjunto02)

print(f"Diferencia simetrica entre conjuntos 01 y 02 {Conjunto03}")
