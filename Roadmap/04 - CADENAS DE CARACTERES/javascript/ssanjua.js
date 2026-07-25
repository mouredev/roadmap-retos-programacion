const contatenacion = 'hola' + ' mundo';          // hola mundo
const longitud = 'hola'.length;                   // 4
const caractereseEsp = 'hola'.charAt(0);          // h
const subcadenas = 'hola'.substring(0, 2);        // ho
const mayus = 'hola'.toUpperCase();               // HOLA
const minus = 'Hola'.toLowerCase();               // hola
const repetir = 'hola'.repeat(3);                 // holaholahola
const trim = ' hola '.trim();                     // hola
const includes = 'hola'.includes('o');            // true
const indexOf = 'hola'.indexOf('o');              // 1
const lastIndexOf = 'holaho'.lastIndexOf('o');    // 5
const replace = 'hola'.replace('o', 'a');         // hala
const slice = 'hola'.slice(0, 2);                 // ho
const split = 'hola'.split('');                   // ['h', 'o', 'l', 'a']
const terminaCon = 'hola'.endsWith('a');          // true
const empiezaCon = 'hola'.startsWith('h');        // true
const comparacion = 'hola'.localeCompare('hola'); // 0


console.log(contatenacion, longitud, caractereseEsp, subcadenas, mayus, minus, repetir, trim, includes, indexOf, lastIndexOf, replace, slice, split, terminaCon, empiezaCon, comparacion);


/* EXTRA
  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
  * para descubrir si son:
  * - Palíndromos
  * - Anagramas
  * - Isogramas
*/

function palindromo(palabra) {
  const palabraInvertida = palabra.split('').reverse().join('');
  return palabra === palabraInvertida;
}

function anagrama(palabra1, palabra2) {
  return palabra1.split('').sort().join('') === palabra2.split('').sort().join('');
}

function isograma(palabra) {
  const letras = palabra.split('');
  return letras.length === new Set(letras).size;
}

console.log(palindromo('oso'));         // true
console.log(anagrama('roma', 'amor'));  // true
console.log(isograma('murcielago'));    // true
console.log(isograma('oso'));           // false
console.log(palindromo('hola'));        // false
console.log(anagrama('rama', 'amor'));  // false