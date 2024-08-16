let n1 = 1;
let n2 = 10;

// Operadores de comparación

// Las comparaciones entre valores retornan un booleano como resultado
console.log(n1 > n2); // Mayor que
console.log(n1 < n2); // Menor que
console.log(n1 >= n2); // Mayor o igual que
console.log(n1 <= n2); // Menor o igual que
console.log(n1 == n2); // Igual
console.log(n1 != n2); // No es igual

// Operadores aritméticos
console.log(n1 + n2); // Suma
console.log(n1 - n2); // Resta
console.log(n1 * n2); // Multiplicación
console.log(n1 / n2); // División
console.log(n1 % n2); // Residuo de una división
console.log(n1 ** n2); // Potenciación
console.log(n1++); // Incremento
console.log(n1--); // Decremento

// Operadores a nivel de bits
console.log(n1 & n2); // AND
console.log(n1 | n2); // OR
console.log(n1 ^ n2); // XOR
console.log(~n1); // NOT
console.log(n1 << n2); // Desplazamiento a la izquierda
console.log(n1 >> n2); // Desplazamiento a la derecha
console.log(n1 >>> n2); // Desplazamiento a la derecha sin signo

// Operadores lógicos
const result1 = n1 > n2 && n2 > 0; // AND
console.log(result1); // Salida: false
const result2 = n1 < n2 || n2 > 0; // OR
console.log(result2); // Salida: true
const result3 = !(n1 < n2); // NOT
console.log(result3); // Salida: true
const result4 = n1 ?? n2; // Nullish coalescing
console.log(result4); // Salida: 1

// Operadorer de cadena
const string1 = 'Hola';
const string2 = 'Mundo';
console.log(string1 + ' ' + string2); // Concatenación de cadenas

let message = 'Hola';
message += ' Mundo'; // Concatenación de cadenas
console.log(message); // Salida: Hola Mundo

let text = 'JavaScript';
console.log(text[0]); // Salida: J
console.log(text[1]); // Salida: a

// Spread operator o operador de propagación
// Permite expandir elementos de un iterable como arrays, strings objetos, etc.

// expandir un array
let arr = [1, 2, 3];
let arr2 = [...arr, 4, 5, 6];

// copiar un array de forma superficial
let arr3 = [...arr];

// copiar un objeto de forma superficial
let obj = { a: 1, b: 2, c: 3 };
let obj2 = { ...obj };

// de forma superficial significa que solo se copia la referencia de los elementos esto es, si los elementos son objetos o arrays, estos no se copian, sino que se hace una referencia al objeto original.

// Operador ternario
let age = 18;
let message2 = age >= 18 ? 'Eres mayor de edad' : 'Eres menor de edad';
console.log(message2); // Salida: Eres mayor de edad

// Operador de asignación
let a = 1;
let b = 2;
let c = 3;

// Estructuras de control

// Condicionales

// if
// Nos permite ejecutar un bloque de código si una condición es verdadera
if (age >= 18) {
  console.log('Eres mayor de edad');
} else {
  // este bloque se va a ejectuar si la condición previa es falsa
  console.log('Eres menor de edad');
}

// else if
// Nos permite evaluar una nueva condición si la condición anterior es falsa
if (age >= 18) {
  console.log('Eres mayor de edad');
} else if (age >= 15) {
  console.log('Eres adolescente');
} else {
  console.log('Eres un niño');
}

// switch
// Nos permite evaluar una expresión multiples veces (es decir, con diferentes condiciones) y ejecutar un bloque de código dependiendo del valor de la expresión
let day = 3;
switch (day) {
  case 1:
    console.log('Lunes');
    break;
  case 2:
    console.log('Martes');
    break;
  case 3:
    console.log('Miércoles');
    break;
  case 4:
    console.log('Jueves');
    break;
  case 5:
    console.log('Viernes');
    break;
  default:
    console.log('Fin de semana');
}

// Iterativas
// Bucles:
// Nos permiten ejecutar un bloque de código múltiples veces mientras la condición de la expresión sea verdadera

// for: ideal para cuando sabemos cuántas veces queremos que se ejecute el bucle
// for (inicialización; condición; incremento)
for (let i = 0; i < 5; i++) {
  console.log(i); // Salida: 0, 1, 2, 3, 4
}

// while: ideal para cuando no sabemos cuántas veces queremos que se ejecute el bucle y queremos que se ejecute mientras una condición sea verdadera
let winner = false;
let counter = 0;
const randomNumberBetween0And10 = Math.floor(Math.random() * 11);

while (!winner) {
  counter++;

  if (counter === randomNumberBetween0And10) {
    winner = true;
  }
}

// do while: similar al bucle while, pero la diferencia es que el bloque de código se ejecuta al menos una vez antes de evaluar la condición
let num = 1;

do {
  if (num % 2 === 0) {
    console.log(`${num} es par.`);
  }
  num++;
} while (num <= 10);

// for in: se usa para iterar sobre las propiedades de un objeto
const person = {
  name: 'John',
  age: 30,
};

for (let key in person) {
  console.log(key, person[key]); // Salida: name John, age 30
}

// for of: se usa para iterar sobre los elementos de arrays, strings, maps, sets, etc.
let numbers = [1, 2, 3, 4, 5];

for (let number of numbers) {
  console.log(number); // Salida: 1, 2, 3, 4, 5
}

// Control de excepciones

try {
  // Bloque de código a probar
  let x = y + 10; // y no está definido por lo que se lanzará un error
} catch (error) {
  // Bloque de código a ejecutar si hay un error
  console.log(error); // Salida: ReferenceError: y is not defined
} finally {
  // Bloque de código a ejecutar siempre
  console.log('Este bloque siempre se ejecutará');
}

// break y continue
// break: se usa para salir de un bucle
// continue: se usa para saltar la iteración actual de un bucle y continuar con la siguiente iteración
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break; // Salir del bucle cuando i es 5
  }
  console.log(i);
}

for (let i = 0; i < 5; i++) {
  if (i === 3) {
    continue; // Saltar la iteración cuando i es 3
  }
  console.log(i);
}

// return
// Nos permite devolver un valor de una función y finalizar su ejecución

/*
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3 */

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}

// podriamos hacerlo con un while
let i = 10;
let limit = 55;

while (i <= limit) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
  i++;
}
