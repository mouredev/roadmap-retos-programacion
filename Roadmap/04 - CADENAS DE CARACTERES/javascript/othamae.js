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

let string = 'Hello from JavaScript!'
console.log(`This is the string: ${string}`)

// Character access 
const char = string[4]
const char2 = string.charAt(4)
console.log(`Character on index 4 using string[4]: ${char}`)
console.log(`Character on index 4 using string.charAt(4): ${char2}`)

// Length
const stringLength = string.length
console.log(`String length: ${stringLength}`)

// Substring
const substring = string.substring(11, 21)
console.log(`Substring from index 11 to 20: ${substring}`)

const slice = string.slice(11, 21)
console.log(`Slice from index 11 to 20: ${slice}`)

// Concatenation
const contat = string + ' and Node.js!'
console.log(`Concatenation: ${contat}`)

// Repetition
const repetition = string.repeat(3)
console.log(`Repetition x3: ${repetition}`)

// Traversal
console.log('Traversal:')
for (const char of string) {
  console.log(char)
}

// Conversion
const upper = string.toUpperCase()
const lower = string.toLowerCase()
console.log(`Uppercase: ${upper}`)
console.log(`Lowercase: ${lower}`)

// Replacement
const replaced = string.replace('JavaScript', 'TypeScript')
console.log(`Replaced: ${replaced}`)

const replaceAll = string.replaceAll('o', 'u')
console.log(`Replaced all: ${replaceAll}`)

// Division
const divided = string.split(' ')
console.log(`Divided by ' ': ${divided}`)

// Union
const joined = divided.join(' ')
console.log(`Joined by ' ': ${joined}`)

// Interpolation
const interpolation = `Interpolation: ${string}`
console.log(interpolation)

// Verification
const contains = string.includes('JavaScript')
console.log(`Contains 'JavaScript': ${contains}`)


// EXTRA TASK:

function isPalindrome(string) {
    return string === string.split('').reverse().join('')
}

function isAnagram(string1, string2) {
    const sorted1 = string1.toLowerCase().split('').sort().join('')
    const sorted2 = string2.toLowerCase().split('').sort().join('')
    return sorted1 === sorted2
}

function isIsogram(string) {
    const letters = string.toLowerCase().split('')
    const dic = {}
    for (const letter of letters) {       
        if (dic[letter]) dic[letter]++ 
        else dic[letter] = 1
    }
    const frecuencies = Object.values(dic)
    return frecuencies.every(frec => frec === frecuencies[0]);
}

const word1 = 'reconocer'
const word2 = 'debit card' 
const word3 = 'bad credit'
const word4 = 'redder'

console.log(`Is the word '${word1}' Palindrome? ${isPalindrome(word1)}`)
console.log(`Are the words '${word2}' and '${word3}' Anagrams? ${isAnagram(word2, word3)}`)
console.log(`Is the word '${word4}' Isogram? ${isIsogram(word4)}`)


