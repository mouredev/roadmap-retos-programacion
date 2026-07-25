/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

console.log('for');
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

console.log('while');
let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

console.log('do while');
let j = 1;
do {
    console.log(j);
    j++
} while (j <= 10);


console.log('---------------------DIFICULTAD EXTRA-------------------------------');

console.log('for of');
const numerosHastaDiez = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (numero of numerosHastaDiez) {
    console.log(numero);
}

console.log('for in');
for (index in numerosHastaDiez) {
    console.log(numerosHastaDiez[index]);
}

console.log('forEach');
numerosHastaDiez.forEach(num => console.log(num))

console.log('map');
numerosHastaDiez.map(num => console.log(num));

console.log('flatMap');
numerosHastaDiez.flatMap(num => console.log(num));

console.log('reduce');
numerosHastaDiez.reduce((_prevValue, num) => {
    console.log(num);
    return _prevValue;
}, 0)