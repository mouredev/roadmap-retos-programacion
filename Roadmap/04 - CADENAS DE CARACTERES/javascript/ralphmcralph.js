/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 */


// Acceso a caracteres específicos
let cadena = "Hola mundo";

console.log(cadena[0]); // H

// Subcadenas

console.log(cadena.substring(0, 4)); // Hola

// Longitud

console.log(cadena.length); // 10

// Concatenación

let cadena2 = " desde JavaScript";

console.log(cadena + cadena2); // Hola mundo desde JavaScript

// Repetición

console.log(cadena.repeat(3)); // Hola mundoHola mundoHola mundo

// Recorrido

for (let i = 0; i < cadena.length; i++) {
    console.log(cadena[i]);
}

// Conversión a mayúsculas y minúsculas

console.log(cadena.toUpperCase()); // HOLA MUNDO

console.log(cadena.toLowerCase()); // hola mundo

// Reemplazo

console.log(cadena.replace("mundo", "amigos")); // Hola amigos

// División

console.log(cadena.split(" ")); // ["Hola", "mundo"]

// Unión

console.log(["Hola", "mundo"].join(" ")); // Hola mundo

// Interpolación

let nombre = "Ralph";

console.log(`Hola ${nombre}`); // Hola Ralph

// Verificación

console.log(cadena.includes("mundo")); // true

console.log(cadena.startsWith("Hola")); // true

console.log(cadena.endsWith("mundo")); // true

console.log(cadena.indexOf("mundo")); // 5

console.log(cadena.lastIndexOf("o")); // 7

console.log(cadena.search("mundo")); // 5

console.log(cadena.match(/o/g)); // ["o", "o", "o"]

console.log(cadena.match(/o/g).length); // 3

/* DIFICULTAD EXTRA(opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
*   - Palíndromos
*   - Anagramas
*   - Isogramas
*/

let palabra1 = "Yuxtaponer"
let palabra2 = "Radar"

function isPalindrome(word) {

    word = word.toLowerCase();

    return word === word.split("").reverse().join("");

}

function printResult(word) {
    console.log(isPalindrome(word) ? `La palabra ${word.toLowerCase()} es un palíndromo` : `La palabra ${word.toLowerCase()} no es un palíndromo`);
}


printResult(palabra1);
printResult(palabra2);

// Anagrama

function isAnagram(word1, word2) {

    return word1.toLowerCase().split("").sort().join("") === word2.toLowerCase().split("").sort().join("");

}

console.log(isAnagram(palabra1, palabra2) ? `${palabra1} es un anagrama de ${palabra2.toLowerCase()}` : `${palabra1} no es un anagrama de ${palabra2.toLowerCase()}`);

// Isograma

function isIsogram(word) {

    letterCounter = new Map();

    word.toLowerCase().split("").forEach(letter => {
        if (letterCounter.get(letter)) {

            letterCounter.set(letter, letterCounter.get(letter) + 1)

        } else {
            letterCounter.set(letter, 1);
        }
    }
    );

    const uniqueValues = new Set(letterCounter.values());

    return uniqueValues.size === 1;

}

console.log(isIsogram(palabra1) ? `La palabra ${palabra1.toLowerCase()} es un isograma` : `La palabra ${palabra1.toLowerCase()} no es un isograma`);

console.log(isIsogram(palabra2) ? `La palabra ${palabra2.toLowerCase()} es un isograma` : `La palabra ${palabra2.toLowerCase()} no es un isograma`);






