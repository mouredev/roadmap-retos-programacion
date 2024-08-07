// #04 CADENAS DE CARACTERES

/**
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 */
const hello = 'Hello';
const world = 'World';
const javascript = ', JavaScript!';
let hola = 'Hola';
const five = 5;
console.log(five.toString()); // -> '5'
// .length: Longitud de la cadena
console.log(hello.length); // -> 5
console.log(world.length); // -> 5
console.log(hola.length); // -> 4
// concatenacion(+)(.concat) e interpolacion(Template Literals ` `)
const concat = 'Hello' + ',' + ' ' + 'World!';
const interp = `${hello}, ${world}!`;
console.log((hola += javascript)); // -> 'Hola, JavaScript!'
console.log(concat); // -> 'Hello, World!'
console.log(hello, world); // -> 'Hello World'
console.log(hello.concat(javascript)); // -> 'Hello, JavaScript!'
console.log(interp); // -> 'Hello, World!'
console.log(concat.length); // -> 13
console.log(interp.length); // -> 13
console.log(hola.length); // -> 17
// acceder a un caracter
console.log('Hello'.charAt(0)); // -> 'H'
console.log('Hello'[-1]); // -> undefined
console.log('Hello'[1]); // -> 'e'
console.log('Hello'.charAt(4)); // -> 'o'
console.log('Hello'.charAt(5)); // -> ''
// verificar y busqueda
console.log('Hello'.startsWith('H')); // -> true
console.log('Hello'.startsWith('h')); // -> false
console.log('Hello'.endsWith('o')); // -> true
console.log('Hello'.endsWith('O')); // -> false

console.log('Javascript'.includes('s')); // -> true
console.log('Javascript'.includes('S')); // -> false

console.log('welcome'.indexOf('e')); // -> 1
console.log('welcome'.lastIndexOf('e')); // -> 6
// repetir
console.log('Hello'.repeat(3)); // -> 'HelloHelloHello'
console.log('Hello'.repeat(0)); // -> ''
// reemplazar
console.log('Hekko'.replace('k', 'l')); // -> 'Helko'
console.log('Hekko'.replaceAll('k', 'l')); // -> 'Hello'
// Mayúsculas y minúsculas
console.log('Hello'.toUpperCase()); // -> 'HELLO'
console.log('Hello'.toLowerCase()); // -> 'hello'
// Division y subcadenas
console.log('Dos mil veinticuatro'.split(' ')); // -> ['Dos', 'mil', 'veinticuatro']
console.log('DOS'.split('')); // -> ['D', 'O', 'S']
console.log('DOS'.split('', 1)); // -> ['D']
console.log('Dos mil veinticuatro'.slice(0, 3)); // -> 'Dos'
console.log('Dos mil veinticuatro'.slice(-12)); // -> 'veinticuatro'
console.log('Dos mil veinticuatro'.substring(0, 3)); // -> 'Dos'
// Mayusculas y minusculas
console.log('Hello'.toUpperCase()); // -> 'HELLO'
console.log('HELLO'.toLowerCase()); // -> 'hello'
// trim eliminación de espacios (inicio y final)
console.log('    Hello World!     '.trim()); // -> 'Hello World!'
console.log('    Hello World!     '.trimStart()); // -> 'Hello World!     '
console.log('    Hello World!     '.trimEnd()); // -> '    Hello World!'
// rellenar
console.log('Hello'.padStart(10, '*')); // -> '****Hello'
console.log('Hello'.padEnd(10, '*')); // -> 'Hello****'

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

function main(firstWord, secondWord) {
	if (
		typeof firstWord !== 'string' ||
		typeof secondWord !== 'string' ||
		firstWord === '' ||
		secondWord === ''
	) {
		return console.log('Please enter a valid word');
	}
	palindrome(firstWord, secondWord);

	anagram(firstWord, secondWord);

	isogram(firstWord, secondWord);
}

function palindrome(firstWord, secondWord) {
	const first = firstWord.toLowerCase();
	const second = secondWord.toLowerCase();
	first === first.split('').reverse().join('')
		? console.log(`${firstWord} is Palindrome`)
		: console.log(`${firstWord} is not Palindrome`);

	second === second.split('').reverse().join('')
		? console.log(`${secondWord} is Palindrome`)
		: console.log(`${secondWord} is not Palindrome`);
}

function anagram(firstWord, secondWord) {
	const first = firstWord.toLowerCase();
	const second = secondWord.toLowerCase();
	const firstSorted = first.split('').sort().join('');
	const secondSorted = second.split('').sort().join('');
	firstSorted === secondSorted
		? console.log(`The words ${firstWord} and ${secondWord} are anagrams`)
		: console.log(`The words ${firstWord} and ${secondWord} are not anagrams`);
}

function isogram(firstWord, secondWord) {
	const first = firstWord.toLowerCase();
	const second = secondWord.toLowerCase();
	const firstSet = new Set(first);
	const secondSet = new Set(second);

	firstSet.size === first.length
		? console.log(`The word ${firstWord} is a First-order Isogram`)
		: console.log(`The word ${firstWord} is not a First-order Isogram`);

	secondSet.size === second.length
		? console.log(`The word ${secondWord} is a First-order Isogram`)
		: console.log(`The word ${secondWord} is not a First-order Isogram`);
}

main('string', 'number');
main('evil', 'live');
main('level', 'noon');
