// Author: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

// Mecanismo 1: Bucle for
console.log("[ Mecanismo 1 ] -> Bucle for");
for (let i = 1; i <= 10; i++) {
    process.stdout.write(i + ", ");
}
console.log("\n");

// Mecanismo 2: forEach()
console.log("[ Mecanismo 2 ] -> forEach()");
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
array.forEach(function(element) {
    process.stdout.write(element + ", ");
});
console.log("\n");

// Mecanismo 3: for...of
console.log("[ Mecanismo 3 ] -> for...of");
for (const element of array) {
    process.stdout.write(element + ", ");
}
console.log("\n");

// Mecanismo 4: for...in (no recomendado para arrays)
console.log("[ Mecanismo 4 ] -> for...in");
for (const index in array) {
    process.stdout.write(array[index] + ", ");
}
console.log("\n");

// Mecanismo 5: while
console.log("[ Mecanismo 5 ] -> while");
let i = 0;
while (i < array.length) {
    process.stdout.write(array[i] + ", ");
    i++;
}
console.log("\n");

// Mecanismo 6: do...while
console.log("[ Mecanismo 6 ] -> do...while");
let j = 0;
do {
    process.stdout.write(array[j] + ", ");
    j++;
} while (j < array.length);
console.log("\n");

// Mecanismo 7: recursividad
console.log("[ Mecanismo 7 ] -> recursividad");
const recursive = (value) => {
    process.stdout.write(value + ", ");
    if (value === 1) return 1;
    return value * recursive(value -1)

}
recursive(10);
console.log("\n");

// Mecanismo 8: Array.from() (para convertir otros objetos en arrays)
console.log("[ Mecanismo 8 ] -> Array.from()");
const arrayFromSet = Array.from(new Set(array));
arrayFromSet.forEach(function(element) {
    process.stdout.write(element + ", ");
});
console.log("\n");

// Mecanismo 9: Array.prototype.entries() (para obtener pares clave-valor de un objeto)
console.log("[ Mecanismo 9 ] -> Array.prototype.entries()");
const entries = array.entries();
for (const [index, value] of entries) {
    process.stdout.write(value + ", ");
}
console.log("\n");

// Mecanismo 10: Array.prototype.keys() (para obtener las claves de un objeto)
console.log("[ Mecanismo 10 ] -> Array.prototype.keys()");
const keys = array.keys();
for (const index of keys) {
    process.stdout.write(array[index] + ", ");
}
console.log("\n");

// Mecanismo 11: for...await...of (para iterar sobre async iterables)
console.log("[ Mecanismo 11 ] -> for...await...of");
async function asyncFunction() {
    for await (const element of array) {
        process.stdout.write(element + ", ");
    }
    console.log("\n");
}
asyncFunction();