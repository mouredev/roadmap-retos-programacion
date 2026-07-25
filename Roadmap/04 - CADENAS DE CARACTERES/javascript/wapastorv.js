/* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en JavaScript. Todas las operaciones que se podrian hacer:
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación, etc...
*/

// Acceso a caracteres específicos
let cadena = "Hola mundo";
console.log(cadena[0]); // H
console.log(cadena.charAt(0)); // H
console.log(cadena.charCodeAt(0)); // 72

// Subcadenas
console.log(cadena.substring(0, 4)); // Hola
console.log(cadena.substr(0, 4)); // Hola
console.log(cadena.slice(0, 4)); // Hola
console.log(cadena.slice(-5)); // mundo

// Longitud
console.log(cadena.length); // 10

// Concatenación
let cadena2 = " desde JavaScript";
console.log(cadena + cadena2); // Hola mundo desde JavaScript
console.log(cadena.concat(cadena2)); // Hola mundo desde JavaScript
//console.log(cadena.concat(" desde JavaScript")); // Hola mundo desde JavaScript

// Repetición
console.log(cadena.repeat(3)); // Hola mundoHola mundoHola mundo

//Recorrido o Iteración
for (let i = 0; i < cadena.length; i++) {
    console.log(cadena[i]);// H o l a   m u n d o
}
for(let i in cadena){
    console.log(cadena[i]); // H o l a   m u n d o
}

// Conversión a mayúsculas y minúsculas
console.log(cadena.toUpperCase()); // HOLA MUNDO
console.log(cadena.toLowerCase()); // hola mundo

// Reemplazo
console.log(cadena.replace("mundo", "amigos")); // Hola amigos
console.log(cadena.replace(/o/g, "0")); // H0la mund0

// División
console.log(cadena.split(" ")); // ["Hola", "mundo"]

// Unión
console.log(["Hola", "mundo"].join(" ")); // Hola mundo

// Interpolación
let nombre = "Juan";
let edad = 25;
console.log(`Me llamo ${nombre} y tengo ${edad} años.`); // Me llamo Juan y tengo 25 años.

// Verificación
console.log(cadena.startsWith("Hola")); // true
console.log(cadena.endsWith("mundo")); // true
console.log(cadena.includes("mundo")); // true

console.log(cadena.match(/o/g)); // ["o", "o"] 
console.log(cadena.match(/o/g).length); // 2
console.log(cadena.match(/o/g).join("")); // oo
console.log(cadena.match(/o/g).toString()); // o,o
console.log(cadena.match(/o/g).reverse().join("")); // o,o (no funciona) porque reverse() no es una función de un array de strings sino de un array de objetos (en este caso, de un array de strings)

//Eliminar Espacios en Blanco (Trim)
let cadena3 = "    Hola mundo    ";
console.log(cadena3.trim()); // Hola mundo (elimina los espacios en blanco al principio y al final de la cadena)
console.log(cadena3.trimStart()); // Hola mundo    (elimina los espacios en blanco al principio de la cadena)
console.log(cadena3.trimEnd()); //     Hola mundo (elimina los espacios en blanco al final de la cadena)

// Buscar indice de un caracter o subcadena
console.log(cadena.indexOf("mundo")); // 5
console.log(cadena.lastIndexOf("o")); // 7
console.log(cadena.search("mundo")); // 5

// Comparación de Cadenas
let cadena4 = "Hola";
let cadena5 = "Hola";
console.log(cadena4 === cadena5); // true (compara el valor y el tipo de dato) 
console.log(cadena4 == cadena5); // true (compara el valor)
console.log(cadena4 > cadena5); // false (compara el valor en Unicode)
console.log(cadena4 < cadena5); // false (compara el valor en Unicode)
console.log(cadena4 >= cadena5); // true (compara el valor en Unicode)
console.log(cadena4 <= cadena5); // true (compara el valor en Unicode)

