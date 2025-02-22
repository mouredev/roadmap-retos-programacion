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
 * - Palíndromos (se leen igual de izquierda a derecha y de derecha a izquierda)
 * - Anagramas (Las letras de una palabra, si se escriben en orden diferente, forman otra)
 * - Isogramas (Las letras se repiten el mismo número de veces)
 */

// String length
let text = "ABCDEFGHIJKLLLMNOPQRSTUVWXYZ";
let length = text.length;
console.log("Length of the text: " + length);


// Accessing characters
console.log("Accessing characters");
console.log("First character: " + text[0]);
console.log("Last character: " + text[length - 1]);
console.log("Character at index 2: " + text[2]);
console.log("Character at index 10: " + text[10]);
console.log("Character at index -1: " + text[length + 1]);

// Accessing substrings
console.log("Accessing substrings");
let substring = text.substring(2, 5);
console.log("Substring from index 2 to index 5: " + substring);
substring = text.substring(2);
console.log("Substring from index 2 to the end: " + substring);
substring = text.substring(0, length);
console.log("Substring from the beginning to the end: " + substring);

// Concatenation
console.log("Concatenation");
let concatenatedText = text + "123456789";
console.log("Concatenated text: " + concatenatedText);

// Repetition
console.log("Repetition");
let repeatedText = text + text;
console.log("Repeated text: " + repeatedText);

// Iterating over characters
console.log("Iterating over characters");
for (let i = 0; i < length; i++) {
  console.log("Character at index " + i + ": " + text[i]);
}

// Iterating over substrings
console.log("Iterating over substrings");
for (let i = 0; i < length; i++) {
  let substring = text.substring(i, i + 3);
  console.log("Substring from index " + i + " to index " + (i + 3) + ": " + substring);
}

// Converting to uppercase
console.log("Converting to uppercase");
let uppercaseText = text.toUpperCase();
console.log("Uppercase text: " + uppercaseText);

// Converting to lowercase
console.log("Converting to lowercase");
let lowercaseText = text.toLowerCase();
console.log("Lowercase text: " + lowercaseText);

// Replacing characters
console.log("Replacing characters");
let replacedText = text.replace("A", "X");
console.log("Replaced text: " + replacedText);

// Splitting a string
console.log("Splitting a string");
let splitText = text.split("");
console.log("Split text: " + splitText);

//String Interpolation method: Interpolate variables and expressions into strings
console.log("Interpolate between M and N the string: INTERPOLATED_TEXT");
let interpolateText = `${text.slice(0, text.indexOf('N'))} INTERPOLATED_TEXT ${text.slice(text.indexOf('N'))}`;
console.log("Interpolate text: " + interpolateText);

// Checking if a string is empty
console.log("Checking if a string is empty");
if (text.length === 0) {
  console.log("The text is empty");
} else {
  console.log("The text is not empty");
}

// Checking if a string contains a substring
console.log("Checking if a string contains a substring");
if (text.includes("A")) {
  console.log("The text contains the substring 'A'");
} else {
  console.log("The text does not contain the substring 'A'");
}

// Checking if a string starts with a substring
console.log("Checking if a string starts with a substring");
if (text.startsWith("A")) {
  console.log("The text starts with the substring 'A'");
} else {
  console.log("The text does not start with the substring 'A'");
}

// Checking if a string ends with a substring
console.log("Checking if a string ends with a substring");
if (text.endsWith("A")) {
  console.log("The text ends with the substring 'A'");
} else {
  console.log("The text does not end with the substring 'A'");
}

//  Checking if a string contains a sequence of characters
console.log("Checking if a string includes a sequence of characters");
if (text.includes("ABCDE")) {
  console.log("true");
} else {
  console.log("false");
}

console.log("Dificultad EXTRA");
/*DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos (se leen igual de izquierda a derecha y de derecha a izquierda)
 * - Anagramas (Las letras de una palabra, si se escriben en orden diferente, forman otra)
 * - Isogramas (Las letras se repiten el mismo número de veces)
 */

 
console.log("Reverse a string & check if it is a palindrome, anagram or isogram")
let word1 = "oso";
let word2 = "nana";

let reversedWord = word1.split("").reverse().join("");
console.log(`"${word1}" is a palindrome:`, word1 === reversedWord); // you can read the word in reverse
console.log(`"${word2}" is an anagram of "${word1}":`, word2 === reversedWord);// the letters of a word can form another word
console.log(`"${word1}" is an isogram:`, word1.length === new Set(word1).size); // it has no repeated characters


