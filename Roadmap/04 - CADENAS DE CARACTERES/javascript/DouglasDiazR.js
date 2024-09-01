/*STRING */

const string = "Hola soy un string";
const string2 = "También soy un string";
const string3 = `   Ésto tambien" es 'una cadena'       `;

console.log(string3.length); // Devuelve la longitud del string

const text = "Hola Mundo";
console.log(text.charAt(1)); //Devuelve el caracter específicado con el índice de su posición
console.log(text.at(0)); //Devuelve el caracter específicado con el índice de su posición

console.log(text[5]); // Acceso a un caracter específico

console.log(string3.slice(1, 13)); // extrae una parte de una cadena y devuelve una nueva.
console.log(string3.substring(6, 13));

console.log(string.toUpperCase()); //convierte la cadena a mayúsculas
console.log(string.toLowerCase()); //convierte la cadena a minúsculas

console.log(string3.trim()); // elimina los espacios en blanco al principio y final de la cadena
console.log(string3.trimStart()); // elimina los espacios en blanco al principio de la cadena
console.log(string3.trimEnd()); // elimina los espacios en blanco al final de la cadena

console.log(string.includes("string")); //devuelve true si una cadena contiene un valor especificado

console.log(string3.indexOf("a")); //devuelve el indice del primer caracter que coincida con el indicado. Devuelve -1 si no encuenta coincidencia
console.log(string3.lastIndexOf("a")); //devuelve el indice del último caracter que coincida con el indicado

console.log(string.repeat(4)); // repite el string

console.log(string.replace("Hola", "Chao")); // método reemplaza un valor especificado con otro valor en una cadena
console.log(string.replace(/n/g, "x"));

console.log(string.split(" ")); //Convierte un string en un array

console.log(string3.match("en")); //devuelve un array con los resultados de hacer coincidir una cadena con otra cadena

console.log(string2.startsWith("Tam")); //retorna true si una cadena comienza con un valor especificado.
console.log(string.endsWith("g")); //retorna true si una cadena termina con un valor especificado.

/*PALÍNDROMOS*/

const isPalindromo = (palabra) => {
  const palabra2 = palabra.toLowerCase().split("").reverse();
  palabra.toLowerCase() === palabra2.join("")
    ? console.log("Es Palíndromo")
    : console.log("No es Palíndromo");
};

isPalindromo("arepera");

const isAnagrama = (palabra1, palabra2) => {
  if (
    palabra1.toLowerCase().split("").sort().join("") ===
    palabra2.toLowerCase().split("").sort().join("")
  )
    console.log("Son anagramas");
  else console.log("No son Anagramas");
};
isAnagrama("Aroma", "amaro");

const isIsograma = (palabra) => {
  const palabraArray = palabra.toLowerCase().split("");
  const palabraset = new Set(palabra.toLowerCase());
  palabraArray.length === palabraset.size
    ? console.log("Es Isograma")
    : console.log("No es Isograma");
};

isIsograma("murcielago");
