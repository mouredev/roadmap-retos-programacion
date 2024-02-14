function printSep(title = null) {
    const sep = "-";
    const printVar = title ? sep.repeat(8) + title + sep.repeat(8) : sep.repeat(16);
    console.log(printVar);
}

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

function myFunction(n) {
    if (n === 0) {
        console.log(0);
    } else {
        console.log(n);
        myFunction(n - 1);
    }
}

printSep("Ejercicio");

myFunction(100);

/*
* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

// Factorial de un número
function factorial(n) {
    if (n === 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

printSep("Factorial");

console.log(factorial(9));

// Calcular valor de elemento en la sucesión de fibonacci
function fibonacci(position) {
    /*
    Esta función tiene complejidad algorítmica de O(2^n).
    Es decir que es muy ineficiente para valores grandes de position
    */
    if (position === 1 || position === 2) {
        return position - 1;
    } else {
        return fibonacci(position - 1) + fibonacci(position - 2);
    }
}

printSep("Fibonacci");

console.log(fibonacci(15));

printSep();