//Convertir Cadena a Array de Caracteres
let cadena6 = "Hola";
console.log(cadena6.split("")); // ["H", "o", "l", "a"]
let chars = [...cadena6];
console.log(chars); // ["H", "o", "l", "a"]

//Remplazo Complejo Usando Expresiones Regulares
let cadena7 = "Hola mundo";
console.log(cadena7.replace(/(mundo)/, "amigos")); // Hola amigos

let frase = "Ella es ella, pero ella no es él.";
console.log(frase.replace(/ella/g, "él")); // Él es él, pero él no es él.

//Convertir a Código ASCII
let cadena8 = "Hola";
let ascii = "";
for (let i = 0; i < cadena8.length; i++) {
    ascii += cadena8.charCodeAt(i) + " ";
}
console.log(ascii); // 72 111 108 97

//Convertir a Código ASCII con Expresiones Regulares
let cadena9 = "Hola";
let ascii2 = "";
let asciiArray = cadena9.split("").map(c => c.charCodeAt(0));
ascii2 = asciiArray.join(" ");
console.log(ascii2); // 72 111 108 97

//convertir a Código ASCII con Expresiones Regulares
const texto = "Hola";
let ascii3 = texto.replace(/./g, c => c.charCodeAt(0) + " ");
console.log(ascii3); // 72 111 108 97

//Convertir a Código ASCII con Expresiones Regulares y Eliminar Espacios en Blanco
const texto2 = "Hola"; 
let ascii4 = texto2.replace(/./g, c => c.charCodeAt(0) + " ").trim();
console.log(ascii4); // 72 111 108 97

//Convertir a Código ASCII con Expresiones Regulares y Eliminar Espacios en Blanco con Expresiones Regulares
const texto3 = "Hola";
let ascii5 = texto3.replace(/./g, c => c.charCodeAt(0) + " ").replace(/\s/g, "");
console.log(ascii5); // 7211110897

//Convertir a Código ASCII con Expresiones Regulares y Eliminar Espacios en Blanco con Expresiones Regulares y Convertir a Array
const texto4 = "Hola";
let ascii6 = texto4.replace(/./g, c => c.charCodeAt(0) + " ").replace(/\s/g, "").split("");
console.log(ascii6); // ["7", "2", "1", "1", "1", "0", "8", "9", "7"]

//Convertir a Código ASCII con Expresiones Regulares y Eliminar Espacios en Blanco con Expresiones Regulares y Convertir a Array de Números
const texto5 = "Hola";
let ascii7 = texto5.replace(/./g, c => c.charCodeAt(0) + " ").replace(/\s/g, "").split("").map(Number);
console.log(ascii7); // [7, 2, 1, 1, 1, 0, 8, 9, 7]


// Ejercio Practico
function esPalindromo(texto) {
    // Convertimos el texto a minúsculas, eliminamos todos los caracteres no alfanuméricos
    // y normalizamos para eliminar tildes
    const textoLimpio = texto
        .normalize('NFD')         // Descompone caracteres acentuados
        .replace(/[\u0300-\u036f]/g, '') // Elimina los diacríticos (tildes)
        .toLowerCase()            // Convertimos todo a minúsculas
        .replace(/[^a-z0-9]/g, ''); // Eliminamos caracteres no alfanuméricos

    // Comparamos el texto limpio con su versión invertida
    const esPalindromo = textoLimpio === textoLimpio.split('').reverse().join('');

    // Retornamos un mensaje en forma de string indicando si es palíndromo o no
    return esPalindromo ? `"${texto}" es un palíndromo` : `"${texto}" no es un palíndromo`;
}

const frase1= "Somos o no somos"
const frase2 = "Amó la paloma"
const frase3 = "palabra"
const frase4 = "No es palíndromo"

console.log(esPalindromo(frase1)); // "Somos o no somos" es un palíndromo
console.log(esPalindromo(frase2)); // "Amó la paloma" es un palíndromo
console.log(esPalindromo(frase3)); // "palabra" no es un palíndromo
console.log(esPalindromo(frase4)); // "No es palíndromo" no es un palíndromo





