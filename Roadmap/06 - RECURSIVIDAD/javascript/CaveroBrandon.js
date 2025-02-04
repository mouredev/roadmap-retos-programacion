/*
EJERCICIO:
Entiende el concepto de recursividad creando una función recursiva que imprima
números del 100 al 0.
*/
function recursiveCounter(num) {
    if (num == 0) {
        console.log(num);
        return num;
    }
    else {
        console.log(num);
        recursiveCounter(num-1);
    }
}
/* DIFICULTAD EXTRA (opcional):
Utiliza el concepto de recursividad para:
- Calcular el factorial de un número concreto (la función recibe ese número).
- Calcular el valor de un elemento concreto (según su posición) en la 
sucesión de Fibonacci (la función recibe la posición).
*/

function factorial(num) {
    if (num == 0) {
        return 1;
    }
    else if (num == 1) {
        return num;
    }
    else {
        return num * factorial(num - 1);
    }
}

function myFibonacci(pos) {
    if (pos == 0) {
        return 0;
    }
    if (pos == 1) {
        return 1;
    }
    else {
        return myFibonacci(pos - 1) + myFibonacci(pos - 2);
    }
}

console.log('Counting down from 100 to 0: ');
recursiveCounter(100);
// Factorial function examples
console.log('The factorial of 1 is: ' + factorial(1));
console.log('The factorial of 2 is: ' + factorial(2));
console.log('The factorial of 4 is: ' + factorial(4));
console.log('The factorial of 6 is: ' + factorial(6));
// Fibonacci function examples
console.log('The Fibonacci of 2 is: ' + myFibonacci(2));
console.log('The Fibonacci of 4 is: ' + myFibonacci(4));
console.log('The Fibonacci of 8 is: ' + myFibonacci(8));
console.log('The Fibonacci of 10 is: ' + myFibonacci(10));
