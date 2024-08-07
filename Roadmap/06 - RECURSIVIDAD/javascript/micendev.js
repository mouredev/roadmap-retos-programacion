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

function cuentaAtras(num) {
    console.log(num);
    if (num === 0) return;
    return cuentaAtras(num - 1);
}

cuentaAtras(100);

//Factorial

function factorial(num) {

    
    if (num < 0) return 'Ingresa un número positivo';
    if (num === 0) return 1;
    return num * factorial(num - 1);
}

console.log(factorial(4));

//Fibonacci

function fibonacci(num) {

    if (num < 0) return 'Ingresa un número positivo';
    if (num === 0) return 0;
    if (num === 1) return 1;
    return fibonacci(num - 1) + fibonacci(num - 2);
}

console.log(fibonacci(10));