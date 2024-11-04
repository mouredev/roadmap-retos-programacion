/*
# #01 OPERADORES Y ESTRUCTURAS DE CONTROL
> #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

## Ejercicio  
*
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

// Tipo de Operadores en JavaScript
// Aritméticos
console.log(2 + 2); // Suma
console.log(2 - 2); // Resta
console.log(2 * 2); // Multiplicación
console.log(2 / 2); // División
console.log(2 % 2); // Módulo, que es el resto de la división
console.log(2 ** 2); // Exponenciación

// Lógicos
console.log(true && true); // AND
console.log(true || false); // OR
console.log(!true); // NOT

// De comparación
console.log(2 > 2); // Mayor que
console.log(2 < 2); // Menor que
console.log(2 >= 2); // Mayor o igual que
console.log(2 <= 2); // Menor o igual que
console.log(2 == 2); // Igual que
console.log(2 != 2); // Distinto que
console.log(2 === 2); // Igual que y mismo tipo

// De asignación
let a = 2;
console.log(a);

// De identidad
console.log(2 === 2); // Igual que y mismo tipo (true)
console.log(2 === '2'); // Igual que y mismo tipo (false)

// De pertenencia
let b = [1, 2, 3];
console.log(2 in b); // Existe en el array (true) 
console.log(4 in b); // Existe en el array (false)

// De bits
console.log(2 & 2); // AND
console.log(2 | 2); // OR
console.log(2 ^ 2); // XOR
console.log(~2); // NOT
console.log(2 << 2); // Desplazamiento a la izquierda
console.log(2 >> 2); // Desplazamiento a la derecha 
console.log(2 >>> 2); // Desplazamiento a la derecha sin signo, ejemplos con números negativos

// Estructuras de control en JavaScript
// Condicionales
if (2 === 2) {
  console.log('Condición verdadera');
}

// Iterativas
for (let i = 0; i < 2; i++) {
  console.log(i);
}

// Excepciones
try {
  throw 'Error';
}
catch (error) {
  console.log(error);
}

// EJECICIO DIFICULTAD EXTRA
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i); 
  }
}




