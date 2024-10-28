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

const decrementByOne = (i = 101) => {
    let decrementedValue = i - 1;
    console.log(decrementedValue);
    if (decrementedValue > 0) {
        decrementByOne(decrementedValue)
    }
}

decrementByOne();

const calculateFactorial = (num, total = 1) => {
    if (num > 1) {
        const multi = num * total;
        return calculateFactorial(num - 1, multi)
    } else {
        return total;
    }
}

console.log(calculateFactorial(6));

const calculateFibonacciVal = (pos) => {
    if (pos < 1){
        console.log('El valor tiene que ser positivo y mayor a 0');
        return 0;
    } else if (pos === 1){
        return 0;
    } else if (pos === 2){
        return 1;
    } else {
        return calculateFibonacciVal(pos - 1) + calculateFibonacciVal(pos - 2);
    }
}

console.log(calculateFibonacciVal(8));