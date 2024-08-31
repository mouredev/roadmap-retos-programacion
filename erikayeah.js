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

// Operadores
let a = 10;
let b = 5;
let c = 15;
let d = 3;

// Aritméticos
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
console.log(a ** b);

// Lógicos
console.log(a && b);
console.log(a || b);
console.log(!a);

// De comparación
console.log(a === b);
console.log(a !== b);
console.log(a < b);
console.log(a > b);
console.log(a <= b);
console.log(a >= b);

// De asignación
console.log((a += b));
console.log((a -= b));
console.log((a *= b));
console.log((a /= b));
console.log((a %= b));
console.log((a **= b));

// De identidad
console.log(a === b);
console.log(a !== b);

// De pertenencia
let arr = [1, 2, 3, 4, 5];
console.log(1 in arr);
console.log(6 in arr);

// Bits
console.log(a & b);
console.log(a | b);
console.log(a ^ b);
console.log(~a);
console.log(a << b);
console.log(a >> b);
console.log(a >>> b);

// Estructuras de control

// Condicionales
let x = 10;
let y = 5;

if (x > y) {
  console.log("x es mayor que y");
} else {
  console.log("x es menor que y");
}

// Iterativas
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// Excepciones
try {
  throw "Error";
} catch (error) {
  console.log(error);
}

// Programa extra

let program = () => {
  for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
      console.log(i);
    }
  }
};

program();
