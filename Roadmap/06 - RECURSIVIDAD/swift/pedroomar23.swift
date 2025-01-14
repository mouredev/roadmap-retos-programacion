import Foundation

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

// Recursividad 
let number = 0

func recurso(number: Int) {
    if number == 0 {
        return 

        print(number)
    } else if number > 0 {
        return recurso(number: number - 1)

        print(number)
    }
}


