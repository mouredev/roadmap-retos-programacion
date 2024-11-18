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
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 """
 
conjunto = [1,2,3,4,5]
#Añdir un elemento al final
conjunto.append(6)
print(conjunto)
#Añadir un elemento al principio
conjunto.insert(0,0)
print(conjunto)
#Añadir varios elementos al final
conjunto.extend([7,8,9])
print(conjunto)
#Añadir varios elementos en un posicion concreta
conjunto[3:3]=[10,11,12]
print(conjunto)
#Eliminar un elemento de una posicion concreta
del conjunto[3]
print(conjunto)
#Actualizar el valor de un elemento en una posicion concreta
conjunto[3] = 3
#Comprobar si un elemento esta en el conjunto
n =  5
if(n in conjunto):
    print(f"El elemento {n} esta en el conjunto.")
else:
    print(f"El elemento {n} no esta en el conjunto.") 
conjunto.clear()
print(conjunto)

#Extra
conjunto_a = {20,21,22,23,24,25}
conjuto_b = {19,21,18,23,17,25}
#Union
conjunto = conjunto_a.union(conjuto_b)
print(conjunto)
#Interseccion
conjunto = conjunto_a.intersection(conjuto_b)
print(conjunto)
#Diferencia
conjunto = conjunto_a.difference(conjuto_b)
print(conjunto)
#Diferencia simetrica
conjunto = conjunto_a.symmetric_difference(conjuto_b)
print(conjunto)
