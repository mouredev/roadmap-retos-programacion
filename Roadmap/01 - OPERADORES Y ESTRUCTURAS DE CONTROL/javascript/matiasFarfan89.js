// Operadores

//Operadores Aritmeticos

let suma = 5 + 3;          // 8
let resta = 5 - 3;         // 2
let multiplicacion = 5 * 3; // 15
let division = 5 / 3;      // 1.6666666666666667
let modulo = 5 % 3;        // 2
let incremento = 5;
incremento++;              // 6
let decremento = 5;
decremento--;              // 4

console.log(suma, resta, multiplicacion, division, modulo, incremento, decremento);

//Operadores logicos

let and = true && false;   // false
let or = true || false;    // true
let not = !true;           // false

console.log(and, or, not);

//Operadores de comparacion

let igual = 5 == '5';      // true (comparación no estricta)
let estrictamenteIgual = 5 === '5'; // false (comparación estricta)
let diferente = 5 != '5';  // false (comparación no estricta)
let estrictamenteDiferente = 5 !== '5'; // true (comparación estricta)
let mayorQue = 5 > 3;      // true
let menorQue = 5 < 3;      // false
let mayorOIgual = 5 >= 3;  // true
let menorOIgual = 5 <= 3;  // false

console.log(igual, estrictamenteIgual, diferente, estrictamenteDiferente, mayorQue, menorQue, mayorOIgual, menorOIgual);

//Operadores de Asignacion

let x = 10;
x += 5; // x = x + 5
x -= 3; // x = x - 3
x *= 2; // x = x * 2
x /= 2; // x = x / 2
x %= 3; // x = x % 3

console.log(x);

//Operadores de identidad

let a = 5;
let b = '5';
console.log(a === b); // false (comparación estricta)
console.log(a == b);  // true (comparación no estricta)
console.log(a !== b); // true (comparación estricta)
console.log(a != b);  // false (comparación no estricta)

// Operadores de pertenencia

let objeto = { clave: "valor" };
console.log("clave" in objeto); // true

let arreglo = [1, 2, 3];
console.log(0 in arreglo); // true (0 es un índice válido)

class Clase {}
let instancia = new Clase();
console.log(instancia instanceof Clase); // true

//Operadores a nivel de bit

let bitwiseAnd = 5 & 3;   // 1 (0101 & 0011 = 0001)
let bitwiseOr = 5 | 3;    // 7 (0101 | 0011 = 0111)
let bitwiseXor = 5 ^ 3;   // 6 (0101 ^ 0011 = 0110)
let bitwiseNot = ~5;      // -6 (~0101 = 1010)
let bitwiseShiftLeft = 5 << 1;  // 10 (0101 << 1 = 1010)
let bitwiseShiftRight = 5 >> 1; // 2 (0101 >> 1 = 0010)
let bitwiseShiftRightZeroFill = 5 >>> 1; // 2 (0101 >>> 1 = 0010)

console.log(bitwiseAnd, bitwiseOr, bitwiseXor, bitwiseNot, bitwiseShiftLeft, bitwiseShiftRight, bitwiseShiftRightZeroFill);




