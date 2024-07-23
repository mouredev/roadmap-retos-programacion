//operadores logicos

const a=5;
const b=123;
const c= 12;
//suma resta multi y division
console.log("suma de a + b =",a+b);
console.log("resta de a - b =",a-b);
console.log("multi de a * b =",a*b);
console.log("division de a / b =",a/b);
let modulo = 5 % 3;        // 2
let incremento = 5;
incremento++;              // 6
let decremento = 5;
decremento--;              // 4
//Operadores de comparacion
let igual = 5 == '5';      // true (comparación no estricta)
let estrictamenteIgual = 5 === '5'; // false (comparación estricta)
let estrictamenteDiferente = 5 !== '5'; // true (comparación estricta)
let mayorQue = 5 > 3;      // true
let menorQue = 5 < 3;      // false
let mayorOIgual = 5 >= 3;  // true
let menorOIgual = 5 <= 3;  // false
console.log(igual, estrictamenteIgual, estrictamenteDiferente, mayorQue, menorQue, mayorOIgual, menorOIgual);

let compaacion = a === b;
let diferente = a!= b;
console.log(compaacion,diferente);

 //comparacion estrcita con triple ===  !==

let prueba = a !== b ;
console.log(prueba)

//Operadores de identidad
// comparon valor en memoria 
let y = 5;
let z = '5';
console.log(y === z); // false (comparación estricta)
console.log(y == z);  // true (comparación no estricta)
console.log(y !== z); // true (comparación estricta)
console.log(y != z);  // false (comparación no estricta)

// Operadores de pertenencia
//conjuntos estructuras se aplica
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

for(i=10;i<=55;i++){
    if(i % 2 === 0 && i !== 16 && i % 3 !== 0 )
    console.log(i);
};
let v = 2;
let g = 7;
console.log(v%=g);


//Residuo (%)	Operador binario. Devuelve el resto entero de dividir los dos operandos.	12 % 5 devuelve 2.