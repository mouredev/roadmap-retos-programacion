// Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
var printNumbers = function (num) {
    console.log(num--);
    if (num >= 0)
        printNumbers(num);
};
printNumbers(100);
//Dificultad Extra
// - Calcular el factorial de un número concreto (la función recibe ese número).
var factorial = function (num) {
    if (num === 0)
        return 1;
    return num-- * factorial(num);
};
console.log('====================================');
console.log(factorial(3));
console.log(factorial(4));
//- Calcular el valor de un elemento concreto (según su posición) en la  sucesión de Fibonacci (la función recibe la posición).
var fibonacci = function (num) {
    if (num <= 0) {
        console.log('Debe ser mayor a 0');
        return 0;
    }
    else if (num == 1) {
        return 0;
    }
    else if (num == 2) {
        return 1;
    }
    else {
        return fibonacci(num - 1) + fibonacci(num - 2);
    }
};
console.log('====================================');
console.log(fibonacci(4));
console.log(fibonacci(5));
