//! Operaciones con cadenas

//* Concatenacion de cadenas
let str1 = "Hola";
let str2 = "Mundo";
let result = str1 + " " + str2; // "Hola Mundo"

//* Acceso a caracteres
let str = "JavaScript";
let char = str[0]; // "J"
let charAt = str.charAt(0); // "J"

//* Longitud de una cadena
let string = "Hola Mundo";
let length = string.length; // 10

//* Cambio de mayusculas a minusculas
let str3 = "Hola Mundo";
let upperCase = str3.toUpperCase(); // "HOLA MUNDO"
let lowerCase = str3.toLowerCase(); // "hola mundo"

//* Extraccion de subcadenas
let str4 = "Hola Mundo";
let substring = str4.substring(0, 4); // "Hola"
let slice = str4.slice(5); // "Mundo"

//* Division de una cadena
let str5 = "Hola Mundo";
let split = str5.split(" "); // ["Hola", "Mundo"]

//* Reemplazo de texto
let str6 = "Hola Mundo";
let replaced = str6.replace("Mundo", "JavaScript"); // "Hola JavaScript"

//* Busqueda de texto
let str7 = "Hola Mundo";
let indexOf = str7.indexOf("Mundo"); // 5
let includes = str7.includes("Mundo"); // true

//* Eliminar espacios en blanco
let str8 = "   Hola Mundo   ";
let trimmed = str8.trim(); // "Hola Mundo"

//* Repetir cadenas
let str9 = "Hola";
let repeated = str9.repeat(3); // "HolaHolaHola"

//* Conversion de una cadena en un arreglo de caracteres
let str10 = "Hola";
let array = Array.from(str10); // ["H", "o", "l", "a"]

//* Verificacion de inicio y final de una cadena
let str11 = "Hola Mundo";
let startsWith = str11.startsWith("Hola"); // true
let endsWith = str11.endsWith("Mundo"); // true

//* Interpolacion de cadenas (template literals)
let nombre = "Juan";
let saludo = `Hola, ${nombre}`; // "Hola, Juan"

//* Obtener codigo de caracter
let str12 = "A";
let charCode = str12.charCodeAt(0); // 65

//* Recorrido
let str13 = "JavaScript";
for (let i = 0; i < str13.length; i++) {
  console.log(str13[i]);
}
// J
// a
// v
// a
// S
// c
// r
// i
// p
// t

//* Union
let arr = ["Hola", "Mundo"];
let joined = arr.join(" "); // "Hola Mundo"

//! Ejercicio Extra
// Polindromo: es una palabra, numero o frace que se lee igual de izquierda a derea que de derecha a izquierda
function isPalindromo(stringA) {
  let palindromo = Array.from(stringA);
  let revercedPolindromo = [];
  for (let i = stringA.length - 1; i >= 0; i--) {
    revercedPolindromo.push(stringA[i]);
  }
  let isPalindromo = true;
  for (let j = 0; j < palindromo.length; j++) {
    if (palindromo[j].toLowerCase() !== revercedPolindromo[j].toLowerCase()) {
      isPalindromo = false;
      break;
    }
  }
  if (isPalindromo) {
    return `${stringA} es palindromo`;
  } else {
    return `${stringA} no es palindromo`;
  }
}
// Anagrama: es una palabra o frace que se forma reordenando las letras de otra palabra o frace original, utilizando exactamente las mismas letras con la misma frecuencia.
function cleanSort(string) {
  return string
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "")
    .split("")
    .sort()
    .join("");
}
function isAnagrama(stringA, stringB) {
  let string1 = cleanSort(stringA);
  let string2 = cleanSort(stringB);

  if (string1 === string2) {
    return `${stringA} y ${stringB} son Anagramas`;
  } else {
    return `${stringA} y ${stringB} no son Anagramas`;
  }
}
// Isograma: es una palabra o frace en la que ninguna letra se repita
function isIsograma(string) {
  let newString = string.toLowerCase().replace(/[^a-z]/g, "");
  let letters = new Set();

  for (const letter of newString) {
    if (letters.has(letter)) {
      return `${string} no es un Isograma`;
    }
    letters.add(letter);
  }
  return `${string} es un Isograma`;
}

console.log(isPalindromo("radar"));
console.log(isAnagrama("amors", "roma"));
console.log(isIsograma("isogramas"));
