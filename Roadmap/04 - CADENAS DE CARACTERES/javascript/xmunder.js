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

// Acceso a caracteres específicos
let cadena = "Hola, mundo!";
console.log(cadena[0]); // Muestra "H"
console.log(cadena.charAt(7)); // Muestra "m"

// Subcadenas
let subcadena = cadena.substring(6, 11);
console.log(subcadena); // Muestra "mundo"

// Longitud de la cadena
console.log(cadena.length); // Muestra 12

// Concatenación
let otraCadena = " Qué tal?";
let resultadoConcatenacion = cadena + otraCadena;
console.log(resultadoConcatenacion); // Muestra "Hola, mundo! Qué tal?"

// Repetición
let cadenaRepetida = cadena.repeat(3);
console.log(cadenaRepetida); // Muestra "Hola, mundo!Hola, mundo!Hola, mundo!"

// Recorrido
for (let i = 0; i < cadena.length; i++) {
  console.log(cadena[i]);
}

// Conversión a mayúsculas y minúsculas
console.log(cadena.toUpperCase()); // Muestra "HOLA, MUNDO!"
console.log(cadena.toLowerCase()); // Muestra "hola, mundo!"

// Reemplazo
let nuevaCadena = cadena.replace("mundo", "amigo");
console.log(nuevaCadena); // Muestra "Hola, amigo!"

// División
let palabras = cadena.split(", ");
console.log(palabras); // Muestra ["Hola", "mundo!"]

// Unión
let nuevaCadenaUnida = palabras.join(" ");
console.log(nuevaCadenaUnida); // Muestra "Hola mundo!"

// Interpolación
let nombre = "Cristian";
let edad = 21;
console.log(`Mi nombre es ${nombre} y tengo ${edad} años.`);

// Verificación
console.log(cadena.includes("mundo")); // Devuelve true
console.log(cadena.startsWith("Hola")); // Devuelve true
console.log(cadena.endsWith("!")); // Devuelve true

// Dificultad extra

const transformString = (myString) => {
  return myString.replace(/\s/g, "").toLowerCase();
};

const isPalindrome = (myString) => {
  const myWord = transformString(myString);
  myWord === Array.from(myWord).reverse().join("")
    ? console.log(`${myString} es un Palíndromo`)
    : console.log(`${myString} no es un Palíndromo`);
};

const isAnagram = (myString1, myString2) => {
  const myWord1 = transformString(myString1);
  const myWord2 = transformString(myString2);
  if (myWord1.length === myWord2.length) {
    const isAnagram = Array.from(myWord1).every((char) =>
      myWord2.includes(char)
    );
    isAnagram
      ? console.log(`${myString1} y ${myString2} son Anagramas`)
      : console.log(`${myString1} y ${myString2} no son Anagramas`);
  }
};

const isIsogram = (myString) => {
  const myWord = transformString(myString);
  const letter = myWord.split("").sort();
  for (let index = 0; index < letter.length; index++) {
    if (letter[index] === letter[index + 1]) {
      return console.log(`${myString} no es un Isograma`);
    }
  }
  return console.log(`${myString} es un Isograma`);
};

isPalindrome("Oso");
isPalindrome("Casa");
isAnagram("Roma", "Amor");
isAnagram("Rojo", "Verde");
isIsogram("Cristian");
isIsogram("Hamburguesa");
