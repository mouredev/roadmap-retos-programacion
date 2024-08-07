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

/**** OPERADORES ****/

// Operadores aritméticos
console.log(`Suma: 10 + 3 = ${10 + 3}`);
console.log(`Resta: 10 - 3 = ${10 - 3}`);
console.log(`Multiplicación: 10 X 3 = ${10 * 3}`);
console.log(`Division: 9 / 3 = ${9 / 3}`);
console.log(`Módulo: 10 % 3 = ${10 % 3}`);
console.log(`Exponente: 10 ** 3 = ${10 ** 3}`);

// Operadores de comparación
console.log(`Igualdad: 10 == 3: ${10 == 3}`);
console.log(`Igualdad: 10 == 10: ${10 == 10}`);
console.log(`Desigualdad: 10 != 3: ${10 != 3}`);
console.log(`Desigualdad: 10 != 10: ${10 != 10}`);
console.log(`Mayor que: 10 > 3: ${10 > 3}`);
console.log(`Menor que: 10 < 3: ${10 < 3}`);
console.log(`Mayor o igual que: 10 >= 3: ${10 >= 3}`);
console.log(`Menor o igual que: 10 <= 3: ${10 <= 3}`);

// Operadores lógicos
console.log(
  `AND &&: 10 + 3 == 13 && 5 - 1 == 4: ${10 + 3 == 13 && 5 - 1 == 4}`
);
console.log(`OR ||: 10 + 3 == 13 || 5 - 2 == 4: ${10 + 3 == 13 || 5 - 2 == 4}`);
console.log(`NOT !: !10 + 4 == 13: ${!(10 + 4 == 13)}`);

// Operadores de asignación
let my_number = 11; // Asignación
console.log(my_number);
my_number += 1; // Suma y asignación
console.log(my_number);
my_number -= 1; // Resta y asignación
console.log(my_number);
my_number *= 2; // Multiplicación y asignación
console.log(my_number);
my_number /= 2; // División y asignación
console.log(my_number);
my_number %= 2; // Módulo y asignación
console.log(my_number);
my_number **= 3; // Exponente y asignación
console.log(my_number);

// Operadores de identidad
let my_new_number = 1;
console.log(
  `my_number es estrictamente igual a my_new_number es: ${
    my_new_number === my_number
  }`
); // Compara no solo el valor también el tipo de dato
my_number = "1";
console.log(
  `my_number es estrictamente igual a my_new_number es: ${
    my_new_number === my_number
  }`
); // Compara no solo el valor tambien el tipo de dato

console.log(
  `my_number es estrictamente desigual a my_new_number es: ${
    my_new_number !== my_number
  }`
); // Compara no solo el valor tambien el tipo de dato
my_number = 1;
console.log(
  `my_number es estrictamente desigual a my_new_number es: ${
    my_new_number !== my_number
  }`
); // Compara no solo el valor tambien el tipo de dato

// Operadores de bit
let a = 10; // 1010
let b = 3; // 0011
console.log(`AND: 10 & 3 = ${a & b}`); // 0010
console.log(`OR: 10 | 3 = ${a | b}`); // 1011
console.log(`XOR: 10 ^ 3 = ${a ^ b}`); // 1001
console.log(`NOT: ~10 = ${~a}`); // 0101
console.log(`Desplazamiento a la derecha: 10 >> 2  ${a >> 2}`); // 0010
console.log(`Desplazamiento a la izquierda: 10 << 2  ${a << 2}`); // 101000

// Estructura de control

// Condicionales

let my_string = "Raton";
if (my_string == "Raton") {
  console.log(my_string);
} else if (my_string == "Gato") {
  console.log(my_string);
} else {
  console.log("Perro");
}

// Iterativas

for (let i = 0; i < 11; i++) {
  console.log(i);
}

i = 0;
while (i <= 10) {
  console.log(i);
  i++;
}

// Manejo de excepciones

try {
  console.lot(10 / 0);
} catch (error) {
  console.log("Error en el programa");
} finally {
  console.log("Se ha finalizado el manejo de excepciones");
}

// DIFICULTAD EXTRA

/*Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.*/

for (let i = 10; i < 56; i++) {
  if (i % 2 == 0 && i != 16 && i % 3 != 0) {
    console.log(i);
  }
}
