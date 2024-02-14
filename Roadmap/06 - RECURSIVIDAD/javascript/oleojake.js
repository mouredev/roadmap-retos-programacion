/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.*/

function countDown(number){
    
    if (number == 0){
        console.log(number);
        console.log("Fin de la Cuenta Atrás");
        return;
    }
    else {
        console.log(number);
        countDown(number-1);
    }
}
countDown(100);

/* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 */
function factorialRecursivo (limit) {
    if (limit == 0 || limit == 1){
        return 1;
    } else {
        return limit * factorialRecursivo(limit-1);
    }
}

/* - Calcular el valor de un elemento concreto (según su posición) en la 
*  - sucesión de Fibonacci (la función recibe la posición).*/
// fibonacci(6) -> 8 (0, 1, 1, 2, 3, 5, 8)
function fib (limit) {
    if (limit == 0) {
        return 0;
    } else if (limit == 1) {
        return 1;
    } else {
        return fib(limit-2) + fib(limit-1);
    }
}

function printArrayFib(number){
    let myArray = new Array ();
    for (let i = 0; i <= number; i ++){
        myArray.push(fib(i));
    }
    return myArray;
}


// INTERFACE
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question("Introduce un número para calcular su factorial: ", (number) => {
    console.log("El factorial de " + number + " es: " + factorialRecursivo(number));
    rl.question("Introduce la posición de un elemento para conocer su valor en la succesión fibonnaci: ", (numfib) => {
        console.log("Para la posición " + numfib + " su valor es: " + fib(numfib));
        console.log("La sucesión es la siguiente: "+ printArrayFib(numfib));
        rl.close();
    });
});