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

//Operadores Aritméticos
let x = 10;
let y = 5;
console.log("Suma: ", x + y); //Suma
console.log("Resta: ", x - y); //Resta
console.log("Multiplicación: ", x * y); //Multiplicación
console.log("División", x / y); //División
console.log("Residuo", x % y); //Residuo
console.log("Exponenciación: ", x ** y); //Exponenciación

//Operadores de asignación
let a = 10;
a += 3; // a = a +3
console.log("a += 3: ", a);
a -= 3; // a = a - 3
console.log("a -= 3: ", a);
a *= 3; // a = a * 3
console.log("a *= 3: ", a);
a /= 3; // a = a / 3
console.log("a /= 3: ", a);
a %= 3; // a = a % 3
console.log("a %= 3: ", a);
a **= 3; // a = a ** 3
console.log("a **= 3: ", a);

//Operadores de comparación
let b = 5;
console.log("a == b: ", a == b); //Igualdad
console.log("a === b: ", a === b); //Igualdad estricta
console.log("a != b: ", a != b); //Desigualdad
console.log("a !== b: ", a !== b); //Desigualdad estricta
console.log("a > b: ", a > b); //Mayor que
console.log("a < b: ", a < b); //Menor que
console.log("a >= b: ", a >= b); //Mayor o igual que
console.log("a <= b: ", a <= b); //Menor o igual que

//Operadores lógicos
console.log("true && false: ", true && false); // AND
console.log("true || false: ", true || false); // OR
console.log("!true: ", !true); //NOT

//Operadores de Bits
console.log(x << y); //Desplazamiento a la izquierda
console.log(x >> y); //Desplazamiento a la derecha
console.log(x >>> y); //Desplazamiento a la derecha sin signo
console.log(x & y); //Asignación AND bit a bit
console.log(x ^ y); //Asignación XOR bit a bit
console.log(x | y); //Asignación OR bit a bit
console.log(x && (x = y)); //Asignación AND lógico
console.log(x || (x = y)); //Asignación OR lógico
console.log(x ?? (x = y)); //Asignación de anulación lógica

//Estucturas de control

// Condicionales

if (x > y) {
  console.log("x es mayor que y");
} else {
  console.log("x no es mayor que y");
}

let z = 3;
switch (z) {
  case 1:
    console.log("Z es 1");
    break;
  case 2:
    console.log("Z es 2");
    break;
  case 3:
    console.log("z es 3");
    break;
  default:
    console.log("z no es 1,2 o 3");
}

//Iterativas
for (let i = 0; i < 5; i++) {
  console.log("For loop i: ", i);
}
let j = 0;
while (j < 5) {
  console.log("while loop j: ", j);
  j++;
}
let k = 0;
do {
  console.log("do while loop k: ", k);
  k++;
} while (k < 5);

//Excepciones
try {
  throw new error("Error");
} catch (error) {
  console.log("Mensaje: ", error.message);
} finally {
  console.log("Finally");
}

//Ejercicio Extra
function extraExercise() {
  for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i !== 16 && i % 3 !== 0) {
      console.log(i);
    }
  }
}

extraExercise();
