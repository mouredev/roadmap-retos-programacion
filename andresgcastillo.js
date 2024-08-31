// Operadores Aritméticos
console.log("Operadores Aritméticos:");
let a = 10;
let b = 3;
console.log("a + b =", a + b); // Suma
console.log("a - b =", a - b); // Resta
console.log("a * b =", a * b); // Multiplicación
console.log("a / b =", a / b); // División
console.log("a % b =", a % b); // Módulo
console.log("a ** b =", a ** b); // Exponente

// Operadores de Comparación
console.log("\nOperadores de Comparación:");
console.log("a == b:", a == b); // Igual
console.log("a != b:", a != b); // No igual
console.log("a > b:", a > b); // Mayor que
console.log("a < b:", a < b); // Menor que
console.log("a >= b:", a >= b); // Mayor o igual que
console.log("a <= b:", a <= b); // Menor o igual que

// Operadores Lógicos
console.log("\nOperadores Lógicos:");
console.log("true && false:", true && false); // AND lógico
console.log("true || false:", true || false); // OR lógico
console.log("!true:", !true); // NOT lógico

// Operadores de Asignación
console.log("\nOperadores de Asignación:");
a = 10;
console.log("a = 10:", a);
a += 5;
console.log("a += 5:", a);
a -= 2;
console.log("a -= 2:", a);
a *= 3;
console.log("a *= 3:", a);
a /= 2;
console.log("a /= 2:", a);

// Operadores de Identidad
console.log("\nOperadores de Identidad:");
console.log("a === b:", a === b);
console.log("a !== b:", a !== b);

// Operadores de Bits
console.log("\nOperadores de Bits:");
a = 60; // 60 = 0011 1100
b = 13; // 13 = 0000 1101
console.log("a & b =", a & b); // AND bit a bit
console.log("a | b =", a | b); // OR bit a bit
console.log("a ^ b =", a ^ b); // XOR bit a bit
console.log("~a =", ~a); // NOT bit a bit
console.log("a << 2 =", a << 2); // Desplazamiento a la izquierda
console.log("a >> 2 =", a >> 2); // Desplazamiento a la derecha

// Estructuras de Control
console.log("\nEstructuras de Control:");
// Condicional
let x = 10;
if (x > 5) {
  console.log("x es mayor que 5");
} else {
  console.log("x es menor o igual a 5");
}

// Iterativa
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// Excepciones
function performDivision(a, b) {
  if (b === 0) {
    throw new Error("No se puede dividir por cero");
  }
  return a / b;
}

try {
  console.log(performDivision(10, 0));
} catch (e) {
  console.log("\nOcurrió un error:", e.message);
}

//Dificultad extra
console.log("\nDificultad extra");
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
