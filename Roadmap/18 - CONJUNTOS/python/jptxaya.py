# # #18 CONJUNTOS

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

my_conj = [0,1,2,3,4]
print(my_conj)

print("Add element at the end")
my_conj.append(5)
print(my_conj)

print("Add a element at the beginning")
my_conj.insert(0,-1)
print(my_conj)

print("Add several items at the end")
my_conj2 = [6,7]
my_conj = my_conj + my_conj2
print(my_conj)

print("Add several items at a position")
my_conj3 = [4.5 ,4.7]
my_conj[6:6] = my_conj3
print(my_conj)

print("Delete item at specified position")
my_conj.pop(7)
print(my_conj)

print("Update a value at specified position")
my_conj[6] = 4.2
print(my_conj)

print("Check if the value exist")
try:
    my_conj.index(8)
except ValueError as ex:
    print(ex.args)

print("Delete all content")
my_conj.clear()
print(my_conj)

print("Dificultad extra")
my_conj1 = [1,2,3]
my_conj2 = [3,4,5]
print(f"Conj1:  {my_conj1}")
print(f"Conj2:  {my_conj2}")
print("Union")
my_conj_union = my_conj1 + my_conj2
print(my_conj_union)

print("Interseccion")
my_conj_inter = set(my_conj1).intersection(set(my_conj2))
print(list(my_conj_inter))

print("Difference")
my_conj_dif = set(my_conj1).difference(set(my_conj2))
print(list(my_conj_dif))

print("Symetric Difference")
my_conj_sdif = set(my_conj1).symmetric_difference(set(my_conj2))
print(list(my_conj_sdif))

