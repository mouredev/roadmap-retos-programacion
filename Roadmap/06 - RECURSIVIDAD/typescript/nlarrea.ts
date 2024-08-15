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


function printNumbers(num: number): void {
    console.log(num)

    if (num === 0) return
    printNumbers(num - 1)
}


printNumbers(100)


/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */


// Factorial


function factorial(num: number): number {
    // Check if number is negative or 0
    if (num <= 0) {
        return -1
    }

    // Get the factorial of the number
    if (num === 1) {
        return 1
    }

    return num * factorial(num - 1)
}


console.log(factorial(4))  // 24
console.log(factorial(5))  // 120


// Fibonacci


function fibonacci(position: number): number {
    if (position <= 0) {
        console.log('Only positive numbers')
        return -1
    } else if (position === 1) return 0
    else if (position === 2) return 1

    return fibonacci(position - 1) + fibonacci(position - 2)
}


console.log(fibonacci(4))  // 2
console.log(fibonacci(7))  // 8
console.log(fibonacci(10))  // 34