
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// Arithmetic operators

// Addition
console.log(1 + 2); // 3

// Subtraction
console.log(1 - 2); // -1

// Multiplication
console.log(1 * 2); // 2

// Division
console.log(1 / 2); // 0.5

// Modulus
console.log(1 % 2); // 1

// Increment
let a = 1;
console.log(++a); // 2

// Decrement
let b = 1;
console.log(--b); // 0

// Logical operators

// AND
console.log(true && true); // true
console.log(true && false); // false
console.log(false && false); // false

// OR
console.log(true || true); // true
console.log(true || false); // true
console.log(false || false); // false

// NOT
console.log(!true); // false
console.log(!false); // true

// Comparison operators
console.log(1 == 1); // true
console.log(1 != 1); // false
console.log(1 === 1); // true
console.log(1 !== 1); // false
console.log(1 > 1); // false
console.log(1 >= 1); // true
console.log(1 < 1); // false
console.log(1 <= 1); // true

// Assignment operators
let c = 1;
c += 1;
console.log(c); // 2

// Identity operators
console.log(1 === 1); // true
console.log(1 !== 1); // false

// Membership operators
console.log(1 in [1, 2, 3]); // true
console.log(4 in [1, 2, 3]); // false

// Bitwise operators
console.log(1 & 1); // 1
console.log(1 | 1); // 1

// Conditional statements
if (1 === 1) {
  console.log("1 is equal to 1");
}
else {
  console.log("1 is not equal to 1");
}

// bits
let d = 1;
d <<= 1;
console.log(d); // 2

// Iterative statements
for (let i = 0; i < 10; i++) {
  console.log(i);
}

// Exception statements
try {
  throw "Error";
}
catch (e) {
  console.log(e);
}
finally {
  console.log("Finally");
}

// Extra
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}