// Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje.

// STRINGS METHODS
let myName = "Pablo";

// Acceder a las posiciones
console.log(myName[0], myName[1]);
console.log(myName.length);

// Contactenación
console.log(myName.concat(" is my name"));
console.log(`${myName} is my name`);

// Upper & Lowercase
console.log(myName.toLowerCase());
console.log(myName.toUpperCase());

// 
console.log(myName.endsWith("lo"));
console.log(myName.includes("ab"));

let myStr = 'This is a very short sentence'
let searchTerm = 'very'
console.log(myStr.indexOf(searchTerm))
