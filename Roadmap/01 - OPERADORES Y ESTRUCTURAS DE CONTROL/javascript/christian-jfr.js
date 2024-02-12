// #01 - Operadores y estructuras de control

/* 
 * 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 * Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 * (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
*/

// Operadores Aritméticos
const num1 = 10; 
const num2 = 5;
const string1 = '10';

console.log('Suma: ', num1 + num2); // -> Suma: 15
console.log('Resta: ', num1 - num2); // -> Resta: 5
console.log('Multiplicación: ', num1 * num2); // -> Multiplicación: 50
console.log('División: ', num1 / num2); // -> División: 2
console.log('Módulo: ', num1 % num2); // -> Módulo: 0
console.log('Potencia: ', num1 ** num2); // -> Potencia: 100000

console.log('Incremento Postfijo: ', num1++);
console.log('Incremento Prefijo: ', ++num1);
console.log('Decremento Postfijo: ', num2--);
console.log('Decremento Prefijo: ', --num2);

// Operadores de Asignación
// = Asignación
let as = 10;
console.log(as); // -> 10
// += Suma y asignación
let as1 = 10;
as1 += 2;
console.log(as1); // -> 12
// -= Resta y asignación
let as2 = 10;
as2 -= 2;
console.log(as2); // -> 8
// *= Multiplicación y asignación
let as3 = 10;
as3 *= 2;
console.log(as3); // -> 20
// /= División y asignación
let as4 = 10;
as4 /= 2;
console.log(as4); // -> 5
// %= Módulo y asignación
let as5 = 10;
as5 %= 2;
console.log(as5); // -> 0
// **= Potencia y asignación
let as6 = 10;
as6 **= 2;
console.log(as6); // -> 100
// <<= Desplazamiento a la izquierda y asignación
let as7 = 10;
as7 <<= 2;
console.log(as7); // -> 40
// >>= Desplazamiento a la derecha y asignación
let as8 = 10;
as8 >>= 2;
console.log(as8); // -> 2
// >>>= Desplazamiento a la derecha y asignación sin signo
let as9 = 2;
as9 >>>= 2;
console.log(as9); // -> 0
// &= Bitwise AND y asignación
let as10 = 10;
as10 &= 2;
console.log(as10); // -> 2
// ^= Bitwise XOR y asignación
let as11 = 10;
as11 ^= 2;
console.log(as11); // -> 8
// |= Bitwise OR y asignación
let as12 = 10;
as12 |= 2;
console.log(as12); // -> 10
// &&= logico AND y asignación
let as13 = 10;
as13 &&= 2;
console.log(as13); // -> 2
// ||= logico OR y asignación
let as14 = 10;
as14 ||= 2;
console.log(as14); // -> 10
// ??= Asignación de coalescencia nula
let as15 = 10;
as15 ??= 2;
console.log(as15); // -> 10

// Operadores de Comparación
// Relacionales
console.log('Mayor que: ', num1 > num2); // -> Mayor que: true
console.log('Menor que: ', num1 < num2); // -> Menor que: false
console.log('Mayor o igual que: ', num1 >= num2); // -> Mayor o igual que: true
console.log('Menor o igual que: ',num1 <= num2); // -> Menor o igual que: false
// Igualdad
console.log('Igualdad: ', num1 == num2); // -> Igualdad: false
console.log('Desigualdad: ', num1 != num2); // -> Desigualdad: true
// Igualdad estricta
console.log('Igualdad estricta: ', num1 === string1); // -> Igualdad estricta: false
console.log('Desigualdad estricta: ', num1 !== string1); // -> Desigualdad estricta: true

// Operadores Lógicos ! - && - || 
let opNot = !true;
let opAnd = true && false;
let opOr = true || false;

console.log(opNot, opAnd, opOr); // -> false, false, true

// Operadores Bitwise
console.log('Bitwise AND: ', 3 & 5); // Bitwise AND: 1
console.log('Bitwise OR: ', 1 | 4); // Bitwise OR: 5
console.log('Bitwise XOR: ', 3 ^ 5); // Bitwise XOR: 6
console.log('Bitwise NOT: ', ~3); // Bitwise NOT: -4
console.log('Bitwise LEFT SHIFT: ', 3 << 2); // Bitwise LEFT SHIFT: 12
console.log('Bitwise RIGHT SHIFT: ', 3 >> 2); // Bitwise RIGHT SHIFT: 0
console.log('Bitwise ZERO FILL RIGHT SHIFT: ', 2 >>> 3); // Bitwise ZERO FILL RIGHT SHIFT: 0

// Operadores Unarios
// delete
let myObject = {a: 1, b: 2};
delete myObject.a;
console.log(myObject); // -> {b: 2}
// typeof
console.log(typeof num1); // -> number
// void
const vacio = void 10;
console.log(vacio); // -> undefined

// Operadores relacionales
// in
let numbers = [7, 8, 9];
console.log('a' in numbers); // -> false
console.log(0 in numbers); // -> true
console.log(9 in numbers); // -> false
console.log(length in numbers); // -> true
// instanceof
let myArray = [1, 2, 6];
console.log(myArray instanceof Array); // -> true
console.log(myArray instanceof Object); // -> true
console.log(myArray instanceof String); // -> false

// Operadores de agrupación
// ()
console.log((1 + 2) * 3); // -> 9
console.log(1 + 2 * 3); // -> 7
// new
let myArray2 = new Array(1, 2, 3);
console.log(myArray2); // -> [1, 2, 3]

/* 
 * 2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 * que representen todos los tipos de estructuras de control que existan
 * en tu lenguaje.
 * Debes hacer print por consola del resultado de todos los ejemplos.
*/

// Operador ternario
let ternario = 10 > 5 ? 'Mayor' : 'Menor';
console.log(ternario); // -> Mayor

// if/else
let condicion = 10 > 5;
if (condicion) {
  console.log('10 es mayor que 5'); // Si la condicion es true
} else {
  console.log('10 no es mayor que 5'); // Si la condicion es false
}

// switch
let dia = 'lunes';
switch (dia) {
  case 'lunes':
    console.log('Inicia la semana');
    break;
  case 'viernes':
    console.log('Fin de semana');
    break;
  default:
    console.log('Día intermedio');
    break;
}

// try-catch-finally
let probar = 'PRUEBA';
try {
    probar = noExiste;  // ReferenceError -> noExiste no existe
} catch (error) {
    console.log('Hubo un error'); // -> Hubo un error
} finally {
    console.log('Esto es un finally'); // -> Esto es un finally
}
console.log(probar); // -> PRUEBA

// while
let fruits = ['apple', 'banana', 'orange', 'pineapple'];
let i = 0;

while (i < fruits.length) {
  console.log(fruits[i]); // Imprime los elementos del array fruits
  i++;
}

// do while
let j = 0;
do {
  console.log(fruits[j]); // Imprime solo el primer elemento del array fruits
  j++;
} while (j < 1);

// for
for (let contador = 10; contador >= 0; contador--) {
  console.log(contador); // Imprime los numeros del 10 al 0
}

// for of
for (let fruit of fruits) {
  console.log(fruit); // Imprime cada elemento del array fruits
}

// for in
let user = {
  name: 'John',
  age: 30,
  isAdmin: true,
  email: 'John@example.com'
};

for (let prop in user) {
  console.log(prop); // Imprime las propiedades del objeto user
  console.log(user[prop]); // Imprime los valores de las propiedades del objeto user
}

/*
 * 3. DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for (let extra = 10; extra <= 55; extra++) {
  if (extra % 2 === 0 && extra !== 16 && extra % 3 !== 0) {
    console.log(extra);
  }
}
