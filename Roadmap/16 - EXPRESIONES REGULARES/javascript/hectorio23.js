// Author: Héctor Adán 
// GitHub: https://github.com/hectorio23
"use strict";


// Zona de REGEX Patterns
const emailRegex = /\w+@[a-z]+\.[a-z]{3}$/g;
const phoneNumberRegex = /^(\+\d{2,3})\s(\d{3})\s(\d{3})\s(\d{2})\s(\d{2})/g;
const urlRegex = /^https?:\/\/([a-zA-Z0-9]*\.)?[a-zA-Z0-9]*\.([a-zA-Z]{3})(\.[a-zA-Z]{2,3})?\/?/;

// texto al cual se le quitaran los numeros apra hacerlo
// legible
let texto_legible = "E5n e6l si5g7ui8e956nte tex8to s9e 0t4ien4e que3 extr3aer to3dos lo0s nume3ro0s pa2ra q4ue s8e7a l9e0gi9b0le"

//////////////////////////
////// EJERCICIO 1 ///////
//////////////////////////

console.log("EJERCICIO");
console.log(`Cadena Original: ${ texto_legible }`)
console.log(`Cadena aplicando la REGEX: ${ texto_legible.replace(/[0-9]+/g, "") }`)

console.log("\n********* EJERCICIO EXTRA **********");
console.log("********* EMAIL CHECKER **********");
console.log(`[ hectorino2789@gmail.com ] es un email? ${ emailRegex.test("hectorino2789@gmail.com") }`);
console.log(`[ quesobadas@outlook.es ] es un email? ${ emailRegex.test("quesobadas@outlook.es") }`);
console.log(`[ nocorresponde a unema%il@gmaildjfj.completo ] es un email? ${ emailRegex.test("nocorresponde a unema%il@gmaildjfj.completo") }`);

console.log("\n********* PHONE NUMBER CHECKER **********");
console.log(`[ +52 449-369-52-34 ] es un número de teléfono? ${ phoneNumberRegex.test("+52 449-369-52-34") }`);
console.log(`[ +52 449 369 52 34 ] es un número de teléfono? ${ phoneNumberRegex.test("+52 449 369 52 34") }`);
console.log(`[ 449 369 52 34 ] es un número de teléfono? ${ phoneNumberRegex.test("449 369 52 34") }`);

console.log("\n********* URL CHECKER **********");
console.log(`[ https://github.com/hectorio23 ] es una URL? ${ urlRegex.test("https://github.com/hectorio23") }`);
console.log(`[ outlook:///github.com\hectorio23 ] es una URL? ${ urlRegex.test("outlook:///github.com\hectorio23") }`);
console.log(`[ 127.0.0.1:89/path/otherpath ] es una URL? ${ urlRegex.test("127.0.0.1:89/path/otherpath") }`);
console.log(`[ https://apple.com ] es una URL? ${ urlRegex.test("https://apple.com") }`);
