/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

console.log("### OPERADORES ###");

// Operadores Aritméticos
console.log("\n--- Aritméticos ---");
let a = 10;
let b = 3;
console.log(`Suma: 10 + 3 = ${a + b}`);
console.log(`Resta: 10 - 3 = ${a - b}`);
console.log(`Multiplicación: 10 * 3 = ${a * b}`);
console.log(`División: 10 / 3 = ${a / b}`);
console.log(`Módulo: 10 % 3 = ${a % b}`);
console.log(`Exponenciación: 10 ** 3 = ${a ** b}`);

// Operadores Lógicos
console.log("\n--- Lógicos ---");
console.log(`AND (true && false): ${true && false}`);
console.log(`OR (true || false): ${true || false}`);
console.log(`NOT (!true): ${!true}`);

// Operadores de Comparación
console.log("\n--- Comparación ---");
console.log(`Igualdad (10 == '10'): ${10 == '10'}`); // Compara valor
console.log(`Igualdad Estricta (10 === '10'): ${10 === '10'}`); // Compara valor y tipo
console.log(`Desigualdad (10 != '10'): ${10 != '10'}`);
console.log(`Desigualdad Estricta (10 !== '10'): ${10 !== '10'}`);
console.log(`Mayor que (10 > 3): ${10 > 3}`);

// Operadores de Asignación
console.log("\n--- Asignación ---");
let x = 5;
console.log(`Asignación simple: x = ${x}`);
x += 2;
console.log(`Suma y asignación: x += 2 -> x = ${x}`);

// Operadores de Identidad (ya vistos con === y !==)

// Operadores de Pertenencia
console.log("\n--- Pertenencia ---");
const arr = [1, 2, 3];
const obj = { a: 1, b: 2 };
console.log(`in para arrays (2 in arr): ${2 in arr}`); // true, busca el índice
console.log(`in para objetos ('a' in obj): ${'a' in obj}`); // true, busca la propiedad

// Operadores de Bits
console.log("\n--- Bits ---");
let p = 10; // 1010
let q = 3;  // 0011
console.log(`AND a nivel de bits (10 & 3): ${p & q}`);
console.log(`OR a nivel de bits (10 | 3): ${p | q}`);

/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 */

console.log("\n### ESTRUCTURAS DE CONTROL ###");

// Condicionales
console.log("\n--- Condicionales (if, else if, else) ---");
let edad = 18;
if (edad < 18) {
    console.log("Eres menor de edad.");
} else if (edad === 18) {
    console.log("Tienes 18 años.");
} else {
    console.log("Eres mayor de edad.");
}

// Iterativas
console.log("\n--- Iterativas (for) ---");
for (let i = 1; i <= 3; i++) {
    console.log(i);
}

console.log("\n--- Iterativas (while) ---");
let contador = 3;
while (contador > 0) {
    console.log(contador);
    contador--;
}

// Excepciones
console.log("\n--- Excepciones (try, catch, finally) ---");
try {
    let resultado = 10 / 0;
    if (resultado === Infinity) throw new Error("División por cero produce Infinity");
} catch (e) {
    console.log(`Se capturó un error: ${e.message}`);
} finally {
    console.log("Este bloque (finally) se ejecuta siempre.");
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

console.log("\n### DIFICULTAD EXTRA ###");
console.log("Números entre 10 y 55, pares, no 16 y no múltiplos de 3:");
for (let numero = 10; numero <= 55; numero++) {
    if (numero % 2 === 0 && numero !== 16 && numero % 3 !== 0) {
        console.log(numero);
    }
}
