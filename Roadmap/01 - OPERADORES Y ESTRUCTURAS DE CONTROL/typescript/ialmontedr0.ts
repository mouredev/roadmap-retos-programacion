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

/**
 * Ejemplos de operadores aritméticos
 */

console.log("Suma: " + (5 + 3)); // Suma

console.log("Resta: " + (5 - 3)); // Resta

console.log("Multiplicación: " + 5 * 3); // Multiplicación
console.log("División: " + 5 / 3); // División
console.log("Módulo: " + (5 % 3)); // Módulo
console.log("Incremento: " + ++5); // Incremento
console.log("Decremento: " + --5); // Decremento

/**
 * Ejemplos de operadores lógicos
 */

console.log("AND: " + (true && true)); // AND (true)
console.log("OR: " + (true || false)); // OR (true)
console.log("NOT: " + !true); // NOT (false)
console.log("XOR: " + (true ^ false)); // XOR (true)

/**
 * Ejemplos de operadores de comparación
 */

console.log("Igualdad: " + (5 == 3)); // Igualdad
console.log("Diferencia: " + (5 != 3)); // Diferencia
console.log("Estrictamente igual: " + (5 === 3)); // Estrictamente igual
console.log("Menor que: " + (5 < 3)); // Menor que
console.log("Mayor que: " + (5 > 3)); // Mayor que
console.log("Menor o igual que: " + (5 <= 3)); // Menor o igual que

/**
 * Ejemplos de operadores de asignación
 */

let x = 0;
console.log("Asignación x:", (x = 5)); // Asignación
console.log("Adicional x:", (x += 3)); // Adicional
console.log("Sustracción x:", (x -= 2)); // Sustracción
console.log("Multiplicación x:", (x *= 2)); // Multiplicación
console.log("División x:", (x /= 2)); // División
console.log("Módulo x:", (x %= 3)); // Módulo

/**
 * Ejemplos de operadores ternarios
 */

console.log("Ternario: " + (5 > 3 ? "5 es mayor" : "5 no es mayor")); // Ternario

/**
 * Estructuras de control condicionales
 */

// Ejemplo if-else
let y = 5;
if (y > 3) {
  console.log("y es mayor que 3");
} else {
  console.log("y no es mayor que 3");
}

// Ejemplo switch
switch (y) {
  case 1:
    console.log("y es 1");
    break;
  case 2:
    console.log("y es 2");
    break;
  case 3:
    console.log("y es 3");
    break;
  default:
    console.log("y no es 1, 2 o 3");
}

// Ejemplo for

for (let i = 0; i < 5; i++) {
  console.log("Iteración:", i);
}

// Ejemplo while

let j = 0;
while (j < 5) {
  console.log("Iteración:", j);
  j++;
}

// Ejemplo do-while

let k = 0;
do {
  console.log("Iteración:", k);
  k++;
} while (k < 5);

// Excepciones

try {
  let l = 5 / 0; // División por cero
} catch (error) {
  console.error("Error en la división:", error.message);
}

// Dificultad extra (imprimir números comprendidos entre 10 y 55, pares, y no 16 ni múltiplos de 3)
for (let m = 10; m <= 55; m++) {
  if (m % 2 === 0 && m! == 16 && m % 3 !== 0) {
    console.log(m);
  }
}
