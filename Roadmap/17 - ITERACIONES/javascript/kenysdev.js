/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#17 ITERACIONES
---------------------------------------
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/
// ________________________________________________________

console.log("bucle 'for'")
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

console.log("\nbucle 'while'")
let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

console.log("\nbucle 'do...while'")
let n = 1;
do {
    console.log(n);
    n++;
} while (n <= 10);

// ________________________________________________________
// DIFICULTAD EXTRA

console.log("\nfor...of con Array.from()")
for (const num of Array.from({ length: 5 }, (_, i) => i + 1)) {
    console.log(num);
}

console.log("\nArray.from() con .forEach()")
Array.from({ length: 5 }, (_, i) => i + 1).forEach(num => console.log(num));

console.log("\nUsando 'map()'")
Array.from({ length: 5 }, (_, i) => i + 1).map(num => console.log(num));

console.log("\nUsando 'reduce'")
Array.from({ length: 5 }, (_, i) => i + 1).reduce((_, num) => {
    console.log(num);
    return num;
}, 0);

console.log("\nUsando 'every'")
const result = [1, 2, 3, 4].every(num => {
    console.log(num);
    return num < 4;
});

console.log("\nUsando 'some'")
const result2  = [1, 2, 3, 4].some(num => {
    console.log(num);
    return num === 3;
});

console.log("\nUsando 'for...in'")
const numbers = [1, 2, 3 , 4, 5]
for (const n in numbers) {
    console.log(n);
}
