/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */
const printNumbers = numero => {
    if (numero === -1) {
        return
    }
    console.log(numero)
    return printNumbers(numero - 1)
}
printNumbers(100)


/* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

const factorial = numero => {
    if (numero === 0 || numero === 1) {
    return 1
    } else if (numero > 1) {
        return numero * factorial(numero-1)
        
    }
}
console.log(factorial(5))

const fibonacci = numero => {
    if (numero === 0) {
        return 0
    } else if (numero === 1) {
        return 1
    } else if (numero > 1) {
        return fibonacci(numero - 1) + fibonacci(numero - 2) 
    }
}
console.log(fibonacci(8))