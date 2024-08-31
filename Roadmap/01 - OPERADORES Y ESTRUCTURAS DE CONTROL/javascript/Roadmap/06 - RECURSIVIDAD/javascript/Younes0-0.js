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

//Ejercicio
function cuenta_atras(num){
    if (num <= 0) {
        return;
    }
    console.log(num);
    return cuenta_atras(num - 1);
}
//cuenta_atras(100)

//Factorial
function factorial(num){
    if (num === 0 || num === 1) {
        return 1;
    } else {
        return num * factorial(num - 1);
    }
}
//console.log(factorial(5));

//Fibonacci
function fibonacci(num){
    if (num === 0) {
        return 0;
    } else if (num === 1) {
        return 1;
    } 
    return fibonacci(num - 1) + fibonacci(num - 2);
    
}
//0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
console.log(fibonacci(10));


