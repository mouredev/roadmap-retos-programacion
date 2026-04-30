/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */
let myName = "Bryanorx"
let age = 30

//Concatenación
console.log("Hola soy "+myName+" y tengo "+age+" años")

//Interpolación
let message = `Hola soy ${myName} y tengo ${age} años`
console.log(message)

//Longitud
console.log(message.length)

//Acceso a caracteres
console.log(message[9])
console.log(message[26])

//Métodos
//Convertir cadena a mayúscula
console.log(message.toUpperCase())

//Convertir cadena a minúscula
console.log(message.toLowerCase())

//Encontrar el índice
console.log(message.indexOf("Hola"))
console.log(message.indexOf("Bryan"))
console.log(message.indexOf("años"))

//Verificar si incluye
console.log(message.includes("Hola"))
console.log(message.includes("Bryan"))
console.log(message.includes("30"))

//Devuelve una copia de una parte de la cadena en un array
console.log(message.slice(0,10))

//Reemplazar dentro de la cadena
console.log(message.replace("Hola", "Hi"))

//Separa la cadena en un array
let text = "Juan Perez se fue de viaje"
console.log(text.split(" "))

//Elimina espacios en blanco
let phrase = "    Hola, amigoos   "
console.log(phrase.trim())

//Repita una cadena
let text2 = "Holaa"
console.log(text2.repeat(3))

//Recorrer cadena en un bucle
for (let i of text2) {
    console.log(i)
}

//Verifica si la cadena inicia con un caracter o cadena específica
console.log(text.startsWith("Juan"))
console.log(text.startsWith("juan"))

//Verifica si la cadena termina con un caracter o cadena específica
console.log(text.endsWith("viaje"))
console.log(text.endsWith("Viaje"))

//Rellena la cadena desde el inicio con otra cadena o caracter alcanzando una longitud
console.log(text.padStart(28,"-"))

//Rellena la cadena desde el final con otra cadena o caracter alcanzando una longitud
console.log(text.padEnd(28, "*"))

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

let phrase1 = "Anita lava la tina"
let phrase2 = "Reconocer"
let palindrome1 = phrase1.toLocaleLowerCase().replaceAll(" ","").split("").reverse().join("")
let palindrome2 = phrase2.toLocaleLowerCase().replaceAll(" ","").split("").reverse().join("")

if (phrase1.toLocaleLowerCase().replaceAll(" ","") === palindrome1) {
    console.log(`${phrase1} es palíndroma`)
} else {
    console.log(`${phrase1} no es palíndroma`)
}
if (phrase2.toLocaleLowerCase().replaceAll(" ","") === palindrome2) {
    console.log(`${phrase2} es palíndroma`)
} else {
    console.log(`${phrase2} no es palíndroma`)
}

let phrase3 = "Amor"
let phrase4 = "Roma"

if (phrase3.toLocaleLowerCase().split("").sort().toString() === phrase4.toLocaleLowerCase().split("").sort().toString()) {
    console.log(`Las palabras ${phrase3} y ${phrase4} son anagramas`)
} else {
    console.log(`Las palabras ${phrase3} y ${phrase4} no son anagramas`)
}

let phrase5 = "Letra"
let times = {}
for (let i of phrase5.toLocaleLowerCase()) {
    times[i] = (times[i] || 0)+1
}

let isograma = true
for (let i in times) {
    if (times[i] > 1) {
        isograma = false
        break
    }
}
console.log(`${phrase5} es isograma: ${isograma}`)