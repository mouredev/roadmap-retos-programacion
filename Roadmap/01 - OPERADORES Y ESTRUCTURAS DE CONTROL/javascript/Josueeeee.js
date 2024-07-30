/* 
 ---------------------
    OPERADORES
 --------------------
 */

// Operadores Aritméticos
console.log(`Suma: 10 + 20 = ${10 + 20}`);
console.log(`Resta: 10 - 20 = ${10 - 20}`);
console.log(`multiplicación: 10 * 20 = ${10 * 20}`);
console.log(`división: 10 / 20 = ${10 / 20}`);
console.log(`Modulo 10 % 20 = ${10 % 20}`);
console.log(`Exponente 10 ** 2 = ${10 ** 2} `);

// Operadores de comparación
console.log(`Igual: 10 == "10" es ${10 == "10"}`);
console.log(`Disigual: 10 != "10" es ${10 != "10"}`);
console.log(`Mayor que: 19 > 10 es ${19 > 10}`);
console.log(`Menor que: 19 < 10 es ${19 < 10}`);
console.log(`Mayor o igual que: 19 >= 10 es ${19 >= 10}`);
console.log(`Menor o igual que: 19 <= 10 es ${19 <= 19}`);

// Operadores lógico
console.log(
  `AND &&: 10 + 10 == 20 && 30 + 3 == 33 es ${10 + 10 == 20 && 30 + 3 == 33}`
);

console.log(
  `OR ||: 10 + 10 == 20 || 30 + 3 == 33 es ${10 + 10 == 20 || 30 + 40 == 33}`
);

// Operadores de asignación
var number = 10; //asignación
console.log(number);
number += 1; //suma y asignación
console.log(number);
number -= 3; //resta y asignación
console.log(number);
number *= 3; //multipliación y asignación
console.log(number);
number /= 2; // división y asignación
console.log(number);
number **= 2; //exponente y asignación
console.log(number);
number %= 3; // modulo y asiganicón
console.log(number);

// operadores de identidad
console.log(`Igualdad estricta: 10 === 10  es${10 === "10"}`);
console.log(`Disigual estricta: 10 !== "10" es ${10 !== "10"}`);

// Operadore de pertenencia
const person = {
  name: "Jeffrey",
  age: 23,
  gender: "male",
};
console.log(`Name esta en el objeto Person? ${"name" in person}`);

// operadores en bit
let bitnum1 = 10;
let bitnum2 = 3;
console.log(`AND: 10 & 3 = ${bitnum1 & bitnum2}`);
console.log(`OR: 10 | 3 = ${bitnum1 | bitnum2}`);
console.log(`xOR: 10 ^ 3 = ${bitnum1 ^ bitnum2}`);
console.log(`NOT: ~10 = ${~bitnum1}`);
console.log(`DESPLAZAMMIENTO  A LA DERECHA: 10 >> 3 = ${bitnum1 >> bitnum2}`);
console.log(`DESPLAZAMMIENTO  A LA IZQUIERDA: 10 << 3 = ${bitnum1 << bitnum2}`);

// MÁS OPERADORES DE JAVASCRIPT

// Operadores ternarios
const val1 = true;
const val2 = false;
console.log(`Imprime el valor verdadero:  ${true ? val1 : val2}`);

//OPERADORES DE STRING
console.log("Mi " + "edad es: " + 23);

/*
 --------------------------
   ESTRUCUTRAS DE CONTROL
 --------------------------
*/

// estructura de control condicional

const namePerson = "ha";

if (namePerson == "Jeffrey") {
  console.log("El nombre es Jeffrey");
} else if (namePerson == "Josue") {
  console.log("El nombre es Josue");
} else {
  console.log("El mombre no es Jeffrey ni Josue ");
}

const interruptor = 3;
switch (interruptor) {
  case 0:
    console.log("El bombillo esta en off");
    break;
  case 1:
    console.log("El bombillio esta on");
    break;
  default:
    console.log("Ya no funciona");
    break;
}

// iterativas

for (let i = 0; i <= 10; i++) {
  console.log(i);
}

console.log(`Estructura con while`);
let i = 0;
while (i <= 10) {
  console.log(i);
  i++;
}

/*
 --------------------------
    DIFICULTAD EXTRA 
 --------------------------
*/

for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
