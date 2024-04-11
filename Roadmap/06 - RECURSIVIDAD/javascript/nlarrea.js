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


const printNumbers = number => {
    console.log(number);

    if (number === 0) {
        return;
    }

    printNumbers(number - 1);
};

printNumbers(100);


/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */


const factorial = number => {
    if (number < 0) {
        console.log('Only positive numbers.');
        return -1;
    } else if (number === 0) {
        return 1;
    }

    return number * factorial(number - 1);
};

console.log('\nFactorial:');
const number = 4;
console.log(`${number}! = ${factorial(number)}`);           // 24
console.log(`${number + 1}! = ${factorial(number + 1)}`);   // 120


const fibonacci = position => {
    if (position <= 0) {
        console.log('Only positive numbers.');
        return -1;
    } else if (position === 1) {
        return 0;
    } else if (position === 2) {
        return 1;
    }

    return fibonacci(position - 1) + fibonacci(position - 2);
};

console.log('\nFibonacci:');
console.log(`The Fibonacci in position 3 is: ${fibonacci(3)}`);     // 1
console.log(`The Fibonacci in position 7 is: ${fibonacci(7)}`);     // 8