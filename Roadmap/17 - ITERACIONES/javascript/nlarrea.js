/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

// OPTION 1

console.log("\nOPTION 1: for loop");

for (let num = 1; num <= 10; num++) {
    console.log(num);
}


// OPTION 2

console.log("\nOPTION 2: while loop");

let num = 1;
while (num <= 10) {
    console.log(num);
    num++;
}


// OPTION 3

console.log("\nOPTION 3: recursive function call");


/**
 * Prints the numbers in the given range.
 * @param {Number} start The number where the counter starts to count (included).
 * @param {Number} stop The number where the counter stops (included).
 */
function counter(start, stop) {
    console.log(start);

    if (start >= stop) {
        return stop;
    }

    counter(start + 1, stop);
}


counter(1, 10);
