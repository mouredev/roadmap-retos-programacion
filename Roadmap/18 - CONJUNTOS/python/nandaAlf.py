# /*
#  * EJERCICIO:
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
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.
#  */

myList=[1,2,3,4,5]

# Añade un elemento al final.
myList.append(6)

# Añade un elemento al principio.
myList.insert(0,0)

# Añade varios elementos en bloque al final.
myList.extend(['a','b'])

# Añade varios elementos en bloque en una posición concreta.
myList[2:3]=['c','d']

# Elimina un elemento en una posición concreta.
del myList[3]

# Actualiza el valor de un elemento en una posición concreta.
myList[2]='hello'

# Comprueba si un elemento está en un conjunto.
print(10 in myList)

# Elimina todo el contenido del conjunto.
myList.clear()

#EXTRA
set1={1,2,3,4,5}
set2={1,3,5,7,9}

#Union
print(set1|set2)

#Interseccion
print(set1&set2)

#Diferencia
print(set1-set2)

#Diferencia simetrica
print(set1^set2)