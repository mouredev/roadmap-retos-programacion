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

function recursivity(number) {
    if (number > 0) {
        console.log(number)
        return recursivity(--number)
    }
    return console.log(number)
}

recursivity(100)


// Ejercicio Extra

// Factorial  !5= 5 * 4 * 3 * 2 * 1 = 120

function factorial(x) {
    if (x === 1) {
        return x
    }
    return x * factorial(--x)
}

console.log(factorial(5));


// Fibonacci

function fibonacci(position) {
    
    if (position <= 0) {
        return 0 
    } else if (position === 1) {
        return 1
    } else if (position === 2) {
        return 1
    } else {
        return fibonacci (position - 1) + fibonacci(position - 2)
    }
}


console.log(fibonacci(18));
