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

function recursiva (num) {
    console.log(num)
    if (num === 0){
        return 0
    }
    return recursiva(num-1)
}

recursiva(100)


//factorial
function factorial (num) {
    if(num === 1){return 1}
    return num*factorial(num-1)
}
console.log(factorial(100))

//Fibonacci
function fibonacci(n) {
    if(n === 0){return 0}
    else if (n === 1){return 1}
    return fibonacci(n-1) + fibonacci(n-2)
}