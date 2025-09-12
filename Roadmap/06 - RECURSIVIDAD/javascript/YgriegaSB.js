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

const printNumbers = (n) => {
    console.log(n);
    if(n !== 1) {
        printNumbers(n-1);
    }
}
printNumbers(100);

const factorial = (n) => {
    if(n > 1){
        return n * factorial(n-1);
    }
    return 1;
}

factorial(5);

const fibonacci = (position) => {
    if(position > 1) {
        return fibonacci(position - 1) + fibonacci(position - 2);
    }
    return (position === 0) ? 0 : 1;
}
fibonacci(8);