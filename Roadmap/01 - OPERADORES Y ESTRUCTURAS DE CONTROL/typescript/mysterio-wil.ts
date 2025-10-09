/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

console.log("### OPERADORES ###");

// Operadores Aritméticos
console.log("\n--- Aritméticos ---");
let a: number = 10;
let b: number = 3;
console.log(`Suma: 10 + 3 = ${a + b}`);
console.log(`Resta: 10 - 3 = ${a - b}`);
console.log(`Multiplicación: 10 * 3 = ${a * b}`);
console.log(`División: 10 / 3 = ${a / b}`);
console.log(`Módulo: 10 % 3 = ${a % b}`);

// Operadores Lógicos
console.log("\n--- Lógicos ---");
console.log(`AND (true && false): ${true && false}`);
console.log(`OR (true || false): ${true || false}`);
console.log(`NOT (!true): ${!true}`);

// Operadores de Comparación
console.log("\n--- Comparación ---");
console.log(`Igualdad (10 == 10): ${10 == 10}`);
console.log(`Igualdad Estricta (10 === 10): ${10 === 10}`);

// Operadores de Asignación
console.log("\n--- Asignación ---");
let x: number = 5;
x += 2;
console.log(`Suma y asignación: x += 2 -> x = ${x}`);

// Operadores de Bits
console.log("\n--- Bits ---");
let p: number = 10; // 1010
let q: number = 3;  // 0011
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
console.log("\n--- Condicionales (if, else) ---");
let edad: number = 18;
if (edad < 18) {
    console.log("Eres menor de edad.");
} else {
    console.log("Eres mayor de edad.");
}

// Iterativas
console.log("\n--- Iterativas (for) ---");
for (let i: number = 1; i <= 3; i++) {
    console.log(i);
}

console.log("\n--- Iterativas (while) ---");
let contador: number = 3;
while (contador > 0) {
    console.log(contador);
    contador--;
}

// Excepciones
console.log("\n--- Excepciones (try, catch) ---");
try {
    throw new Error("Este es un error de ejemplo");
} catch (e) {
    if (e instanceof Error) {
        console.log(`Se capturó una excepción: ${e.message}`);
    }
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

console.log("\n### DIFICULTAD EXTRA ###");
for (let numero: number = 10; numero <= 55; numero++) {
    if (numero % 2 === 0 && numero !== 16 && numero % 3 !== 0) {
        console.log(numero);
    }
}
