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

const num1 = 10;
const num2 = 5;

// Operadores aritméticos
console.log("Operadores aritméticos:");

let suma = num1 + num2;
let resta = num1 - num2;
let multiplicacion = num1 * num2;
let division = num1 / num2;
let modulo = num1 % num2;
let exponenciacion = num1 ** num2;

console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicación:", multiplicacion);
console.log("División:", division);
console.log("Resto:", modulo);
console.log("Exponenciación:", exponenciacion);

// Operadores de asignación
console.log("Operadores de asignación:");

let x = num1; // Asignación
x += division;
console.log("Asignación de adición:", x);

let y = num2;
y -= 1;
console.log("Asignación de resta:", y);

let z = num1;
z *= y;
console.log("Asignación de multiplicación:", z);

let a = multiplicacion;
a /= resta;
console.log("Asignación de división:", a);

let b = exponenciacion;
b %= x;
console.log("Asignación de resto:", b);

// Operadores de comparación
console.log("Operadores de comparación:");

let igualdad = y == "4";
console.log(igualdad);

let igualdadEstricta = z === 40;
console.log(igualdadEstricta);

let desigualdad = num1 != resta;
console.log(desigualdad);

let desigualdadEstricta = 4 !== "4";
console.log(desigualdadEstricta);

let mayorQue = num1 > num2;
console.log(mayorQue);

let mayorIgualQue = 10 >= 10;
console.log(mayorIgualQue);

let menorQue = suma < z;
console.log(menorQue);

let menorIgualQue = multiplicacion <= 50;
console.log(menorIgualQue);

// Operadores lógicos
console.log("Operadores lógicos:");

let and = true && true;
console.log("Operador AND lógico: && =>", and);

let or = true || false;
console.log("Operador OR lógico: || =>", or);

let not = !false;
console.log("Operador NOT lógico: ! =>", not);

// Dificultad extra

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
