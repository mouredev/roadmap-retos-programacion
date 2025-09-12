import os
os.system('clear')
os.system('cls')


""" * EJERCICIO:
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
 """

my_list = [1,7,0,2,4,6]
print("La lista original:            ", my_list)
my_list.append(8)

print("Le añadimos un 8 al final:    ",my_list)

my_list.insert(0,3)

print("Le añadimos un 3 al principio:",my_list)


my_tuple = "Hola", True, (1,2,3)
print("Creamos esta tupla:           ",my_tuple)
[my_list.insert(3,my_tuple[i]) for i in range(2,-1,-1)]

print("Insertamos los elementos de la tupla en la lista en la posición 3:",my_list)
hola = "Hola" in my_list
print ("¿El elemento \"Hola\" está en la lista? ", hola )
my_list.clear()
print("Borramos todo el contenido de la lista, ahora la lista es esta: ", my_list)
print('\n')

"""* DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica."""

set1 = {"C", "Kotlin", "Swift", "C#", "Java", "Rust", "Javascript", "PhP", "Python", "R", "Ruby", "Scala"}
set2 = {"C++", "Dart", "Python", "Cobol", "Javascript", "Pascal", "Abap", "Typescript", "Java", "Fortran"}

print("### UNIÓN ###")
print(set1 | set2)# Muestra todos los elementos de ambos sets sin repeticiones
print(set1.union(set2))# Muestra todos los elementos de ambos sets sin repeticiones
print()

print("### INTERSECCIÓN ###")
print(set1.intersection(set2))# Muestra únicamente los elementos que existen a la vez en ambos sets
print(set2 & set1)# Muestra únicamente los elementos que existen a la vez en ambos sets
print()

print("### DIFERENCIA ###")
print(set1 - set2)# Muestra los elementos que sólo existen en set1 y no están en set2 ni en ambos
print(set1.difference(set2))# Muestra los elementos que sólo existen en set1 y no están en set2 ni en ambos
print(set2 - set1)# Muestra los elementos que sólo existen en set2 y no están en set1 ni en ambos
print(set2.difference(set1))# Muestra los elementos que sólo existen en set2 y no están en set1 ni en ambos
print()

print("### DIFERENCIA SIMÉTRICA ###")
print(set1 ^ set2)# Muestra los elementos de ambos sets que están en uno u otro set pero no en ambos 
print(set1.symmetric_difference(set2))# Muestra los elementos de ambos sets que están en uno u otro set pero no en ambos 






