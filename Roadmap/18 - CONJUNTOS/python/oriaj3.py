"""
18 - Conjuntos

Autor de la solución: Oriaj3	

Teoria: 

Los conjuntos son una estructura de datos que permite almacenar elementos de forma no ordenada.
En Python, los conjuntos se definen con llaves {} y los elementos se separan por comas.
Los conjuntos no permiten elementos duplicados, por lo que si se añade un elemento que ya existe, no se añadirá.
Los conjuntos son mutables, por lo que se pueden añadir o eliminar elementos.
Los conjuntos no permiten acceder a los elementos por índice, ya que no tienen un orden definido.
Los conjuntos son útiles para realizar operaciones de conjuntos, como unión, intersección, diferencia y diferencia simétrica.

Ejemplo:
Conjunto con mamíferos
mamiferos = {"perro", "gato", "elefante", "jirafa"}

Operaciones con conjuntos
*add - Añade un elemento al conjunto
*update - Añade varios elementos al conjunto
*remove - Elimina un elemento del conjunto
*discard - Elimina un elemento del conjunto si existe
*clear - Elimina todos los elementos del conjunto
*in - Comprueba si un elemento está en el conjunto
*union - Realiza la unión de dos conjuntos
*intersection - Realiza la intersección de dos conjuntos
*difference - Realiza la diferencia de dos conjuntos
*symmetric_difference - Realiza la diferencia simétrica de dos conjuntos

"""

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

#Conjunto de mamíferos con lista
mamiferos = ["perro", "gato", "elefante", "jirafa"]
print(mamiferos)

mamiferos.append("vaca") 
print(mamiferos)

mamiferos.insert(0, "mono")
print(mamiferos)

mamiferos.extend(["cabra","oveja"])
print(mamiferos)

mamiferos[2:2]= [ "caballo", "llama"]
print(mamiferos)

del mamiferos[2] 
print(mamiferos)

mamiferos[3] = "gorila"
print(mamiferos)

print(f"Está gorila? {'Sí' if 'gorila' in mamiferos else 'No'}")

mamiferos.clear()
print(mamiferos)



"""
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */
"""

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {1, 2, 3, 4, 6, 7}

print(f"Unión: {conjunto1.union(conjunto2)}")
print(f"Intersección: {conjunto1.intersection(conjunto2)}")
print(f"Diferencia: {conjunto1.difference(conjunto2)}")
print(f"Diferencia: {conjunto2.difference(conjunto1)}")
print(f"Diferencia simétrica: {conjunto1.symmetric_difference(conjunto2)}")
print(f"Diferencia simétrica: {conjunto2.symmetric_difference(conjunto1)}")

