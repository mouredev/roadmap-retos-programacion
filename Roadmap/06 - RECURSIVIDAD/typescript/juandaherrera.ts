function printSep(title: string | null = null): void {
    const sep: string = "-";
    const printVar: string = title ? sep.repeat(8) + title + sep.repeat(8) : sep.repeat(16);
    console.log(printVar);
}

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
*/

function myFunction(n: number): void {
    if (n === 0) {
        console.log(0);
    } else {
        console.log(n);
        myFunction(n - 1);
    }
}

/*
* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
*/

function factorial(n: number): number {
    if (n === 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

function fibonacci(position: number): number {
    if (position === 1 || position === 2) {
        return position - 1;
    } else {
        return fibonacci(position - 1) + fibonacci(position - 2);
    }
}

function runExamples(): void {
    printSep('Ejercicio');
    myFunction(100);

    printSep('Factorial');
    console.log(factorial(9));

    printSep('Fibonacci');
    console.log(fibonacci(15));

    printSep();
}

runExamples();