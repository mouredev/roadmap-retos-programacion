/**
 * Reto de programación - #03 - JavaScript
 * Autor: Yoandy Doble Herrera
 * Fecha: 06/12/2024
 */

/** Ejercicio 1 */

//Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

/**
 * Función void
 */
function newUser() {
  //función clásica sin parámetros
  //cuerpo de la función
  console.log(`Roadmap #02 - JavaScript`)
}
newUser()

// Funciones anónimas

const funcJS = function (attr) {
  console.log(`¡Ejemplo de función anónima, ${attr}!`)
}

funcJS("codebydoble")

/**
 * Función void declarativa sin parámetros
 */
const newUser2 = () => {
  //cuerpo de la función
  console.log(`Esta función no retorna nada`)
}
newUser2()

/**
 * Función void anónima sin parámetros
 */
const sayHello = function () {
  console.log("Hello JavaScript, goodbye!")
}
sayHello()

/**
 * Función que recibe un parámetro string y modifica parámetros
 * @param {String} username
 */
const createTicket = (username) => {
  console.log("Welcome,", username + "!")
}
createTicket("Endry")

/**
 * Función con dos parámetros y retorno. Recibe dos números y devuelve la exponenciación
 * @param {number} numer1 Any number
 * @param {number} numero2 Any number
 * @returns Retorna la exponenciación del número
 */
const exponenteNumeros = (numero1, numero2) => {
  let resultado = 0 //Variable local
  resultado = numero1 ** numero2
  return resultado
}
let exponente = exponenteNumeros(3, 2)
console.log(exponente)

/** Ejercicio 2 funciones anidadas una dentro de otra*/
/**
 * Halla la raíz cuadrada de un número
 * @param {number} value Any number
 * @returns Retorna la raíz cuadrada de un número
 */
const elevarFunc = (value) => {
  return Math.sqrt(value)
}

/**
 * Multiplica la raíz cuadrada de números
 * @param {number} value1 Any number
 * @param {number} value2 Any number
 * @returns Retorna la multiplicación de la raíz cuadrada de dos números
 */
const multiplicarNumeros = (value1, value2) => {
  return elevarFunc(value1) * elevarFunc(value2)
}

console.log("La raíz cuadrada de dos números multiplicados es: ", multiplicarNumeros(8, 54))

//Funciones de orden superior
let estacionesAnio = ["Primavera", "Verano", "Otoño", "Invierno"]

const printSeasons = (arraySeason) => {
  for (let index = 0; index < arraySeason.length; index++) {
    console.log("Estación #" + (index + 1), arraySeason[index])
  }
}

function seasons(func, parametros) {
  func(parametros)
}

seasons(printSeasons, estacionesAnio)

/**Ejemplo función de javaScript Factorial recursividad*/
function factorial(n) {
  if (n === 0 || n === 1) return 1
  else return n * factorial(n - 1)
}

//Ejemplo variable local mostrará error su scope es local
/**
 * console.log(resultado)
 */
const piElemento = 3.14 //variable global
console.log(piElemento)

/**Ejercicio EXTRA */

/**
 * Función que recibe dos parámetros de tipo cadena de texto y retorne un número
 * @param {string} cadena1 Cualquier cadena de texto
 * @param {string} cadena2 Cualquier cadena de texto
 * @returns Retorna el número de veces que se ha impreso el número en lugar de los textos
 */
let multiplos = (cadena1, cadena2) => {
  let contador = 0
  for (let index = 0; index < 100; index++) {
    if ((index + 1) % 3 === 0 && (index + 1) % 5 === 0) {
      // multiplo de 3 y 5
      console.log(`El número ${index + 1} es ${cadena1} y  ${cadena2}`)
    } else if ((index + 1) % 3 === 0) {
      //multiplo de 3
      console.log(`El número ${index + 1} es ${cadena1}`)
    } else if ((index + 1) % 5 === 0) {
      //multiplo de 3
      console.log(`El número ${index + 1} es ${cadena2}`)
    } else {
      console.log("Numero: ", index + 1)
      contador++
    }
  }
  return contador
}

console.log("Se han mostrado los números: ", multiplos("Multiplo de 3", "Multiplo de 5"), "veces")
