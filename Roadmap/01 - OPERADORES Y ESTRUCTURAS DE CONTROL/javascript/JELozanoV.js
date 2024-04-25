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

let suma = 1 + 1;
let resta = 1 - 1;
let multiplicacion = 1 * 1;
let division = 1 / 1 ;
let resto = 2 % 2 ;

// Operadores logicos 

//      &&
let esVerdadreoAND = true && true 
let esFalsoAND = true && false 
let esFalsoAND2 = false && true;  
let esFalsoAND3 = false && false;

//     || 
let esVerdaderoOR = true || true;
let esFalsoOR = true || false;
let esFalsoOR2 = false || true;
let esFalsoOR3 = false || false; 

//     ! 
let falsoInvertido = !true;
let verdaderoInvertido = !false

// De comparacion 

/* Igualdad (==) */
5 == 5;       // true
'5' == 5;     // true (coerción de tipo)
5 == '5';     // true (coerción de tipo)
5 == 10;      // false

/* Igualdad estricta (===) */
5 === 5;      // true
'5' === 5;    // false
5 === '5';    // false

/* Desigualdad (!=) */
5 != 10;      // true
5 != '5';     // false (coerción de tipo)


/* Desigualdad estricta (!==) */
5 !== '5';    // true
5 !== 5;      // false

/* Mayor que (>) */
10 > 5;       // true

/* Menor que (<) */
5 < 10;       // true

/* Mayor o igual que (>=) */
10 >= 10;     // true

/* Menor o igual que (<=) */
5 <= 10;      // true

/* De asignacion (=) */
var variableVar = "Variable" // asigna una variable string 
variableVar = 0 // Reasigna a una variable number 

/* De identidad */ 
5 === 5;      // true
'5' === 5;    // false
5 === '5';    // false

5 !== '5';    // true
5 !== 5;      // false






