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
 * - Elimina todo el contenido del conjunto. '''

#Creación de conjuntos
conjunto1 = {1, 2, 3, 4}
print(conjunto1)

#Añadiendo elemento al Final
conjunto1.add(5)
print(conjunto1)

#Añadiendo elemento al Comienzo
conjunto2 = [1,2,3,4]
conjunto2.insert(0, 0.5)
print(conjunto2)
#Añade varios elementos en bloque al final.
conjunto2.extend({6, 7, 8})
print(conjunto2)

#Añade varios elementos en bloque en una posición concreta.
conjunto2[2:3]=[22,23]
print(conjunto2)

#Elimina un elemento en una posición concreta.
del conjunto2[2]
print(conjunto2)

#Añade varios elementos en bloque en una posición concreta.
conjunto2[2] = "Perro"
print(conjunto2)

# Comprueba si un elemento está en un conjunto
elemento = 5
if elemento in conjunto2:
    print(f"El elemento {elemento} está en el conjunto.")
else:
    print(f"El elemento {elemento} no está en el conjunto.")

# Elimina todo el contenido del conjunto
conjunto2.clear()
print("Conjunto después de eliminar todo el contenido:", conjunto2)

"""
* EJERCICIO #2:
* Muestra ejemplos de las siguientes operaciones con conjuntos:
* - Unión.
* - Intersección.
* - Diferencia.
* - Diferencia simétrica.
"""

#Union, existen dos formas
A = {1,2,3,4}
B = {5,6,7,8}

print(A | B)
print(A.union(B))

#Intersección.
A = {1, 3, 5}
B = {1, 2, 3}
print('Intersección usando &:', A & B)
print('Intersección usando intersection():', A.intersection(B))

#Diferencia
A = {2, 3, 5}
B = {1, 2, 6}
print('Diferencia usando - :', A - B)
print('Diferencia usando difference():', A.difference(B))
print('Diferencia usando - :', B - A)
print('Diferencia usando difference():', B.difference(A))

#Diferencia Simétrica
A = {2, 3, 5}
B = {1, 2, 6}
print('Usando ^:', A ^ B)
print('Usando symmetric_difference():', A.symmetric_difference(B)) 