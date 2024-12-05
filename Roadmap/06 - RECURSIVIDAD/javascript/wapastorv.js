/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

/*function printNumbers(n) {
    if (n >= 0) {
        console.log(n);
        printNumbers(n - 1);
    }
}

printNumbers(100);*/

// factorial de un número especificado
/*function factorial(n) {
    if (n === 0) {
        return 1;
    }

    return n * factorial(n - 1);
}

console.log(factorial(5)); // 120*/

// Secuencia de fibonacci de un número especificado
function fibonacci (n) {
    if (n <= 1) {
        return n;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(6)); // 8