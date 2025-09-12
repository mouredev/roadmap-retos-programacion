//Carlos Arturo Prieto  @cpcarlosprieto

console.log("Reto #01 OPERADORES Y ESTRUCTURAS DE CONTROL " + "\n");

// Ejemplos de operadores
console.log("EJEMPLOS DE OPERADORES:" + "\n");

// Aritméticos
let suma = 5 + 10;
let resta = 20 - 8;
let multiplicacion = 4 * 6;
let division = 30 / 5;
let modulo = 15 % 7;

console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicación:", multiplicacion);
console.log("División:", division);
console.log("Módulo:", modulo);

// Lógicos
let and = true && false;
let or = true || false;
let not = !true;

console.log("AND:", and);
console.log("OR:", or);
console.log("NOT:", not);

// Comparación
let igual = 10 == "10";
let estrictamenteIgual = 10 === "10";
let diferente = 5 != "5";
let mayorQue = 15 > 10;
let menorQue = 8 < 12;

console.log("Igual:", igual);
console.log("Estrictamente Igual:", estrictamenteIgual);
console.log("Diferente:", diferente);
console.log("Mayor Que:", mayorQue);
console.log("Menor Que:", menorQue);

// Asignación
let x = 5;
x += 3;
let y = 10;
y -= 2;

console.log("x después de suma:", x);
console.log("y después de resta:", y);

// Identidad
let identidad = 5 === 5 ? "igual" : "diferente";
console.log("Identidad:", identidad);

// Pertenencia
let arr = [1, 2, 3];
let pertenencia = 2 in arr ? "perteneciente" : "no perteneciente";
console.log("Pertenencia:", pertenencia);

// Bits
let bitwiseAnd = 5 & 3;
let bitwiseOr = 5 | 3;
let bitwiseXor = 5 ^ 3;
let bitwiseNot = ~5;

console.log("Bitwise AND:", bitwiseAnd);
console.log("Bitwise OR:", bitwiseOr);
console.log("Bitwise XOR:", bitwiseXor);
console.log("Bitwise NOT:", bitwiseNot);

// Estructuras de control
console.log("\nEJEMPLOS DE ESTRUCTURAS DE CONTROL:");

// Condicionales
let edad = 18;
if (edad >= 18) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres menor de edad");
}

// Iterativas
console.log("Números del 10 al 55 (pares, no 16 ni múltiplos de 3):");
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}

// Excepciones
try {
  throw new Error("Este es un error de ejemplo");
} catch (error) {
  console.error("Excepción:", error.message);
}
