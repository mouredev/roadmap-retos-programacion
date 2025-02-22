/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 */

// Concatenacion
let myName = 'Jose'
console.log ('Hola ' + myName  + ' Buenas noches')

// Acceso a Caracteres especificos
console.log (myName.indexOf('e')) // para indentificar en indice del caracter
console.log (myName[3]) // para mostrar el caracter
console.log (myName.charAt(3)) // para mostrar el caracter

// Subcadenas
console.log (myName.includes('se')) // para saber si incluye la subcadena
console.log (myName.indexOf('se')) // en que indice empieza
console.log(myName.slice(2,4)) // se indica donde empieza, y donde termnina
console.log(myName.substring(2,4)) // se indica donde empieza, y donde termnina

// Longitud
console.log (myName.length) // para saber la longitud de la cadena

// Repeticion
console.log (myName.repeat(2)) // indica cuantas veces se repite

// Recorrido
for (i = 0; i < myName.length; i++) {
    console.log (myName.charAt(i))
}

// Conversión a mayúsculas y minúsculas
console.log(myName.toUpperCase()) // Covierte en mayusculas
console.log(myName.toLowerCase()) // Convierte en minisculas

// Reemplazo
console.log (myName.replace('se', '  si lo reemplaza')) // reemplaza una cadena por otra

// División
let phrase = "Hola Jose Buenas noches"
let words = phrase.split(' ') // divide la cadena en un array de palabras y devuelve un array
console.log(words)

// Unión
let joinedPhrase = words.join(' ') // une el array de palabras en una cadena
console.log(joinedPhrase)

// Interpolación
let greeting = `Hola ${myName}, ¿cómo estás?` // usa template literals para interpolar variables
console.log(greeting)

// Verificación
console.log(myName.startsWith('Jo')) // verifica si la cadena empieza con 'Jo'
console.log(myName.endsWith('se')) // verifica si la cadena termina con 'se'
console.log(myName.includes('os')) // verifica si la cadena incluye 'os'

// * DIFICULTAD EXTRA (opcional):
// * Crea un programa que analice dos palabras diferentes y realice comprobaciones
// * para descubrir si son:
// * - Palíndromos
// * - Anagramas
// * - Isogramas

let word = 'amor22'
let word2 = 'roma'

function checkPalindromo(word1, word2) {
    const reverseWord = word1.split ('').reverse().join('')
    let result = reverseWord === word2 ? 'Son un palindromo': 'No son un palidromo'
    console.log (`${word1} y ${word2} ${result}`)
};
checkPalindromo (word, word2);

const checkAnagrama = (word1, word2) => {
    const check = (str) => {
        return str.split('').sort().join("");
    }
    let result = check (word1) === check (word2) ? 'Son un anagrama': 'No son un anagrama'
    console.log (`${word1} y ${word2} ${result}`)
}

checkAnagrama (word,word2);

const checkIsogramas = (word1, word2) => {
    const check = (str) => {
        let setWord = new Set (str)
        return new Array (...setWord).join('')
    } 
    let result = check (word1) === word1 ? 'Es un Isograma': 'No es un Isograma'
    return console.log (`${word1} ${result}`)
}

checkIsogramas (word, word2);