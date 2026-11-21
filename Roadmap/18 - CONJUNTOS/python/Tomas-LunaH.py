# EJERCICIO:
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.

#Agregar elementos al final
numers = [1,2,3,4,5]
print(numers)
numers.append(6)
print(numers)

#Agregar elementos al inicio
numers.insert(0,0)
print(numers)

#Agregar varios elementos al final
numers.extend([7,8,9])
print(numers)

#Insertar varios elementos en una posicion
numers[0:0] = [-2,-1]
print(numers)

#Modificar datos en una posision concreta
numers[1] = -1.1
print(numers)

#Eliminar un dato por valor
numers.remove(-2)
print(numers)

#Eliminar un dato en una posicion concreta
numers.pop(0)
print(numers)

del numers[0]
print(numers)

#Buscar elementos
print(10 in numers)
print(2 in numers)

#Obtener la posicion
print(numers.index(5))

#Contar elementos
print(numers.count(1))

#Ordenar una lista
num_sort = [1,6,3,5,2,4]
num_sort.sort()
print(num_sort)
#descendente
num_sort.sort(reverse=True)
print(num_sort)

#  DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.



set1 = {1,2,3,4}
set2 = {1,4,6,2,5,7,}

# @ Union
print( set1 | set2)
print(set1.union(set2))

# @ Interseccion

print(set1 & set2)
print(set1.intersection(set2))

# @ Diferencia

print(set1 - set2)

# @ Diferenia simetrica
print(set1^set2)
