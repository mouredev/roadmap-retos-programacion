/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#16 EXPRESIONES REGULARES
---------------------------------------
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
*/
// ________________________________________________________

function toNumbers(text) {
    const numberPattern = /\d+/g;
    return text.match(numberPattern) || [];
}

const string = "abcdsfs1s(*&#}2. a3// 45sdf67";
const listNumbers = toNumbers(string);
console.log(listNumbers); // ['1', '2', '3', '45', '67']

// ________________________________________________________
// DIFICULTAD EXTRA

function isEmail(text) {
    const pattern = /^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$/;
    return pattern.test(text);
}

function isPhoneNumber(text) {
    const pattern = /^(\d{3}-\d{3}-\d{4}|\d{10})$/;
    return pattern.test(text);
}

function isUrl(text) {
    const pattern = /^(https?:\/\/)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/\S*)?$/;
    return pattern.test(text);
}

// Pruebas
console.log("\nisEmail");
console.log(isEmail("ejm@dmn.com"));        // true
console.log(isEmail("e_jm-2+b@dmn.co.hn")); // true
console.log(isEmail("ejm@dmn.com_"));       // false
console.log(isEmail("ejm@dmn"));            // false

console.log("\nisPhoneNumber");
console.log(isPhoneNumber("123-456-7890")); // true
console.log(isPhoneNumber("1234567890"));   // true
console.log(isPhoneNumber("123456-7890"));  // false
console.log(isPhoneNumber("uno234567890")); // false

console.log("\nisUrl");
console.log(isUrl("http://www.ejm.com"));   // true
console.log(isUrl("google.com"));           // true
console.log(isUrl("ejm.com/a/b/c"));        // true
console.log(isUrl("https://.ejm.com"));     // false
console.log(isUrl("https://.ejm.com/a b")); // false
