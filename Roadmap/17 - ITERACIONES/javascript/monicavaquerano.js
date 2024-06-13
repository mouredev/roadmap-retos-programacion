// 17 ITERACIONES
// Monica Vaquerano
// https://monicavaquerano.dev


/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

console.log("For Loop");
for (let i = 1; i < 11; i++) {
    console.log(i);
};

console.log("\nWhile Loop");
let x = 1;
while (x < 11) {
    console.log(x);
    x++;
};
console.log("\nDo-While Loop");
let y = 1
do {
    console.log(y);
    y++;
} while (y < 11);