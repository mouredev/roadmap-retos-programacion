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

//* 1. OPERADORES

let a = 1;
let b = 2;
let c = [a, b];
let d = { c: c, 3: 3 };

// Asignación
console.log("Asignación: ", (a = b));
console.log("Asignación de adición ", (a += b));
console.log("Asignación de resta: ", (a -= b));
console.log("Asignación de multiplicación: ", (a *= b));
console.log("Asignació de división: ", (a /= b));
console.log("Asignación de residuo: ", (a %= b));
console.log("Asignación de exponenciación: ", (a **= b));
console.log("Asignación desplazamiento a la izquierda: ", (a <<= b));
console.log("Asignación de desplazamiento a la derecha: ", (a >>= b));
console.log("Asignación de desplazamiento a derecha sin signo: " + (a >>>= b));
console.log("Asignación AND bit a bit: ", (a &= b));
console.log("Asignación XOR bit a bit: ", (a ^= b));
console.log("Asignación OR bit a bit: ", (a |= b));
console.log("Asignación AND lógico: ", (a &&= b));
console.log("Asignación OR lógico: ", (a ||= b));
console.log("Asignación de anulación lógica: ", (a ??= b));

// Comparacion
console.log("Igual: ", a == b);
console.log("No es igual: ", a != b);
console.log("Estrictamente igual: ", a === b);
console.log("Desigualdad estricta: ", a !== b);
console.log("Mayor que: ", a > b);
console.log("Mayor o igual que: ", a >= b);
console.log("Menor que: ", a < b);
console.log("Menor o igual: ", a <= b);

// Aritmeticos
console.log("Residuo: ", a % b);
console.log("Incremento: ", a++);
console.log("Decremento: ", a--);
console.log("Negación unaria: ", -a);
console.log("Positivo unario: ", +a);
console.log("Operador de exponenciación: ", a ** b);

// Bit a Bit
console.log("AND a nivel de bits: ", a & b);
console.log("OR a nivel de bits: ", a | b);
console.log("XOR a nivel de bits: ", a ^ b);
console.log("NOT a nivel de bits: ", ~a);
console.log("Desplazamiento a la izquierda: ", a << b);
console.log("Desplazamineto a derecha de propagación de signo: ", a >> b);
console.log("Desplazamiento a la deracha de relleno cero: ", a >>> b);

// Lógicos
console.log("AND lógico: ", a && b);
console.log("OR lógico: ", a || b);
console.log("NOT lógico: ", !a);

// Ternario
console.log("Ternario: ", a > b ? a : b);

// Coma
console.log("Coma: ", (a = b), (b = a));

// Unarios
console.log("Delete: ", delete c[0]);
console.log("Type of: ", typeof a);
console.log("Void: ", void a);

// Relacionales
console.log("In: ", 3 in d);
console.log("Instance of: ", d instanceof Object);

//* Estructuras de Control

// If - Else
if (a === b) {
  console.log("Son iguales");
} else {
  console.log("No son iguales");
}

// Switch
switch (a) {
  case 1:
    console.log("a es igual a 1");
    break;
  case 2:
    console.log("a es igual a 2");
  default:
    console.log("a no es igual a 1 ni a 2");
    break;
}

// For
for (let i = 0; i < c.length; i++) {
  console.log(c[i]);
}

// While
let j = 1;
while (j <= 10) {
  console.log(j);
  j++;
}

// Do While
let k = 10;
do {
  console.log(k);
  k--;
} while (k > 0);

//* Dificultad Extra
for (let index = 10; index <= 55; index++) {
  if (index !== 16 && index % 3 !== 0 && index % 2 === 0) console.log(index);
}
