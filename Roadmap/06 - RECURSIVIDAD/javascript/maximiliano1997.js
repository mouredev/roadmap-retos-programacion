/*
* EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
*/

// SOLUCION:

function recursiv(num) {
    if (num < 0) {
        console.log('Already 0')
        return;
    }


    console.log(num)
    recursiv(num - 1)
}

recursiv(100)



/*
 DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
*/

// SOLUCION:

// FACTORIAL
const funcionFactorial = (factVal) => {
    if (factVal == 0 || factVal == 1) {
        return 1
    }

    return factVal * funcionFactorial(factVal - 1)
}

console.log(funcionFactorial(8))

// FIBONACCI
const funcionFibonacci = (fibo) => {
    if (fibo == 0 || fibo == 1) {
        return 1;
    }

    return funcionFibonacci(fibo - 1) + funcionFibonacci(fibo - 2)
}

console.log(funcionFibonacci(4))