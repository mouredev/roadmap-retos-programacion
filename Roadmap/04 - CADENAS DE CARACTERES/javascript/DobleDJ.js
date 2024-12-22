/**
 * Reto de programación #04 - javaScript
 * Autor: Yoandy Doble Herrera
 * Fecha: 15/12/2024
 */

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

let cadenaTexto = "Esta es una cadena de texto. "
let otraCadena = `Esta es una cadena de texto literal. By codebydoble`

/* Búsqueda */
const mensajeTry = "Utilizaré este ejemplo para el Roadmap."

console.log("Buscar con includes en la cadena return un boolean: ", mensajeTry.includes("este")) // true
console.log("Buscar con indexOF en la cadena return un boolean: ", mensajeTry.indexOf("ejemplo")) // 15
console.log("Buscar con indexOF en la cadena return un boolean: ", mensajeTry.indexOf("javascript")) // -1
console.log("Buscar con endWith en la cadena return un boolean: ", otraCadena.endsWith("doble"))
console.log("Buscar con starWith en la cadena return un boolean: ", cadenaTexto.startsWith("doble"))
console.log("Buscar con includes en la cadena return un boolean: ", cadenaTexto.includes("una"))

/* Interpolación  */
let nombre = "Yoandy"
let oracion = `Este reto de programacion es realizado por: ${nombre} \n`

/* Acceso a elementos */
console.log("Acceso a elemento por index -chartAt-: ", otraCadena.charAt(3), "\n")
console.log("Acceso a elemento por index: ", cadenaTexto[1], "\n")
console.log("Acceso a elemento por index devuelve Code: ", cadenaTexto.charCodeAt(5), "\n")

/* Subcadena */
let subcadenaTexto = cadenaTexto.split(" ")
console.log("Subcadenas de texto: ", subcadenaTexto, "\n")

let sliceText = cadenaTexto.slice(3, 10)
console.log("Slice texto: ", sliceText, "\n")

let tinyText = cadenaTexto.match("es una")
console.log("Subcadenas de texto: ", tinyText, "\n")

/* Longitud */
console.log("Longitud de la cadena: ", otraCadena.length, "\n")

/* Concatenación */
let paragraph = cadenaTexto.concat(otraCadena)
console.log("Concatenación de string -concat-: ", paragraph, "\n")

/* Unión */
let otraConcatenacion = cadenaTexto + otraCadena
console.log("Concatenación de string: ", otraConcatenacion, "\n")

let unJoin = ""
unJoin += cadenaTexto
unJoin += otraCadena
console.log("Join de string: ", unJoin, "\n")

/* repetición */
let textoRepetido = cadenaTexto.repeat(2)
console.log("Cadena repetida 2 veces: ", textoRepetido, "\n")

/* conversión a mayúsculas y minúsculas */
console.log("Conversión a mayúsculas: ", cadenaTexto.toUpperCase(), "\n")

console.log("Conversión a minúsculas: ", cadenaTexto.toLowerCase(), "\n")

/* Reemplazo */
let textoSimple = "javaScript es un lenguaje de programación. Retos de programación by mouredev"
let replaceText = textoSimple.replace("by", "por")
let replaceTextAll = textoSimple.replaceAll("a", "@")

console.log("Texto original: ", textoSimple, "\n")

console.log("Texto de reemplazo: ", replaceText, "\n")

console.log("Texto de reemplazo todos los resultados: ", replaceTextAll, "\n")

/* recorrido */
let message = "Este es un mensaje en un string"

for (let index = 0; index < message.length; index++) {
  console.log(message[index])
}

/* DIFICULTAD EXTRA (opcional):
 Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
 - [] Palíndromos
 - [] Anagramas
 - [] Isogramas
*/

/**
 * Reverse a string
 * @param {string} word Any string word with symbols, spaces and string
 * @returns Returns reversed string word
 */
const reverseManual = (word) => word.split("").reverse().join("")

/**
 * Determine if two words are palindromes, anagram or isogram
 * @param {string} firstWord Any string word
 * @param {string} secondWord Any string word
 * @returns Returns a boolean response true or false
 */
function textAnalizer(firstWord, secondWord) {
  //TODO
  if (palindromeTester(firstWord, secondWord)) console.log("Las palabras son palíndromes")

  const resultAnagram = anagramaTester(firstWord, secondWord)
  const resultIsogram = isogramaTester(firstWord, secondWord)
}

/**
 * Determine if two words are palindromes
 * @param {string} firstWord Any string word
 * @param {string} secondWord Any string word
 * @returns Returns a boolean response true or false
 */
const palindromeTester = (firstWord, secondWord) => {
  //TODO reversed secondWord check firstWord
  return firstWord.toLowerCase() === reverseManual(secondWord).toLowerCase()
}

/**
 * Determine if two words are anagram
 * @param {string} firstWord Any string word
 * @param {string} secondWord Any string word
 * @returns Returns a boolean response true or false
 */
const anagramaTester = (firstWord, secondWord) => {}

/**
 * Determine if two words are isogram
 * @param {string} firstWord Any string word
 * @param {string} secondWord Any string word
 * @returns Returns a boolean response true or false
 */
const isogramaTester = (firstWord, secondWord) => {}
