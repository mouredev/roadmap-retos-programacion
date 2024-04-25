/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

// Concatenation
// Used + or concat()
let string = 'Hello,';
let string2 = ' world!';
console.log(string + string2); // Hello, world!
console.log(string.concat(string2)); // Hello, world!

// String length
let stringLength = 'Good Morning!';
console.log(stringLength.length); // 13

// Slice String
// slice assign number for start 0 (include) and number for the finish (exclude)
let sliceExample = 'Do you go to the park?'
console.log(sliceExample.slice(0, 7)); // Do you

// Index Of
// Index of give you index where start the word.
let indexOfExample = 'My mom went shopping at Wallmart';
console.log(indexOfExample.indexOf('went')); // 7

// Split
// Split process the string and return a array with de words separated for an any character that you choose.
let splitExample = 'Hi,how,are,you';
console.log(splitExample.split(',')); // [ 'Hi', 'how', 'are', 'you' ]

// Replace
// Replace, search in the string the word that you give and replace for another one you give.
let replaceExample = 'on my way';
console.log(replaceExample.replace('way', 'table')); // on my table

// toUpperCase() / toLowerCase()
let exampleUpperLowerCase = 'She is a big woman.'
console.log(exampleUpperLowerCase.toLowerCase()); // she is a big woman.
console.log(exampleUpperLowerCase.toUpperCase()); // SHE IS A BIG WOMAN.

// charAt: Return index from a string
// this method init on 0
let exampleCharAt = 'Hello';
console.log(exampleCharAt.charAt(0)); // H

// Trim
// This method erase blanks on the start and finish from a string.
let exampleTrim = '     Hellow     ';
console.log(exampleTrim.trim()); // 'Hellow'

// Repeat
// This method repeats the text on a string any many times as you indicate.
console.log(exampleCharAt.repeat(5)); // HelloHelloHelloHelloHello


// endsWith/ startsWith
console.log(exampleCharAt.startsWith('H')); // True
console.log(exampleCharAt.endsWith('a')); // False

// includes
// This method verify if the string contain the word thar you indicate.
// is case sensitive
console.log(exampleCharAt.includes('Hello')); // True