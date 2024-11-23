/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//Operadores aritmeticos    
console.log('Operadores aritmeticos');
let num1 = 10;
let num2 = 5;

console.log(num1 + num2);
console.log(num1 - num2);
console.log(num1 * num2);
console.log(num1 / num2);
console.log(num1 % num2);

//Operadores logicos
console.log('Operadores logicos');
let boolean1 = true;
let boolean2 = false;

console.log(boolean1 && boolean2);
console.log(boolean1 || boolean2);
console.log(!boolean1);

//Operadores de comparacion
console.log('Operadores de comparacion');
console.log(num1 == num2);
console.log(num1 != num2);
console.log(num1 > num2);
console.log(num1 < num2);
console.log(num1 >= num2);
console.log(num1 <= num2);

//Operadores de asignacion
console.log('Operadores de asignacion');
num1 += 5;
console.log(num1);
num1 -= 5;
console.log(num1);
num1 *= 5;
console.log(num1);
num1 /= 5;
console.log(num1);
num1 %= 5;
console.log(num1);

console.log(num1);

//Operadores de identidad y pertenencia
console.log('operadores de identidad y pertenencia');
console.log(num1 === num2);
console.log(num1 !== num2);

// Operadores de pertenencia --> in para objetos
console.log('Operadores de pertenencia');
const obj = { a: 1, b: 2, c: 3 };

console.log(num1 in obj);
console.log(num1 !in obj);

// pertenencia en arrays
console.log('pertenencia en arrays');
const arr = [1, 2, 3];

console.log(arr.includes(num1));
console.log(arr.includes(3));

//Operadores de bits
console.log('Operadores de bits');
console.log(num1 & num2);
console.log(num1 | num2);
console.log(num1 ^ num2);
console.log(num1 << num2);
console.log(num1 >> num2);
console.log(num1 >>> num2);

//Estructuras de control

if (num1 > num2) {
  console.log('num1 es mayor que num2');
} else {
  console.log('num1 no es mayor que num2');
}   

for (let i = 0; i < 10; i++) {  
  console.log(i);
}

while (num1 < num2) {
  num1++;
  console.log(num1);                
}

do {           
  num1++;    
  console.log(num1);
} while (num1 < num2);

switch (num1) {
  case 1:
    console.log('num1 es 1');
    break;
  case 2:
    console.log('num1 es 2');
    break;
  default:
    console.log('num1 no es 1 ni 2');
    break;
}

try {
  console.log(num1);
} catch (error) {
  console.log(error);
}   

throw new Error('Error');
