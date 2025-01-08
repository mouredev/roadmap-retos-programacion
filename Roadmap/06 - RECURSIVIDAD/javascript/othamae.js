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

function recursivePrint(number) {
    console.log(number)
    if (number === 0) return
    return recursivePrint(number - 1)
}

recursivePrint(100)

// EXTRA TASK:

function factorial(number) {
    if (number === 0) return 1
    return number * factorial(number - 1)
}

console.log(factorial(5)) //120

function fibonacci(number) {
    if (number === 0) return 0
    if (number === 1) return 1
    return fibonacci(number - 1) + fibonacci(number - 2)
}

console.log(fibonacci(8))