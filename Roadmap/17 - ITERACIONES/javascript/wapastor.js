/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

// Mecanismo 1: for
console.log('Mecanismo 1: for');
for (var i = 1; i <= 10; i++) {
    console.log(i);
}

// Mecanismo 2: while
var i = 1;
console.log('Mecanismo 2: while');
while (i <= 10) {
    console.log(i);
    i++;
}

// Mecanismo 3: do-while
var i = 1;
console.log('Mecanismo 3: do-while');
do {
    console.log(i);
    i++;
} while (i <= 10);

// Mecanismo 4: forEach
console.log('Mecanismo 4: forEach');
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].forEach(function (i) {
    console.log(i);
});

// Mecanismo 5: for...in
console.log('Mecanismo 5: for...in');
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (var indice in numbers) {
    console.log(numbers[indice]);
}
// Mecanismo 6: for...of
console.log('Mecanismo 6: for...of');
for (var number of numbers) {
    console.log(number);
}


// Mecanismo 7: map
console.log('Mecanismo 7: map');
numbers.map(function (i) {
    console.log(i);
});

// Mecanismo 8: reduce
console.log('Mecanismo 8: reduce');
numbers.reduce((acc,number) => {
    console.log(number);
    return acc;
},0);

// mecanismo 9: array.from
console.log('Mecanismo 9: array.from');
Array.from({ length: 10 }, (_, i) => i + 1).forEach(number => {
    console.log(number);
});

// Mecanismo 10: array.prototype.keys
console.log('Mecanismo 10: array.prototype.keys');
[...Array(10).keys()].forEach(number => {
    console.log(number + 1);
});



