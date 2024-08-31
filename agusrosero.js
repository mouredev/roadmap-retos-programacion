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

// EJERCICIO:
// Aritméticos
console.log(2 + 2);
console.log(2 - 2);
console.log(2 * 2);
console.log(2 / 2);
console.log(2 % 2);
console.log(2 ** 2);

// Lógicos
console.log(true && true);
console.log(true || true);
console.log(!true);

// Comparación
console.log(2 === 2);
console.log(2 !== 2);
console.log(2 > 2);
console.log(2 < 2);
console.log(2 >= 2);
console.log(2 <= 2);

// Asignación
let a = 2;
a += 2;
console.log(a);
a -= 2;
console.log(a);
a *= 2;
console.log(a);
a /= 2;
console.log(a);
a %= 2;
console.log(a);
a **= 2;
console.log(a);

// Incremento - Decremento
let b = 2;
b++;
console.log(b);
b--;
console.log(b);

// Estructuras de control
if (true) {
  console.log("Ejecutando el if");
} else {
  console.log("Ejecutando el else");
}

while (true) {
  console.log("Ejecutando el while");
  break;
}

for (let i = 0; i < 10; i++) {
  console.log("Ejecutando el for");
  break;
}

// do {
//   console.log("Ejecutando el do");
// } while (true);

try {
  console.log("Ejecutando el try");
} catch (error) {
  console.log("Ejecutando el catch");
} finally {
  console.log("Ejecutando el finally");
}

// DIFICULTAD EXTRA:
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
  }
}
