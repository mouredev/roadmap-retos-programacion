// Ejemplos de operadores en JavaScript

// 1. Operadores Aritméticos
console.log("--- Operadores Aritméticos ---");
console.log("Suma: 5 + 3 =", 5 + 3);
console.log("Resta: 10 - 4 =", 10 - 4);
console.log("Multiplicación: 6 * 2 =", 6 * 2);
console.log("División: 15 / 3 =", 15 / 3);
console.log("Módulo: 17 % 5 =", 17 % 5);
console.log("Exponenciación: 2 ** 3 =", 2 ** 3);
console.log("Incremento: let a = 5; a++; a =", (() => { let a = 5; a++; return a; })());
console.log("Decremento: let b = 8; b--; b =", (() => { let b = 8; b--; return b; })());

// 2. Operadores de Asignación
console.log("\n--- Operadores de Asignación ---");
let x = 10;
console.log("Asignación simple: x = 10;", x);
x += 5;
console.log("Suma y asignación: x += 5;", x);
x *= 2;
console.log("Multiplicación y asignación: x *= 2;", x);

// 3. Operadores de Comparación
console.log("\n--- Operadores de Comparación ---");
console.log("Igualdad: 5 == '5' es", 5 == '5');
console.log("Igualdad estricta: 5 === '5' es", 5 === '5');
console.log("Desigualdad: 5 != '6' es", 5 != '6');
console.log("Mayor que: 7 > 5 es", 7 > 5);
console.log("Menor o igual que: 10 <= 10 es", 10 <= 10);

// 4. Operadores Lógicos
console.log("\n--- Operadores Lógicos ---");
console.log("AND lógico: true && false es", true && false);
console.log("OR lógico: true || false es", true || false);
console.log("NOT lógico: !true es", !true);

// 5. Operadores de Tipo
console.log("\n--- Operadores de Tipo ---");
console.log("typeof 42 es", typeof 42);
console.log("instanceof: [] instanceof Array es", [] instanceof Array);

// 6. Operadores de Bits
console.log("\n--- Operadores de Bits ---");
console.log("AND a nivel de bits: 5 & 3 =", 5 & 3);
console.log("OR a nivel de bits: 5 | 3 =", 5 | 3);
console.log("XOR a nivel de bits: 5 ^ 3 =", 5 ^ 3);
console.log("Desplazamiento a la izquierda: 5 << 1 =", 5 << 1);

// Ejemplos de estructuras de control

// 1. Estructura Condicional: if-else
console.log("\n--- Estructura Condicional: if-else ---");
let numero = 15;
if (numero > 10) {
    console.log("El número es mayor que 10");
} else if (numero < 10) {
    console.log("El número es menor que 10");
} else {
    console.log("El número es igual a 10");
}

// 2. Estructura Condicional: switch
console.log("\n--- Estructura Condicional: switch ---");
let dia = "Lunes";
switch (dia) {
    case "Lunes":
        console.log("Hoy es Lunes");
        break;
    case "Martes":
        console.log("Hoy es Martes");
        break;
    default:
        console.log("Es otro día de la semana");
}

// 3. Estructura Iterativa: for
console.log("\n--- Estructura Iterativa: for ---");
for (let i = 0; i < 5; i++) {
    console.log("Iteración for:", i);
}

// 4. Estructura Iterativa: while
console.log("\n--- Estructura Iterativa: while ---");
let contador = 0;
while (contador < 3) {
    console.log("Iteración while:", contador);
    contador++;
}

// 5. Estructura Iterativa: do-while
console.log("\n--- Estructura Iterativa: do-while ---");
let j = 0;
do {
    console.log("Iteración do-while:", j);
    j++;
} while (j < 3);

// 6. Manejo de Excepciones: try-catch
console.log("\n--- Manejo de Excepciones: try-catch ---");
try {
    throw new Error("Este es un error de ejemplo");
} catch (error) {
    console.log("Error capturado:", error.message);
} finally {
    console.log("Este bloque siempre se ejecuta");
}

// DIFICULTAD EXTRA
console.log("\n--- DIFICULTAD EXTRA ---");
for (let num = 10; num <= 55; num++) {
    if (num % 2 === 0 && num !== 16 && num % 3 !== 0) {
        console.log(num);
    }
}