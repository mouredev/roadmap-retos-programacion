// #01 OPERADORES Y ESTRUCTURAS DE CONTROL

// ## Ejercicio

// Asignacion de varialbes

let num1 = 25;
let num2 = 5;

console.group("Operadores Aritméticos");
// Operadores Aritméticos de JavaScript
// Operador de Suma
const suma = num1 + num2;
console.log(`La suma de los numeros ${num1} + ${num2} es igual a ${suma}`);
// Operador de Resta
const resta = num1 - num2;
console.log(`La resta de los numeros ${num1} - ${num2} es igual a ${resta}`);
// Operador de Multiplicación
const multiplicacion = num1 * num2;
console.log(
  `La multiplicacion de los numeros ${num1} x ${num2} es igual a ${multiplicacion}`
);
// Operador de division
const division = num1 / num2;
console.log(
  `La division de los numeros ${num1} / ${num2} es igual a ${division}`
);
// Operador de modulo o resto
const modulo = num1 % num2;
console.log(`El resto de la division de ${num1} entre ${num2} es ${modulo}`);
// Operador de exponencial
const exp = num1 ** 2;
console.log(`El numero ${num1} elevado a la ${num2} es igual a ${exp}`);
// (Las varibales deben estar guardadas en let de lo contrario no podra incrementar o decrementar al ser constante)
// Operador de incremento
num1++;
console.log(`El numero incrementado +1 es ${num1}`);
// Operador de decremento
num2--;
console.log(`El numero decrementado -1 es ${num2}`);

console.groupEnd("Operadores Aritméticos");

console.group("Operadores de asignación");
// Operadores de asignación de JavaScript
// Operador de asignación
let i = 5;
num1 = 45;
console.log(` Asignacion ${num1}`);
// Operador de asignacion de adición
num1 = num1 + i; // Forma significativa
console.log(`Asignacion de suma significativa${num1}`);
num1 += i; // Forma abrevidada
console.log(`Asignacion de suma abrevidada${num1}`);
// Operador de asignacion de resta
num1 = num1 - i; // Forma significativa
console.log(`Asignacion de resta significativa${num1}`);
num1 -= i; // Forma abrevidada
console.log(`Asignacion de resta abreviada${num1}`);
// Operador de asignacion de multiplicación
num1 = num1 * i; // Forma significativa
console.log(`Asignacion de multiplicacion significativa${num1}`);
num1 *= i; // Forma abrevidada
console.log(`Asignacion de multiplicacion abreviada${num1}`);
// Operador de asignacion de division
num1 = num1 / i; // Forma significativa
console.log(`Asignacion de division significativa${num1}`);
num1 /= i; // Forma abrevidada
console.log(`Asignacion de division abreviada${num1}`);
// Operador de asignacion de módulo o resto
num1 = num1 % i; // Forma significativa
console.log(`Asignacion de módulo significativa${num1}`);
num1 %= i; // Forma abrevidada
console.log(`Asignacion de módulo abreviada${num1}`);
// Operador de asignacion de exponente
num1 = num1 ** i; // Forma significativa
console.log(`Asignacion de exponente significativa${num1}`);
num1 *= i; // Forma abreviada
console.log(`Asignacion de exponente abreviada${num1}`);

console.groupEnd("Operadores de Asignación");

console.group("Operadores de comparación");
// Operadores de comparación
let a = 25;
let b = "25";

// Operador de igualdad
console.log(a == b); // Devuelve true si es igual en dato o valor
// Operador de igualdad estrictamente
console.log(a === b); // Devuelve true si es igual en dato y valor
// operador de desigualdad
console.log(a != b); // Devuelve true si es desigual en dato o valor
// Operador de desigualdad estrictamente
console.log(a !== b); //Devuelve true si es desigualdad en dato y valor
// Operador de mayor que
console.log(a > b); // Devuelve true si a es mayor que b
// Operador de menor que
console.log(a < b); // Devuelve true si a es mayor que b
// operador de mayor o igual que
console.log(a >= b); // Devuelve true si a es mayor o igual que b
// Operador de menor o igual que
console.log(a <= b); // Devuelve true si a es menor o igual que b
console.groupEnd("Operadores de comparación");

console.group("Operadores logicos");
// Operador AND &&
console.log(5 === 5 && 5 === 5); // Devuelve true si ambas condiciones son verdad
// Operador OR ||
console.log(5 === 6 || 7 === 7); // Devuelve true si una de las dos condiciones es verdad
// Operador NOT !
let c = true;
console.log(!c); // Devuelve false si c es true, y true si c es false
console.groupEnd("Operadores logicos");

console.group("Operador condeicional ternario ");

let d = 5;
console.log(d % 2 === 0 ? "Par" : "Impar");

console.groupEnd("Operador condeicional ternario ");

// Estructura de control
// Estructura iterativa for
for (i = 1; i < 11; i++) {
  console.log(` 2 x ${i} = ${i * 2}`);
}

// Estructura iterativa FOR mezclada con estura condeicional IF
for (i = 1; i < 101; i++) {
  if (i % 2 === 0) {
    console.log(`El numero ${i} es par`);
  } else if (i % 2 !== 0) {
    console.log(`El numero ${i} es impar`);
  }
}

// Estructura iterativa WHILE
let j = 1;
while (j < 101) {
  console.log(`El numero es ${j}`);
  j++;
}

/* EJERCICIO EXTRA
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 */

let array = [];
function numerosComprendidos(base, limite) {
  for (let i = base; i < limite; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
      array.push(i);
    }
  }
}

numerosComprendidos(10, 55);
console.log(array);
