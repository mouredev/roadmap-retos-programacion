// Acceso a caracteres específicos
let string = 'Hello World!';
let char = string[1]; // 'e'

// Subcadenas
let substring = string.substring(0, 5); // 'Hello'

// Longitud
let length = string.length; // 12

// Concatenación
let concatenated = string + ' How are you?'; // 'Hello World! How are you?'

// Repetición
let repeated = string.repeat(3); // 'Hello World!Hello World!Hello World!'

// Recorrido
for (let i = 0; i < string.length; i++) {
    console.log(string[i]);
}

// Conversión a mayúsculas
let upper = string.toUpperCase(); // 'HELLO WORLD!'

// Conversión a minúsculas
let lower = string.toLowerCase(); // 'hello world!'

// Reemplazo
let replaced = string.replace('World', 'Everyone'); // 'Hello Everyone!'

// División
let split = string.split(' '); // ['Hello', 'World!']

// Unión
let joined = split.join(', '); // 'Hello, World!'

// Interpolación
let name = 'Alice';
let interpolated = `Hello, ${name}!`; // 'Hello, Alice!'

// Verificación (includes)
let contains = string.includes('World'); // true



// Ejercicio:
function isPalindrome(word) {
    return word === word.split('').reverse().join('');
}

function isAnagram(word1, word2) {
    let normalize = (str) => str.toLowerCase().split('').sort().join('');
    return normalize(word1) === normalize(word2);
}

function isIsogram(word) {
    let letters = word.toLowerCase().split('').sort();
    for (let i = 1; i < letters.length; i++) {
        if (letters[i] === letters[i - 1]) {
            return false;
        }
    }
    return true;
}

// Use the functions
let word1 = 'listen';
let word2 = 'silent';

console.log(`Is "${word1}" a palindrome?`, isPalindrome(word1));
console.log(`Is "${word2}" a palindrome?`, isPalindrome(word2));
console.log(`Are "${word1}" and "${word2}" anagrams?`, isAnagram(word1, word2));
console.log(`Is "${word1}" an isogram?`, isIsogram(word1));
console.log(`Is "${word2}" an isogram?`, isIsogram(word2));