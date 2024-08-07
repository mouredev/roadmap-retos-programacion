/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

// EJERCICIO:
// for
for (let i = 1; i < 11; i++) {
  console.log(i);
}

// while
console.log();
x = 1;
while (x < 11) {
  console.log(x);
  x++;
}

// do-while
console.log();
a = 1;
do {
  console.log(a);
  a++;
} while (a < 11);

// DIFICULTAD EXTRA:
// 1
const object = { a: 1, b: 2, c: 3 };
for (const property in object) {
  console.log(`${property}: ${object[property]}`);
}

// 2
const miArray = [1, 2, 3, 4, 5];
for (arr of miArray) {
  console.log(arr);
}

// 3
async function forAwait() {
  const secondArray = [6, 7, 8, 9];
  for await (arr of secondArray) {
    console.log(arr);
  }
}

// 4
const array = [1, 2, 3, 4, 5];
array.forEach((value) => {
  console.log(value);
});

// 5
const array2 = [4, 5, 6];
const newArray = array2.map((value) => value * 2);
console.log(newArray);

// 6
const array3 = [7, 8, 9, 10];
const filteredArray = array3.filter((value) => value > 2);
console.log(filteredArray);
