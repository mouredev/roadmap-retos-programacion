// Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje.

// STRINGS METHODS
let myName = "Pablo";
console.log(myName.length);

// ---- Acceder a las posiciones -- Búsqueda
console.log(myName[0], myName[1]);
console.log(myName.at(0), myName.at(1));

let myStr = "This is a very very very Short Sentence.";
let searchTerm = "very";
console.log("IndexOf:", myStr.indexOf(searchTerm));
console.log("LastIndexOf:", myStr.lastIndexOf(searchTerm));

// ---- Contactenación
console.log(myName.concat(" is my name"));
console.log(`${myName} is my name`);

// ---- Upper & Lowercase
console.log(myName.toLowerCase());
console.log(myName.toUpperCase());

// ---- Recorrido
console.log(myName.endsWith("lo"));
console.log(myName.startsWith("Pa"));
console.log(myName.includes("ab"));
console.log(myName.includes("ca"));

// ---- Extracción
const regexUpper = /[A-Z]/g; // Todas las mayús en un string
const regexSpecialCharacters = /[^\w\s']/g;

console.log(myStr.match(regexUpper)); // Extraer mayús usando regex

console.log(myStr.search(regexSpecialCharacters)); // Trae el index del caracter especial
console.log(myStr[myStr.search(regexSpecialCharacters)]); // Accediendo a la posición: "."

let myNewString = "Today will be an amazing day";
console.log(myNewString.slice(6, 10));
console.log(myNewString.slice(-3)); // Para empezar desde atrás

// ---- Divisón
console.log(myNewString.split(" ")); // Separa por espacios vacíos

// ---- Substring
console.log(myNewString.substring(2, 12)); // Extrae parte del string usando los indices

// ---- Reemplazo
console.log(myName.replace("b", "c"), myName);
console.log(myStr.replaceAll("very", "tiny"));

// ---- Transformación
let myNumb = 2344;
console.log(myNumb.toString());
console.log(String(myNumb)); // Recommended

// Trim
let mySpacedString = "      Hi!!    ";
console.log(mySpacedString.trim())
console.log(mySpacedString.trimEnd()) // Remueve espacios al final
console.log(mySpacedString.trimStart()) // Remueve espacios al inicio


// -------------- EXTRA CHALLENGE --------------

// Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
//  * Palíndromos: Se lee igual de izq a derecha 
//  * Anagramas: 
//  * - Isogramas