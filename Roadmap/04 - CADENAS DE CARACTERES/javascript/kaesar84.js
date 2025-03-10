/*
# #04 CADENAS DE CARACTERES
> #### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio

```
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


#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
*/

// Strings

// Concatenación
let myName = "John Wick"
let greeting = "Hello " + myName
console.log(greeting)

// Longitud
console.log(myName.length)

// Acceso a un caracter
console.log(myName[0])

// Métodos comunes
console.log(myName.toUpperCase())
console.log(myName.toLowerCase())
console.log(myName.indexOf("Wick")) // donde encuentra la primera coincidencia -1 si no encuentra
console.log(myName.includes("Wick")) // true si la cadena contiene la cadena
console.log(myName.slice(0, 6)) // extrae una parte de la cadena
console.log(myName.replace("Wick", "Reaves")) // reemplaza una cadena por otra

// Templates literales
let despedida = "Adiós"
let message = `Hello ${myName} y estoy
haciendo cosas.
Hace los saltos de
línea.
${despedida}.`
console.log(message)

// * DIFICULTAD EXTRA (opcional):
//  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
//  * para descubrir si son:
//  * - Palíndromos
//  * - Anagramas
//  * - Isogramas

function isPalindrome(string1, string2) {
  let string1Lower = string1.toLowerCase()
  let string2Lower = string2.toLowerCase()

  if (string1Lower == string2Lower.split("").reverse().join("")) {
    return `*** SON PALINDROMOS`
  } else {
    return `!!! NO SON PALINDROMOS`
  }
}

function isAnagrame(string1, string2) {
  let string1Lower = string1.toLowerCase()
  let string2Lower = string2.toLowerCase()

  if (string1Lower.length == string2Lower.length) {
    let stringOrdenada1 = string1Lower.split("").sort().join("")
    let stringOrdenada2 = string2Lower.split("").sort().join("")
    if (stringOrdenada1 === stringOrdenada2) {
      return `*** SON ANAGRAMAS`
    } else {
      return `!!! NO SON ANAGRAMAS`
    }
  } else {
    return `!!! NO SON ANAGRAMAS`
  }
}

function isIsoagrame(string1, string2) {
  let string1Lower = string1.toLowerCase()
  let string2Lower = string2.toLowerCase()
  let charChecked = new Set()

  for (let i = 0; i < string1Lower.length; i++) {
    charChecked.add(string1Lower[i])
  } // console.log(charChecked)

  for (let i = 0; i < string2Lower.length; i++) {
    if (charChecked.has(string2Lower[i])) {
      return `!!! NO SON ISOGRAMAS.\nCarácteres compartidos >> ${Array.from(
        charChecked
      )}  ***`
    } else {
      charChecked.add(string2Lower[i])
      return `*** SON ISOGRAMAS,\nNo comparten ningún carácter. ***`
    } //console.log(charChecked)
  }
}

function checkWord(string1, string2) {
  console.log("\n===========================")
  console.log(`>> PALABRA 1: ${string1}`)
  console.log(`>> PALABRA 2: ${string2}`)
  console.log("===========================")
  console.log(isPalindrome(string1, string2))
  console.log(isAnagrame(string1, string2))
  console.log(isIsoagrame(string1, string2))
  console.log("===========================")
}
let wordOne = "Amor"
let wordTwo = "Roma"

checkWord(wordOne, wordTwo)

wordOne = "Spawn"
wordTwo = "Rio"

checkWord(wordOne, wordTwo)
