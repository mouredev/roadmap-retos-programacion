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

// Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...

// Operadores aritméticos
const a = 4;
const b = 2;

// Suma
console.log(a + b); // 6
// Resta
console.log(a - b); // 2
// Multiplicación
console.log(a * b); // 8
// División
console.log(a / b); // 2
// Resto, residuo o módulo
console.log(a % b); // 0
// Exponencial
console.log(a ** b); // 16
// Incremento
console.log(a++); // a = a + 1 = 5
// Decremento
console.log(a--); // a = a - 1 = 4

// Operadores lógicos
const c = true;
const d = false;

// AND (&&)
console.log(c && d); // false, devuelve true si ambos operandos son true
// OR (||)
console.log(c || d); // true, devuelve true si alguno de los operandos es true
// NOT (!)
console.log(!c); // false, devuelve el valor contrario al operando

// Operadores de comparación
const e = 4;
const f = 2;

// Igualdad
console.log(e == f); // false, devuelve true si ambos operandos son iguales
// Desigualdad
console.log(e != f); // true, devuelve true si ambos operandos son diferentes
// Estrictamente igual
console.log(e === f); // false, devuelve true si ambos operandos son iguales y del mismo tipo
// Estrictamente desigual
console.log(e !== f); // true, devuelve true si ambos operandos son diferentes o de diferente tipo
// Mayor que
console.log(e > f); // true, devuelve true si el primer operando es mayor que el segundo
// Mayor o igual que
console.log(e >= f); // true, devuelve true si el primer operando es mayor o igual que el segundo
// Menor que
console.log(e < f); // false, devuelve true si el primer operando es menor que el segundo
// Menor o igual que
console.log(e <= f); // false, devuelve true si el primer operando es menor o igual que el segundo

// Operadores de asignación
let g = 4;
let h = 2;

// Asignación
console.log((g = h)); // 2, asigna el valor del segundo operando al primero
// Asignación de suma
console.log((g += h)); // 4, suma el valor del segundo operando al primero
// Asignación de resta
console.log((g -= h)); // 2, resta el valor del segundo operando al primero
// Asignación de multiplicación
console.log((g *= h)); // 4, multiplica el valor del segundo operando al primero
// Asignación de división
console.log((g /= h)); // 2, divide el valor del segundo operando al primero
// Asignación de resto, residuo o módulo
console.log((g %= h)); // 0, asigna el resto de dividir el valor del primer operando entre el segundo al primero
// Asignación de exponencial
console.log((g **= h)); // 0, asigna el valor del primer operando elevado al segundo al primero

// Operadores de identidad
const i = 4;
const j = 2;

// Identidad
console.log(i === j); // false, devuelve true si ambos operandos son iguales y del mismo tipo
// No identidad
console.log(i !== j); // true, devuelve true si ambos operandos son diferentes o de diferente tipo

// Operadores de pertenencia
const k = [1, 2, 3, 4];
const l = 2;

// Pertenencia
console.log(l in k); // true, devuelve true si el segundo operando es una propiedad del primero

// Operadores de bits
const m = 4;
const n = 2;

// AND a nivel de bits
console.log(m & n); // 0, devuelve un 1 para cada bit en la misma posición si ambos operandos son 1
// OR a nivel de bits
console.log(m | n); // 6, devuelve un 1 para cada bit en la misma posición si alguno de los operandos es 1
// XOR a nivel de bits
console.log(m ^ n); // 6, devuelve un 1 para cada bit en la misma posición si ambos operandos son diferentes
// NOT a nivel de bits
console.log(~m); // -5, invierte los bits de un operando
// Desplazamiento a la izquierda
console.log(m << n); // 16, desplaza los bits del primer operando el número de posiciones indicado por el segundo
// Desplazamiento a la derecha
console.log(m >> n); // 1, desplaza los bits del primer operando el número de posiciones indicado por el segundo

// Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje: Condicionales, iterativas, excepciones...

// Condicionales
const o = 4;
const p = 2;

// IF
if (o > p) {
  console.log(`${o} es mayor que ${p}`);
}

// IF ELSE
if (o > p) {
  console.log(`${o} es mayor que ${p}`);
} else {
  console.log(`${o} es menor que ${p}`);
}

// IF ELSE IF
if (o > p) {
  console.log(`${o} es mayor que ${p}`);
} else if (o < p) {
  console.log(`${o} es menor que ${p}`);
}

// SWITCH
const day = 1;

switch (o) {
  case 1:
    console.log("Lunes");
    break;
  case 2:
    console.log("Martes");
    break;
  case 3:
    console.log("Miércoles");
    break;
  case 4:
    console.log("Jueves");
    break;
  case 5:
    console.log("Viernes");
    break;
  case 6:
    console.log("Sábado");
    break;
  case 7:
    console.log("Domingo");
    break;
  default:
    console.log("El día no existe");
}

// Iterativas
// FOR
for (let i = 1; i <= 5; i++) {
  console.log(i); // Muestra 1 2 3 4 5
}

// WHILE
let index = 1;
while (index <= 5) {
  console.log(index); // Muestra 1 2 3 4 5
  index++;
}

// DO WHILE
let index2 = 1;
do {
  console.log(index2);
  index2++;
} while (index2 <= 5); // Muestra 1 2 3 4 5

// FOR OF
const array = [1, 2, 3, 4, 5];
for (let element of array) {
  console.log(element); // Muestra 1 2 3 4 5
}

// FOR IN

const object = { a: 1, b: 2, c: 3, d: 4, e: 5 };
for (let key in object) {
  console.log(key); // Muestra a b c d e
}

// Excepciones
try {
  console.log("Hola");
} catch (error) {
  console.log(error);
} finally {
  console.log("Adiós");
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

for (let i = 10; i <= 55; i++) {
  if (i !== 16 && i % 3 !== 0 && i % 2 === 0) {
    console.log(i);
  }
}
