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

// Operadores aritméticos
const suma: number = 5 + 3;
const resta: number = 10 - 4;
const multiplicacion: number = 6 * 7;
const division: number = 20 / 4;
const modulo: number = 15 % 4;

console.log('Operadores Aritméticos:');
console.log('Suma:', suma);
console.log('Resta:', resta);
console.log('Multiplicación:', multiplicacion);
console.log('División:', division);
console.log('Módulo:', modulo);

// Operadores lógicos
const and: boolean = true && false;
const or: boolean = true || false;
const not: boolean = !true;

console.log('\nOperadores Lógicos:');
console.log('AND:', and);
console.log('OR:', or);
console.log('NOT:', not);

// Operadores de comparación
// eslint-disable-next-line eqeqeq
const igual: boolean = 5 == '5';
const estrictamenteIgual: boolean = 5 === '5';
const diferente: boolean = 10 !== 5;
const mayorQue: boolean = 15 > 10;
const menorQue: boolean = 7 < 12;

console.log('\nOperadores de Comparación:');
console.log('Igual (==):', igual);
console.log('Estrictamente Igual (===):', estrictamenteIgual);
console.log('Diferente (!=):', diferente);
console.log('Mayor Que (>):', mayorQue);
console.log('Menor Que (<):', menorQue);

// Operadores de asignación
let x: number = 10;
x += 5; // equivalente a x = x + 5
let y: number = 20;
y *= 2; // equivalente a y = y * 2

console.log('\nOperadores de Asignación:');
console.log('x:', x);
console.log('y:', y);

// Operadores bitwise
const bitwiseAnd: number = 5 & 3; // AND
const bitwiseOr: number = 5 | 3; // OR
const bitwiseXor: number = 5 ^ 3; // XOR
const bitwiseNot: number = ~5; // NOT
const leftShift: number = 5 << 1; // Left Shift
const rightShift: number = 5 >> 1; // Right Shift
const zeroFillRightShift: number = 5 >>> 1; // Zero-fill Right Shift

console.log('\nOperadores Bitwise:');
console.log('Bitwise AND (&):', bitwiseAnd);
console.log('Bitwise OR (|):', bitwiseOr);
console.log('Bitwise XOR (^):', bitwiseXor);
console.log('Bitwise NOT (~):', bitwiseNot);
console.log('Left Shift (<<):', leftShift);
console.log('Right Shift (>>):', rightShift);
console.log('Zero-fill Right Shift (>>>):', zeroFillRightShift);

// Estructuras de control
// Condicionales
const edad: number = 18;
if (edad >= 18) {
  console.log('\nEres mayor de edad.');
} else {
  console.log('\nEres menor de edad.');
}

// Iterativas
console.log('\nNúmeros entre 10 y 55 (pares, no 16 ni múltiplos de 3):');
for (let i: number = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}

// Excepciones
try {
  throw new Error('Este es un ejemplo de excepción.');
} catch (error) {
  console.error('\nExcepción:', (error as Error).message);
}

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
