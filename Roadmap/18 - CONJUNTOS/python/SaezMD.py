#18 Conjuntos
"""
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes operaciones (debes utilizar una estructura que las soporte):
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
"""

#create elememt:
dataSet = ["a", "b", 1, 2]
#add element to the end:
dataSet.append("last")
#add element to the first:
dataSet.insert(0,"first")
#add several items as a block to the end:
for unit in ["very last", "the end"]:
    dataSet.append(unit)
#add several items as a block to specific position:
position = 2
for unit in ["middle", "another"]:
    dataSet.insert(position,unit)
    position += 1
#delete an element in a position:
dataSet.pop(3)
#update the element in a position: 
dataSet.pop(5)
dataSet.insert(5,"update!")
#check if element is a list:
if "very last" in dataSet:
    print("yes")
else:
    print("no")
#delete all:
dataSet.clear()

print(dataSet)

#EXTRA:

#join:
list1 = ["a", "b", "c"]
list2 = [1,2,3]

join00 = list1 + list2
print(join00)

#intersection:
list3 = [1,2,3,4,5]
list4 = [6,7,8,9,0,1,2]
intersect = []
for value in list3:
    if value in list4:
        intersect.append(value)

print("Intersect:",intersect)

#difference:
difference = []
for value in list3:
    if value not in list4:
        difference.append(value)

print("Difference:",difference)

#symmetric:
difference = []
for value in list3:
    if value not in list4:
        difference.append(value)
for value in list4:
    if value not in list3:
        difference.append(value)

print("Symmetric:",difference)
