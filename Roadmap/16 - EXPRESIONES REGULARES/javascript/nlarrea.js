/*
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

const text = `
Lorem ipsum dolor1 sit amet, consectetur adipiscing elit. Nullam ac mi in
ipsum ultricies 2 varius. Nullam euismod, justo nec fermentum ultricies, nunc
nisl tempus purus, 3 sed dictum 563 nulla odio nec purus. Nullam nec purus
consectetur, consectetur justo. 10 Nullam nec purus consectetur, consectetur.
`

const numbersPattern = /[\d]{1,}/g;
const numbers = text.match(numbersPattern);
console.log(numbers);
// ['1', '2', '3', '563', '10']


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */


function printTest(pattern, text) {
    console.log(text + ':', text.match(pattern)?.length > 0);
}


console.log('\nTesting emails:');
const emailPattern = /^[\w]{1,}[\w\d\._]{4,}\@[\w]{2,}\.[\w]{2,3}$/g;
printTest(emailPattern, 'an_email@gmail.com');  // true
printTest(emailPattern, '1234@email.com');  // false
printTest(emailPattern, 'an_email1234');  // false
printTest(emailPattern, 'an2_email4@gmail.com');  // true
printTest(emailPattern, 'another.2024@gmail');  // false
printTest(emailPattern, 'another.2024@gmail.');  // false
printTest(emailPattern, 'another.2024@gmail.com');  // true

console.log('\nTesting phone numbers:');
const phonePattern = /^\+?\d{3,}$/g;
printTest(phonePattern, '123456789');  // true
printTest(phonePattern, '+34123456789');  // true
printTest(phonePattern, 'abcdefghi');  // false

console.log('\nTesting URLs:');
const urlPattern = /^https?:\/\/(w{3}\.)?[\w\d\.\-\?]+\.[\w]{2,}\/?$/g
printTest(urlPattern, 'https://github.com/');  // true
printTest(urlPattern, 'https://www.twitch.tv/');  // true