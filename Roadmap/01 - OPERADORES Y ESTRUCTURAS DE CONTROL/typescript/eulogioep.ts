// Operadores Aritméticos
console.log("Operadores Aritméticos:");
console.log(5 + 3);  // Suma: 8
console.log(10 - 4); // Resta: 6
console.log(3 * 4);  // Multiplicación: 12
console.log(20 / 5); // División: 4
console.log(23 % 5); // Módulo: 3
console.log(2 ** 3); // Exponenciación: 8

// Operadores de Comparación
console.log("\nOperadores de Comparación:");
console.log(5 > 3);  // Mayor que: true
console.log(5 < 3);  // Menor que: false
console.log(5 >= 5); // Mayor o igual que: true
console.log(5 <= 4); // Menor o igual que: false
console.log(5 === 5);// Igualdad estricta: true
console.log(5 !== 4);// Desigualdad estricta: true

// Operadores Lógicos
console.log("\nOperadores Lógicos:");
console.log(true && false); // AND lógico: false
console.log(true || false); // OR lógico: true
console.log(!true);         // NOT lógico: false

// Operadores de Asignación
console.log("\nOperadores de Asignación:");
let x = 10;
console.log(x);  // 10
x += 5;
console.log(x);  // 15
x -= 3;
console.log(x);  // 12
x *= 2;
console.log(x);  // 24
x /= 4;
console.log(x);  // 6

// Operadores de Identidad (para objetos)
console.log("\nOperadores de Identidad:");
let obj1 = { name: "John" };
let obj2 = { name: "John" };
let obj3 = obj1;
console.log(obj1 === obj2); // false (diferentes objetos)
console.log(obj1 === obj3); // true (mismo objeto)

// Operadores de Bits
console.log("\nOperadores de Bits:");
console.log(5 & 3);  // AND bit a bit: 1
console.log(5 | 3);  // OR bit a bit: 7
console.log(5 ^ 3);  // XOR bit a bit: 6
console.log(~5);     // NOT bit a bit: -6
console.log(5 << 1); // Desplazamiento a la izquierda: 10
console.log(5 >> 1); // Desplazamiento a la derecha: 2

// Estructuras de Control

// Condicional if-else
console.log("\nCondicional if-else:");
let age = 18;
if (age >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}

// Condicional switch
console.log("\nCondicional switch:");
let day = "Lunes";
switch (day) {
    case "Lunes":
        console.log("Hoy es lunes");
        break;
    case "Martes":
        console.log("Hoy es martes");
        break;
    default:
        console.log("Es otro día de la semana");
}

// Bucle for
console.log("\nBucle for:");
for (let i = 0; i < 5; i++) {
    console.log(`Iteración ${i}`);
}

// Bucle while
console.log("\nBucle while:");
let count = 0;
while (count < 3) {
    console.log(`Contador: ${count}`);
    count++;
}

// Bucle do-while
console.log("\nBucle do-while:");
let num = 0;
do {
    console.log(`Número: ${num}`);
    num++;
} while (num < 3);

// Manejo de excepciones
console.log("\nManejo de excepciones:");
try {
    throw new Error("Este es un error de ejemplo");
} catch (error) {
    console.log(`Error capturado: ${error.message}`);
} finally {
    console.log("Este bloque siempre se ejecuta");
}

// DIFICULTAD EXTRA
console.log("\nDIFICULTAD EXTRA:");
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}