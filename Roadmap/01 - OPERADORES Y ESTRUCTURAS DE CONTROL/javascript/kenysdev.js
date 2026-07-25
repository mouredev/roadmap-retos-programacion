/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
01 OPERADORES Y ESTRUCTURAS DE CONTROL
---------------------------------------
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
*/

// Tipos de operadores
// https://developer.mozilla.org/es/docs/Learn/Getting_started_with_the_web/JavaScript_basics#operadores

// concatena
let greeting = "Hola " + "mundo!";
console.log(greeting) // "Hola mundo!"

// _______________________
// Operadores aritmeticos:
let sumResult = 6 + 9;
console.log(sumResult); // 15

let subtractResult = 9 - 3;
console.log(subtractResult); // 6

let multiplicationResult = 8 * 2;
console.log(multiplicationResult); // 16

let divisionResult = 9 / 3;
console.log(divisionResult); // 3

let remainder = 20 % 7;
console.log(remainder); // 6

let power = 2 ** 3;
console.log(power); // 8

// _______________________
// Operador de asignación:
let myString = 'Ken';
console.log(myString); // "Bob"

let b = 3;
b += 2; // Aplicable a todos los operadores aritméticos.
console.log(b) // 5

// _______________________
// Operadores de Comparación:
let equal = 5 == 5; // Igual a
console.log(`5 == 5 -> ${equal}`); // true

let notEqual = 5 != 5; // Diferente de
console.log(`5 != 5 -> ${notEqual}`); // false

let lessThan = 4 < 5; // Menor que
console.log(`4 < 5 -> ${lessThan}`); // true

let greaterThan = 4 > 5; // Mayor que
console.log(`4 > 5 -> ${greaterThan}`); // false

let lessThanOrEqual = 4 <= 5; // Menor o igual
console.log(`4 <= 5 -> ${lessThanOrEqual}`); // true

let greaterThanOrEqual = 4 >= 5; // Mayor o igual
console.log(`4 >= 5 -> ${greaterThanOrEqual}`); // false

// Estructuras de control
// _______________________
// condicinal:
// https://developer.mozilla.org/es/docs/Learn/JavaScript/Building_blocks/conditionals

if (5 == 5) { // Aplicable a todos los operadores de Comparación.
    console.log("si lo es.");
} else {
    console.log("No lo es.");
}

// Con operadores lógicos:
if (5 == 5 && 7 < 10) { // Equivalente a 'and'
    console.log("si lo son.");
}

if (5 == 5 || 7 < 10) { // Equivalente a 'or'
    console.log("Uno de los dos es 'true'.");
}

if (!(5 == 6)) { // Equivalente a 'not'
    console.log("No lo es.");
}

// Declaraciones con switch
let day = 1;
switch (day) {
    case 1:
        console.log("Lunes");
        break;
    case 2:
        console.log("Martes"); 
        break;
    
    default:
        console.log("Día no válido");
}

// Operador Ternario
let age = 17;
let msg = (age >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
console.log(msg);

// _______________________
// Bucles
// https://developer.mozilla.org/es/docs/Learn/JavaScript/Building_blocks/Looping_code

// For Loop
for (let i = 1; i <= 5; i++) {
    console.log(i); // 1, 2, 3, 4, 5
}

// For...of Loop
const fruits = ["Apple", "Banana", "Cherry"];
for (const fruit of fruits) {
  console.log(fruit); // Apple, Banana, Cherry
}

// Acceder mediante el índice.
const colors = ["Red", "Green", "Blue"];
for (let i = 0; i < colors.length; i++) {
  console.log(colors[i]); // Red, Green, Blue
}

// While Loop
let count = 1;
while (count <= 3) {
  console.log(count); // 1, 2, 3
  count++;
}

// Do...While Loop
let num = 1;
do {
  console.log(num); // 1, 2, 3
  num++;
} while (num <= 3);

// Break Statement
for (let i = 1; i <= 5; i++) {
    if (i === 3) break; // detenerse
    console.log(i); // 1, 2
}

// Continue Statement
for (let i = 1; i <= 5; i++) {
    if (i === 3) continue; // omitir
    console.log(i); // 1, 2, 4, 5
 }

// _______________________
// Manejo de excepciones
// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#expresiones_de_manejo_de_excepciones

try {
    throw "Error"; // Lanza una excepción
  } catch (e) {
    console.error(e); // Maneja la excepción
  } finally {
    console.log("Este bloque siempre se ejecuta.");
}

/*
EJERCICIO:
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for (let num = 10; num < 56; num++) {
    if (num % 2 === 0 && num !== 16 && num % 3 !== 0) {
        console.log(num);
    }
}
