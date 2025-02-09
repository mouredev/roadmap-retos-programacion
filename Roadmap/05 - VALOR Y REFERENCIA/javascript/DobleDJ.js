/** #05 - javaScript VALOR Y REFERENCIA
 * Date: 03/01/2025
 * Author: Yoandy Doble Herrera
 */

/*
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia" según su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas. (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
*/

/* Asignación por valor */
let usuario = "codebydoble"
const distancia = 10000
let userCopy = "@" + usuario

console.log(usuario)
console.log(distancia)
console.log(userCopy)

/* Asignación de variables por referencia */

const librosTech = ["De 0 a Experto", "Github ++", "100 Horas de código", "Javascript Eloquent"]
const personalBook = librosTech

librosTech.push("Mouredev la guía definitiva") // se actualiza en ambos array
console.log(librosTech)
console.log(personalBook)

/* Funciones con valores primitivos */

/**
 * Simula un juego
 * @param {number} participantes Númeto total de participantes en el juego
 * @returns Retorna la cantidad de participantes
 */
const game = (participantes) => {
  participantes = 100
  return `El juego cuenta con: ${participantes} atletas`
}

let atletas = 200
console.log(game(atletas)) //Le juego cuenta con 100 atletas
console.log(atletas) //200

/* Funciones con valores no primitivos */

/**
 * Lista de series de TV
 * @param {Array} arr Array lista de series de TV
 * @returns Retorna la lista de series televisivas
 */
const seriesTV = (arr) => {
  const arrCopy = [...arr]
  const results = []
  for (let index = 0; index < arrCopy.length; index++) {
    results.push(arrCopy.shift())
  }
  return results
}
const misSeries = ["X Files", "24 Hours", "La que se avecina", "Bleach", "Big Bang Theory"]
seriesTV(misSeries)
console.log(misSeries) // ["X Files", "24 Hours", "La que se avecina", "Bleach", "Big Bang Theory"]

/* DIFICULTAD EXTRA */
/**
 * DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
*/

// Función con dos parámetros por valor
/**
 * Intercambia dos valores
 * @param {number} paramOne Any number
 * @param {number} paramTwo Any number
 * @returns Retorna un array con los valores intercambiados
 */
function programOne(paramOne, paramTwo) {
  let temp = paramOne
  paramOne = paramTwo
  paramTwo = temp
  return [paramOne, paramTwo]
}

let paramOne = 10
let paramTwo = 20

let switchOne
let switchTwo
;[switchOne, switchTwo] = programOne(paramOne, paramTwo)

console.log(`Parámetros iniciales: Primer valor ${paramOne}, Segundo Valor ${paramTwo}`)

console.log(`Parámetros intercambiados: Primer valor ${switchOne}, Segundo Valor ${switchTwo}`)

// Función con dos parámetros por referencia
function programTwo(arrOne, arrTwo) {
  const temp = arrOne
  arrOne = arrTwo
  arrTwo = temp
  return { arrOne, arrTwo }
}

const laptop = ["Apple", "Dell", "HP", "Lenovo", "Asus"]
const phone = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Huawei"]

let { arrOne: firstArr, arrTwo: secondArr } = programTwo(laptop, phone)
console.log(`Parámetros iniciales -> uno: ${laptop}, dos: ${phone}`)
console.log(`Parámetros Intercambiados -> uno: ${firstArr}, dos: ${secondArr}`)
