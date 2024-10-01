/*
funciones básicas en javascript 
*/

// Simple, funciones declaradas
function showName(){
  console.log("daniback")
}
showName()

// Retorno de valor
function add(){
  return 3 + 9
}
let result = add()
console.log(result)

// Parámetros y argumentos
function argGretting(name){
  console.log(`Hola, ${name}!`)
}
argGretting("Dani")

function argsGretting(text, name) {
  console.log(`${text}, ${name}!`)
}
argsGretting("Saludos", "Dani")

// Parámetro con valor predeterminado
function argSinDefaultGretting (lenguage){
  console.log(`Hola mundo desde ${lenguage}`)
}
argSinDefaultGretting()
function argDefaultGretting(lenguage = "JavaScript") {
  console.log(`Hola mundo desde ${lenguage}`)
}
argDefaultGretting()

// Con parámetros y retorno de valores
function grettCity(message, city){
  return `${message} ${city}`
}
let welcome = grettCity("Saludos desde", "Colombia")
console.log(welcome)

// varibles globales y locales
let user = "Juan" // Externa
function showUser() {
  let msj = `Que tal ${user}`
  console.log(msj)
}
showUser()

let user2 = "Sebastian"
function showUser2() {
  let user2 = "Mari" // local
  console.log("Mostrando user2 local =", user2)
}
showUser2()
console.log("Mostranso user2 global = ", user2)

function showUser3() {
  let myUser = "Dani"
  console.log(myUser, 'Esta dentro la función')
}
showUser3()
// console.log(myUser) no esta declarada como gloabal, not defined

// Funciones de expresion
const operation = function (num1, num2, oper) {
  switch (oper) {
    case "+":
      return num1 + num2
    case "-":
      return num1 - num2
    case "*":
      return num1 * num2
    case "/":
      return num1 / num2
    default:
      return 'Operador erróneo'
  }
} 

let resultOper = operation(3, 3, "*")
console.log("El resultado es", resultOper)

// Funciones flecha
let arrowFunction = (a, b) => a + b // return implícito
console.log(arrowFunction(3, 9))

let arrowFunctionMulti = (a, b, c) => {
  let total = a + b
  let iva = (total * c) / 100
  return iva // return explícito
}
let ivaCalc = arrowFunctionMulti(300, 270, 19)
console.log("IVA:", ivaCalc)

// funcion dentro de otra funcion
function createCounter() {
  let counter = 0;
  return function () {
    counter++
    return counter
  }
}
let counterOne = createCounter()
console.log(counterOne())
console.log(counterOne())

// funciones propias del lenguaje
console.log("Console.log() es una función propia del lenguaje")
let getRandom = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1) + min)
}
let numRam = getRandom(1, 10)
console.log(numRam)

let numLetters = (word) => {
  return word.length
}
function showNumLetters (w) {
  let num = numLetters(w)
  console.log(`La palabra ${w} tiene ${num} letras`)
}
showNumLetters("dani")

// DIFICULTAD EXTRA
function printNumbers (text1, text2) {
  let counter = 0
  for (let num = 1; num <= 100; num++){
    if (num % 3 === 0 && num % 5 === 0) {
      console.log(text1 + text2)
    } else if(num % 3 === 0) {
      console.log(text1)
    } else if (num % 5 === 0) {
      console.log(text2)
    } else {
      console.log(num)
      counter++
    }
  }
  return counter
}
console.log(printNumbers("fizz", "buzz"))