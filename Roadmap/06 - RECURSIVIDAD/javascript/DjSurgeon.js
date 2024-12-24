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

/*
La recursividad es una propiedad de los lenguajes de programación que significa que una función puede llamarse a si misma.
Es útil cuando una tarea puede resolverse en tareas del mismo tipo pero más simples.
*/

// Exercise 

function recursion(first, last) {
    if (first === last) {
        console.log(first);
        return first;
    } 
    else {
        console.log(first)
        return recursion(first + 1, last)
    }
}
// recursion(0,100);

// Extra
function factorial(number) {
    if (number === 0) {
        return 1;
    } 
    else if (number === 1) {
        return 1;
    }
    else {
        return number * factorial(number - 1);
    }
}
// console.log(factorial(5)); // Print 120

function fibonacci(position) {
    let array = [0,1];
    let i;
        for (i = 0; i < position - 1; i++) {
            array.push(array[i] + array[i + 1]);
        }
    if (array.length - 1 === position) {
      return array[array.length - 1];
    }
}
// console.log(fibonacci(8)); // Print 21
