"use strict";

let num1 = 10;
let num2 = 2;
let num3;
let num4 = 1;

// Operadores aritméticos
let suma = num1 + num2; // 12
let resta = num1 - num2; // 8
let multiplicacion = num1 * num2; // 20
let division = num1 / num2; // 5
let modulo = num1 % num2; // 0
let incremento = num1++; // 11
let decremento = num1--; // 10

// Operadores de asignación
let igual = (num3 = num2); // 2
num3 += num2; // 4
num3 -= num2; // 2
num3 *= num2; // 4
num3 /= num2; // 2
num3 %= num2; // 0

// Operadores de comparación
let igualdad = num1 == num2; // false
let desigualdad = num1 != num2; // true
// Son de comparación pero también son operadores de identidad
let igualdadEstricta = num1 === num2; // false
let desigualdadEstricta = num1 !== num2; // true
let mayorQue = num1 > num2; // true
let menorQue = num1 < num2; // false
let mayorIgualQue = num1 >= num2; // true
let menorIgualQue = num1 <= num2; // false

// Operadores lógicos
let and = num1 > num2 && num1 < num2; // false
let or = num1 > num2 || num1 < num2; // true
let not = !num1; // false

// Operadores de pertenencia
let inArray = num1 in [1, 2, 3]; // false
let instanceCheck = num1 instanceof Number;

//! Estructuras de Control en JS
// Condicionales
if (num1 > num2) {
  console.log("num1 es mayor que num2 \n");
} else if (num1 < num2) {
  console.log("num1 es menor que num2 \n");
} else {
  console.log("num1 es igual a num2 \n");
}

switch (num1) {
  case 1:
    console.log("num1 es 10 \n");
    break;
  case 2:
    console.log("num1 es 2 \n");
    break;
  default:
    console.log("num1 no es 1 ni 2 \n");
}
console.log("+-----+");
// Iterativas
for (let i = 0; i < 10; i++) {
  console.log(i);
}

console.log("+-----+");
const map = { a: 1, b: 2, c: 3 };
for (let key in map) {
  console.log(key);
}

console.log("+-----+");
const arr = [1, 2, 3, 4, 5];
for (let element of arr) {
  console.log(element);
}

// Excepciones
try {
  throw "Error";
} catch (error) {
  console.log("Error: " + error);
} finally {
  console.log("Bloque final ejecutado");
}

// Funciones
function sumar(a, b) {
  return a + b;
}

const restar = (a, b) => a - b;

// Operador ternario

const mayor = num1 > num2 ? console.log(num1) : console.log(num2);

const ejemploAdicional = () => {
  for (let i = 0; i <= 55; i++) {
    if (i % 2 === 0 && i % 3 !== 0 && i !== 16) {
      console.log(i);
    }
  }
};

ejemploAdicional();
