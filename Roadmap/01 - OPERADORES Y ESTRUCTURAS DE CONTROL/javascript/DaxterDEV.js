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
let asignación = 5; // Asignación
let suma = 5 + 3; // Aritmético
let resta = 10 - 2; // Aritmético
let multiplicacion = 4 * 2; // Aritmético
let division = 8 / 4; // Aritmético
let modulo = 10 % 3; // Aritmético, resto de la división
let mayorQue = 5 > 3; // Comparación
let menorQue = 2 < 4; // Comparación
let igualQue = 5 == 5; // Comparación
let identidad = 5 === 5; // Identidad
let noIgualQue = 5 != 3; // Comparación
let pertenencia = [1, 2, 3].includes(2); // Pertenencia
let bits = 5 & 3; // Operador bit a bit AND

console.log("Asignación:", asignación);
console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicación:", multiplicacion);
console.log("División:", division);
console.log("Módulo:", modulo);
console.log("Mayor que:", mayorQue);
console.log("Menor que:", menorQue);
console.log("Igual que:", igualQue);
console.log("Identidad:", identidad);
console.log("No igual que:", noIgualQue);

//Operadores Lógicos
let yLogico = true && false; // Lógico
let oLogico = true || false; // Lógico
let noLogico = !true; // Lógico

console.log("Y lógico:", yLogico);
console.log("O lógico:", oLogico);
console.log("No lógico:", noLogico);

// Estructuras de control
// Condicional
if (mayorQue) {
  console.log("5 es mayor que 3");
}
// Condicional con else
if (menorQue) {
  console.log("2 es menor que 4");
} else {
  console.log("2 no es menor que 4");
}
// Condicional con else if
if (igualQue) {
  console.log("5 es igual a 5");
} else if (noIgualQue) {
  console.log("5 no es igual a 3");
}
// Iterativa for
for (let i = 0; i < 5; i++) {
  console.log("Iteración:", i);
}
// Iterativa while
let j = 0;
while (j < 5) {
  console.log("Iteración while:", j);
  j++;
}
// Excepción
try {
  let errorPrueba = 5 / 0; // Esto no generará un error, pero es un ejemplo de manejo de excepciones
} catch (error) {
  console.error("Error:", error);
}
// DIFICULTAD EXTRA
console.log(
  "Números comprendidos entre 10 y 55, pares, no son 16 ni múltiplos de 3:"
);
for (let num = 10; num <= 55; num++) {
  if (num % 2 === 0 && num !== 16 && num % 3 !== 0) {
    console.log(num);
  }
}
// Fin del ejercicio
