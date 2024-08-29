import Foundation 

/*
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

 // Conjuntos 
 let conjunto = [1, 2, 3, 4, 5]

 // Eliminar todo el conjunto 
 conjunto.removeAll()

 // Eliminar un elemento en concreto 
 conjunto.remove(2)

 // Añadir un elemento al principio 
 conjunto.insert(contentsOf: [-1, 0], at: 0)

 // Añadir un elemento al final 
 conjunto.append(contentsOf: [6, 7, 8])

 // Añadir varios elemnetos en bloque en una posicion concreta 
 conjunto.append(contentsOf: [2.1, 2.2, 2.3], at: 2)

 // Actualizar el valor de un elemento en una posicion concreta 
 conjunto[2] = 10

 // Comprobar si un elemento esta en el conjunto 
 conjunto.contains(3)

 



