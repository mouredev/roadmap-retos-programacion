import Foundation

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Metodo for-in 
for i in numeros {
    print(i)
}

// Metodo ForEach 
numeros.forEach { number in 
    print(number)
}

// Metodo repeat-while 
var number = 0 
repeat {
    print(numeros[number])
    number += 1
} while number < numeros.count 

