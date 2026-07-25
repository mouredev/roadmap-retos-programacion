let cadena = 'String';
let bool = true;
let nothing = null;
let array = [1, 2, 3, 4];
let number = -4;
const PI = 3.1416;
let lenguaje = 'JavaScript';
let counter = 1;
let objeto = {
  name: 'Wilson',
  edad: 41,
};

if (number < 0) {
  console.log('El numero es negativo');
} else {
  console.log('El nuemro es positivo');
}

switch (objeto.edad) {
  case 1:
    console.log('El numero es 1');
    break;
  default:
    console.log('Eligiste otro numero diferente ');
}

for (let i = 1; i <= 5; i++) {
  console.log('Numero ', i);
}

while (counter <= 10) {
  console.log('El contador vale ', counter);
  counter++;
}


for (const property in objeto) {
  console.log(
    `la propiedad ${property} tiene un valor de: ${objeto[property]}`
  );
}

try {
  console.log('Antes del error');
  throw new TypeError('oops');
} catch ({ name, message }) {
  console.log(name); // "TypeError"
  console.log(message); // "oops"
}

try {
  throw 'Oops; this is not an Error object';
} catch (e) {
  if (!(e instanceof Error)) {
    e = new Error(e);
  }
  console.log(e);
  console.error(e.message);
}

// ejercicio
// Crea un programa que imprima por consola todos los números comprendidos
//  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0) {
    if (i % 3 !== 0 && i !== 16) {
      console.log(i);
    }
  }
}