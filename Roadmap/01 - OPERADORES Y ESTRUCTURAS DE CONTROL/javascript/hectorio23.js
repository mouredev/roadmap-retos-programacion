// Autor: Héctor Adán 
// GitHub: https://github.com/hectoiro23

"use strict";

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
* DIFICULTAD EXTRA:
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

// Operadores aritméticos
console.log("******** OPERADORES ARITMÉTICOS ********");
console.log("SUMA: 4 + 5 =", 4 + 5);
console.log("RESTA: 4 - 5 =", 4 - 5);
console.log("MULTIPLICACIÓN: 4 * 5 =", 4 * 5);
console.log("DIVISIÓN: 4 / 5 =", 4 / 5);
console.log("DIVISIÓN ENTERA: 4 // 5 =", Math.floor(4 / 5));
console.log("MÓDULO: 4 % 5 =", 4 % 5);
console.log("POTENCIA: 4 ** 5 =", 4 ** 5);

// Operadores de comparación
console.log("******** OPERADORES DE COMPARACIÓN ********");
console.log("IGUAL QUE: 4 == 5:", 4 == 5);
console.log("DIFERENTE DE: 4 != 5:", 4 != 5);
console.log("ESTRICTAMENTE IGUAL QUE: 4 === 5:", 4 === 5);
console.log("ESTRICTAMENTE DIFERENTE DE: 4 !== 5:", 4 !== 5);
console.log("MAYOR QUE: 4 > 5:", 4 > 5);
console.log("MENOR QUE: 4 < 5:", 4 < 5);
console.log("MAYOR O IGUAL QUE: 4 >= 5:", 4 >= 5);
console.log("MENOR O IGUAL QUE: 4 <= 5:", 4 <= 5);

// Operadores lógicos
console.log("******** OPERADORES LÓGICOS ********");
console.log("AND: true && false:", true && false);
console.log("OR: true || false:", true || false);
console.log("NOT: !true:", !true);

// Operadores de asignación
console.log("******** OPERADORES DE ASIGNACIÓN ********");
let x = 5;
console.log("x =", x);
x += 2;
console.log("x += 2 ->", x);
x -= 1;
console.log("x -= 1 ->", x);
x *= 3;
console.log("x *= 3 ->", x);
x /= 2;
console.log("x /= 2 ->", x);
x %= 4;
console.log("x %= 4 ->", x);
x **= 2;
console.log("x **= 2 ->", x);
x //= 3; // En JavaScript no hay operador de asignación para la división entera

// Operadores de identidad
console.log("******** OPERADORES DE IDENTIDAD ********");
let a = [1, 2, 3];
let b = a;
console.log("a === b:", a === b);
let c = [...a];
console.log("a === c:", a === c);
console.log("a == c:", a == c);

// Operadores de pertenencia
console.log("******** OPERADORES DE PERTENENCIA ********");
console.log("1 in [1, 2, 3]:", 1 in [1, 2, 3]); // Esto no funciona en JavaScript
console.log("4 not in [1, 2, 3]:", !(4 in [1, 2, 3])); // Esto tampoco funciona

// Operadores a nivel de bits
console.log("******** OPERADORES A NIVEL DE BITS ********");
console.log("AND: 4 & 5 =", 4 & 5);
console.log("OR: 4 | 5 =", 4 | 5);
console.log("XOR: 4 ^ 5 =", 4 ^ 5);
console.log("NOT: ~4 =", ~4);
console.log("Desplazamiento a la izquierda: 4 << 1 =", 4 << 1);
console.log("Desplazamiento a la derecha: 4 >> 1 =", 4 >> 1);

// Estructuras de control condicionales
console.log("******** ESTRUCTURAS DE CONTROL CONDICIONALES ********");
if (x > 2) {
    console.log("x es mayor que 2");
} else if (x == 2) {
    console.log("x es igual a 2");
} else {
    console.log("x es menor que 2");
}

// Estructuras de control iterativas
console.log("******** ESTRUCTURAS DE CONTROL ITERATIVAS ********");
console.log("Bucle for:");
for (let i = 0; i < 3; i++) {
    console.log("i =", i);
}

console.log("Bucle while:");
let n = 3;
while (n > 0) {
    console.log("n =", n);
    n--;
}

// Manejo de excepciones
console.log("******** MANEJO DE EXCEPCIONES ********");
try {
    let resultado = 10 / 0;
} catch (e) {
    console.log("No se puede dividir por cero");
} finally {
    console.log("Bloque finally ejecutado");
}

// DIFICULTAD EXTRA
console.log("******** DIFICULTAD EXTRA ********");
let values = "[ ";
for (let num = 10; num <= 55; num++) {
    if (num % 2 === 0 && num !== 16 && num % 3 !== 0) {
        values += num + ", ";
    }
}

console.log(values + "]");

