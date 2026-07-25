/* #06 RECURSIVIDAD

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

function recursiva100to0 (num) {
    if (num < 0) {
        return;
    }
    console.log(num);
    recursiva100to0(num - 1);
}
recursiva100to0(100);

function factorial (num) {
    if (num === 0 || num === 1) {
        return 1;
    } else {
        return num * factorial(num - 1);
    }
}
console.log(factorial(6));

function fibonacci (num) {
    if (num === 0) {
        return 0;
    } else if (num === 1) {
        return 1;
    } else {
        return fibonacci(num - 1) + fibonacci(num - 2);
    }
}
console.log(fibonacci(3));


function sumaRecursiva(n) {
    if (n === 1) {
        return 1;
    } else {
        return n + sumaRecursiva(n - 1);
    }
}

console.log(sumaRecursiva(5))