let sentence = "Esto es una prueba";

console.log(sentence.at(1)); // Retorna el caracter en la posición 1, permite valores negativos para contar desde el final de la cadena
console.log(sentence.at(-1));

console.log(sentence.charAt(1)); // Retorna el caracter en la posición 1, no permite valores negativos

console.log(sentence.charCodeAt(1)); // Retorna el código unicode del caracter en la posición 1
console.log(sentence.codePointAt(1));

let str1 = 'Hola'
let str2 = 'Mundo'
console.log(str1.concat(' ', str2)) // Concatena dos cadenas

console.log(sentence.endsWith('prueba')); // Comprueba si la cadena termina con el texto especificado

console.log(sentence.startsWith('Esto')); // Comprueba si la cadena comienza con el texto especificado

console.log(sentence.includes('es')); // Comprueba si la cadena contiene el texto especificado

console.log(sentence.indexOf('es')); // Devuelve la posición de la primera aparición del texto especificado en la cadena. No soporta expresiones regulares

console.log(sentence.isWellFormed()); // Comprueba si la cadena es un mensaje válido

console.log(sentence.lastIndexOf('a')); // Devuelve la posición de la última aparición del texto especificado en la cadena

let str3 = 'reservé'
let str4 = 'RESERVE'
console.log(str3.localeCompare(str4)); // Compara dos cadenas en base al idioma local

const paragraph = 'The quick brown fox jumps over the lazy dog. It barked.';
const regex = /[A-Z]/g;
console.log(paragraph.match(regex)) // Devuelve una lista de todas las coincidencias de la expresión regular

console.log(sentence.padEnd(25, '*')); // Agrega asteriscos al final de la cadena hasta alcanzar la longitud especificada

console.log(sentence.padStart(25)); // Agrega espacios al principio de la cadena hasta alcanzar la longitud especificada

console.log(str1.repeat(3)); // Repetir la cadena 3 veces

console.log(sentence.replace('es', 'is')); // Reemplaza el texto especificado por otro texto

console.log(sentence.replaceAll('es', 'is')); // Reemplaza todos los ocurrencias del texto especificado por otro texto

console.log(sentence.search('es')); // Devuelve la posición de la primera aparición del texto especificado en la cadena. Soporta expresiones regulares

console.log(sentence.slice(1, 3)); // Devuelve una nueva cadena que contiene las letras del texto original desde la posición especificada hasta la posición especificada - 1

console.log(sentence.split('es')); // Divide la cadena en una lista de cadenas, separando cada una por el texto especificado

console.log(sentence.substring(1, 3)); // Devuelve una nueva cadena que contiene las letras del texto original desde la posición especificada hasta la posición especificada

console.log(sentence.toLocaleLowerCase()); // Convierte la cadena a minúsculas en base al idioma local

console.log(sentence.toLocaleUpperCase()); // Convierte la cadena a mayúsculas en base al idioma local

console.log(sentence.toLowerCase()); // Convierte la cadena a minúsculas

console.log(sentence.toUpperCase()); // Convierte la cadena a mayúsculas

let str5 = new String('Hola Mundo');
console.log(str5.toString()); // Convierte la cadena a una cadena de caracteres

console.log(str5.valueOf()); // Convierte la cadena a una cadena de caracteres

let str6 = '    Hola Mundo    '
console.log(str6.trim()); // Elimina espacios en blanco al principio y final de la cadena

console.log(str6.trimEnd()); // Elimina espacios en blanco al final de la cadena

console.log(str6.trimStart()); // Elimina espacios en blanco al principio de la cadena

console.log(sentence.length); // Devuelve la longitud de la cadena


// Dificultad Extra
let str7 = 'radar'
let str8 = 'amor'
let str9 = 'roma'
let str10 = 'murcielago'

function polindromo(str) {
  return str.toLowerCase().split('').reverse().join('') === str.toLowerCase() ? true : false
}

function anagrama(str1, str2) {
  return str1.toLowerCase().sort === str2.toLowerCase().sort ? true : false
}

function isograma(str) {
  let mySet = new Set(str)
  return str.length === mySet.size ? true : false
}

console.log(`¿La palabra ${str7} es políndroma?: ${polindromo(str7)}`)
console.log(`¿Las palabras ${str8} y ${str9} son anagramas?: ${anagrama(str8, str9)} `)
console.log(`¿La palabra ${str10} es un isograma?: ${isograma(str10)}`)
