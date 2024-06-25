// #17 ITERACIONES

/**
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 */

// for
for (let i = 1; i <= 10; i++) {
	console.log(i);
} // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

// while
let i = 1;
while (i <= 10) {
	console.log(i);
	i++;
} // 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

// do...While
let j = 1;
do {
	console.log(j);
	j++;
} while (j <= 10);

/**
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

const arrayNumbers = [1, 2, 3, 4, 5];
const arrayStrings = ['a', 'b', 'c', 'd', 'e'];
const myObject = {
	name: 'Christian',
	age: 23,
	languages: ['Javascript', 'Typescript', 'Python', 'Rust'],
};
// for...in
for (let index in arrayNumbers) {
	console.log(`${index} = ${arrayNumbers[index]}`);
} // -> 0 = 1, 1 = 2, 2 = 3, 3 = 4, 4 = 5

for (let index in arrayStrings) {
	console.log(`${index} = ${arrayStrings[index]}`);
} // -> 0 = a, 1 = b, 2 = c, 3 = d, 4 = e

for (let key in myObject) {
	console.log(`${key}: ${myObject[key]}`);
} // -> name: Christian, age: 23, languages: Javascript, Typescript, Python, Rust

// for...of
for (let element of arrayNumbers) {
	console.log(element);
} // -> 1, 2, 3, 4, 5

for (let element of arrayStrings) {
	console.log(element);
} // -> a, b, c, d, e

for (let element of myObject.languages) {
	console.log(element);
} // -> Javascript, Typescript, Python, Rust

for (let element of 'JavaScript') {
	console.log(element);
} // -> J, a, v, a, s, c, r, i, p, t,

// recursividad
function iterateArray(array, index) {
	if (index >= array.length) {
		return -1;
	}

	console.log(array[index]);
	iterateArray(array, index + 1);
}

iterateArray(arrayNumbers, 0); // -> 1, 2, 3, 4, 5
iterateArray(arrayStrings, 0); // -> a, b, c, d, e

// .forEach()
arrayNumbers.forEach((element) => console.log(element));
arrayStrings.forEach((element) => console.log(element));
myObject.languages.forEach((element) => console.log(element));
'JavaScript'.split('').forEach((element) => console.log(element));

// .map()
arrayNumbers.map((element) => console.log(element));
arrayStrings.map((element) => console.log(element));
myObject.languages.map((element) => console.log(element));
'JavaScript'.split('').map((element) => console.log(element));
