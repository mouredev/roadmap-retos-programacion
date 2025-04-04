
/**
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */


function numberCount(number){
    if (number>=0){
        console.log(number);
        return numberCount(number-1)
    }
}
numberCount(100)

/** DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 */
function factorial(number){
    if (number < 0){
        console.log("Numero no valido");
        return;
    } else if (number===0){
        return 1;
    } else {
        return ((number*factorial(number-1)));
    }
}
console.log(factorial(5));

/** - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

function fibonacci(number){
    if (number===0||number===1){
        return 0;
    } else if( number===2 || number==3){
        return 1;
    } else {
        return fibonacci(number-1) + fibonacci(number-2)
    }
}
console.log(fibonacci(8));

