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

// CREATE A STRING

const myString: string = 'Hello world!';

// ACCESS CHARACTERS

console.log(myString[6]);  // w
const firstWord: string = myString.slice(0, 5);
console.log(firstWord);  // Hello

// Separate the string in each space and take the second item from the list
const secondWord: string = myString.split(' ')[1]
console.log(secondWord);  // world!

// LENGTH

console.log(myString.length);  // 12
console.log(firstWord.length);  // 5
console.log(secondWord.length);  // 6

// INTERPOLATION AND CONCATENATION

let sentence: string = `${firstWord} ${secondWord}`;
console.log(sentence);  // Hello world!

sentence = firstWord + ' ' + secondWord;
console.log(sentence);  // Hello world!

sentence = firstWord.concat(secondWord);
console.log(sentence);  // Helloworld!

// REPETITION

console.log(firstWord.repeat(2));  // HelloHello

// CHECK

console.log(myString.includes('h'));  // false
console.log(myString.includes('H'));  // true
console.log(myString.includes('world'));  // true
console.log(myString.startsWith('Hell'));  // true
console.log(myString.endsWith('!'));  // true

// REPLACE

console.log(myString.replace('!', '.'));  // Hello world.

// DIVISION

console.log(myString.split(' '));  // [ 'Hello', 'world!' ]

// UPPER AND LOWER CASES

console.log(myString.toUpperCase());  // HELLO WORLD
console.log(myString.toLowerCase());  // hello world

// REMOVE EMPTY SPACES FROM BEGINNING AND END

const myOtherString: string = '    Hello there!   '

console.log(myOtherString.length);  // 19
console.log(myOtherString.trim().length);  // 12
console.log(myOtherString.trimEnd().length);    // 16
console.log(myOtherString.trimStart().length);  // 15

// FIND

const longString: string = 'the quick brown fox jumped over the lazy dog'

console.log(longString.search('quick'));  // 4 -> index of the start of the word
console.log(longString.search('QUICK'));  // -1 -> doesn't exist

// FROM NUMERIC STRING TO NUMBER

const stringNumber: string = '1234';
const intNumber: number = +stringNumber;
const intNumber2: number = parseInt(stringNumber);
console.log(typeof stringNumber);   // string
console.log(typeof intNumber);      // number
console.log(typeof intNumber2);     // number

const stringNumber2: string = '1234.56';
const floatNumber: number = +stringNumber2;
const floatNumber2: number = parseFloat(stringNumber2);
console.log(typeof stringNumber2);  // string
console.log(typeof floatNumber);    // number
console.log(typeof floatNumber2);   // number


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


function checkIsPalindrome(word: string): boolean {
    const reversedWord: string = [...word].reverse().join('');
    return word === reversedWord;
}


function checkIsAnagram(wordOne: string, wordTwo: string): boolean {
    return [...wordOne].sort().join('') === [...wordTwo].sort().join('');
}


function checkIsIsogram(word: string): boolean {
    // Store how many times appears each character
    const charsObj = {};
    for (const char of word) {
        charsObj[char] = charsObj[char] + 1 || 1;
    }

    // Check if all the characters repeat the same amount of times
    const charsValues: number[] = Object.values(charsObj);
    const firstCharQty: number = charsValues[0];
    for (const charQty of charsValues) {
        if (charQty !== firstCharQty) {
            return false;
        }
    }

    return true;
}


function checkWords (wordOne: string, wordTwo: string): void {
    // Check if they are palindromes
    console.log(`\nIs ${wordOne} a palindrome? ${checkIsPalindrome(wordOne)}`);
    console.log(`Is ${wordTwo} a palindrome? ${checkIsPalindrome(wordTwo)}`);

    // Check if they are anagrams
    console.log(`\nIs ${wordOne} ${wordTwo}'s anagram? ${checkIsAnagram(wordOne, wordTwo)}`);

    // Check if they are isograms
    console.log(`\nIs ${wordOne} an isogram? ${checkIsIsogram(wordOne)}`);
    console.log(`Is ${wordTwo} an isogram? ${checkIsIsogram(wordTwo)}\n`);
}


checkWords('rotor', 'anna');
checkWords('amor', 'roma');