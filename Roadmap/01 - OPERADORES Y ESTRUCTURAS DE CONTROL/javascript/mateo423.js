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

// Operadores Aritmeticos;
let a = 5;
let b = 4;
console.log(`Suma: ${a} + ${b} =  ${a + b}`);
console.log(`Resta: ${a} - ${b} = ${a - b}`);
console.log(`Multiplicacion: ${a} * ${b} = ${a * b}`);
console.log(`Division : ${a} / ${b} =  ${a / b}`);
console.log(`Potenciacion: ${a} ** ${b} =  ${a ** b}`);
console.log(`Modulo: ${a} % ${b} = ${a % b}`);
console.log(`Incrementa en 1 y devuelve  el operando: ++num1 = ${++a}`);
console.log(`Devuelve  el operando e incrementa en 1: num1++ = ${b++}`);
console.log(`Decrementa en 1 y devuelve  el operando: ++num1 = ${--a}`);
console.log(`Devuelve  el operando y decrementa en 1: num1++ = ${b--}`);
console.log(`Invierte el valor del operando: -num1 = ${-a}`);
console.log(`Convierte el operando en un número: +num3 = ${typeof (+b)}`);
console.log('######################')

// Operadores Logicos;
console.log('Operadores Logicos');
const and = true && true;
const or = true || true;
const not = !true;

console.log(and);
console.log(or);
console.log(not);
console.log('######################')

// Operadores de Comparacion;
console.log('Operadores de Comparacion');
const igual = 5 == '5';
const estrictamenteIgual = 5 === '5';
const diferente = 10 !== 5;
const mayorQue = 15 > 10;
const menorQue = 7 < 12;
const mayorIgualQue = 8 >= 20;
const menorIgualQue = 9 <= 8;

console.log(igual);
console.log(estrictamenteIgual);
console.log(diferente);
console.log(mayorQue);
console.log(menorQue);
console.log(mayorIgualQue);
console.log(menorIgualQue);
console.log('################################')
// Operadores de bit a bit;
let x = 9;
let y = 14;

console.log(`Operador &: x & y = ${x & y}`);
console.log(`Operador |: x | y = ${x | y}`);
console.log(`Operador ^: x & y = ${x ^ y}`);
console.log(`Operador ~: ~x = ${~x}`);
console.log(`Operador <<: x << y = ${x << y}`);
console.log(`Operador >>: x >> y = ${x >> y}`);
console.log(`Operador >>>: x >>> y = ${x >>> y}`);
console.log('######################');

// Estructura de control
console.log('Estructura de control');
let num1 = 5;
let num2 = 4;

if (num1 < num2) {
  console.log(`El numero ${num1} es menor que el numero ${num2}`);
} else if (num1 > num2) {
  console.log(`El numero ${num1} es mayor que el numero ${num2}`);
} else {
  console.log(`El numero ${num1} es igual al numero ${num2}`);
}
console.log('#####################');
// Bucle foor ;

for (let i = 0; i <= 10; i++) {
  console.log(`Numero: ${i}`)
};
console.log('##################');

// Bucle while;
let i = 1;
while (i <= 10) {
  let resultado = 12 * i;
  if (resultado === 48) {
    console.log("Yuju... ya llegamos a 48 Flecidades. ")
  } else {
    console.log(`12*${i} = ${resultado}`)
  }
  i++;
}
// switch
let day = 'friday';
let dia;

switch (day) {
  case "monday":
    dia = 'lunes';
    break;
  case "tuesday":
    dia = 'martes';
    break;
  case "wednesday":
    dia = 'miércoles';
    break;
  case "thursday":
    dia = 'jueves';
    break;
  case "friday":
    dia = 'viernes';
    break;
  case 'saturday':
    dia = 'sábado';
    break;
  default:
    dia = 'Domingo';
}
console.log(`El día es ${dia}`);

// Blue for of
let lista = [1, 4, 6, 2, 3, 7, 10, 12];
console.log(`Estructura for...of`);
for (let valor of lista) {
  console.log(valor);
}

// Excepciones
console.log(`Excepciones`);
const miConstante = 30;

try {
  miConstante = 20;
} catch (error) {
  console.error(`Ha habido una excepción ${error}`);
}
/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

console.log('DIFICULTAD EXTRA');
for (let i = 10; i <= 55; i++) {
  if (i % 2 == 0 && i != 16 && i % 3 != 0) {
    console.log(`Numero ${i}`);
  }

}



