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

console.group('Funcion Recursiva')

function funcRec (n){
    if(n >= 0){
        console.log(n)
        funcRec(n-1)
    }
}
funcRec(2)

console.groupEnd()

//
// EXTRA
//

console.group('Funcion Recursiva Factorial')

function factorial(n){
    if( n === 0){
        return 1
    } else {
        return n *= factorial(n-1)
    }
}

console.log(factorial(100))
console.groupEnd()

console.group('Funcion Recursiva Fibonacci Number')

function fibonacciPos(num, a = 0, b = 1, pos = 0) {
    if (num === 0) {
        return a;
    } else {
        return fibonacciPos(num - 1, b, a + b, pos + 1);
    }
}

console.log("El número de Fibonacci en la posición 4 es: ", fibonacciPos(4)); 
console.groupEnd()