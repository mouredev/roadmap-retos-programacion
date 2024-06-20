/**
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */

function measureTime(func) {
    return function (...args) {
        const start = performance.now();
        const result = func(...args);
        const end = performance.now();
        console.log(`Required time: ${Math.round(((end - start) / 1000 * 100) / 100)} seconds`);

        return result;
    }
}


function sumTwoValues(numOne, numTwo) {
    const wait = ms => {
        const start = new Date().getTime();
        let end = start;

        while (end <= start + ms) {
            end = new Date().getTime();
        }
    }

    wait(3000);
    return numOne + numTwo;
}
// Decorate function
const decoratedSumTwoValues = measureTime(sumTwoValues);

console.log(decoratedSumTwoValues(10, 5));
/** This call prints:
 * Required time: 3 seconds
 * 15
 */


/**
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */

function callCounter(func) {
    function wrapper(...args) {
        wrapper.counter++;
        const result = func(...args);
        console.log(
            `Calls number for function "${func.name}": ${wrapper.counter}`
        );
        
        return result;
    }

    wrapper.counter = 0;
    return wrapper;
}


// First function to test
function printMessage(message = 'Hello there!') {
    console.log(message);
}
// Decorate the new function
const decoratedPrintMessage = callCounter(printMessage);


// Second function to test
function multiply(a, b) {
    return a * b;
}
const decoratedMultiply = callCounter(multiply);

decoratedPrintMessage('Hello JS');  // 1
decoratedPrintMessage();  // 2
decoratedMultiply(3, 2);  // 1
decoratedPrintMessage('Hello JavaScript');  // 3
decoratedMultiply(10, 10);  // 2
/** All of this calls print:
 * Hello JS
 * Calls number for function "printMessage": 1
 * Hello there!
 * Calls number for function "printMessage": 2
 * Calls number for function "multiply": 1
 * Hello JavaScript
 * Calls number for function "printMessage": 3
 * Calls number for function "multiply": 2
 */