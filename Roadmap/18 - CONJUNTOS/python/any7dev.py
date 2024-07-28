""" /*
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
 */ """

#EJERCICIO
lista = [2, 4, 7, 20, 23, 6] #Crear
print(lista)

lista.append(24) #Añadir al final
print(lista)

lista.insert(0, 1) #Añadir al principio
print(lista)

lista.extend([0, 3, 10]) #Añadir en bloque al final
print(lista)

lista[5:3] = [11, 50, 30] #Añade varios elementos en una posición concreta
print(lista)

lista.pop(7) #Elimina el elemento de la posición 6
print(lista)

lista[5] = 5 #Actualiza el valor del elemento en la posición 5
print(lista)

print(20 in lista) #Comprueba si 20 está en la lista

lista.clear() #Elimina todo el contenido
print(lista)

#DIFICULTAD EXTRA
conjunto1 = {2, 4, 7, 20, 23, 6, 0, 11}
conjunto2 = {0, 3, 10, 11, 50, 30, 7, 4}

print(conjunto1.union(conjunto2)) 
print(conjunto1.intersection(conjunto2))
print(conjunto1.difference(conjunto2))
print(conjunto1.symmetric_difference(conjunto2))