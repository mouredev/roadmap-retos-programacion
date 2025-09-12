/**
 * Retos de programación - 01 -
 * Autor: Yoandy Doble Herrera
 * Fecha: 05/12/2024
 */

/**
 * Ejercicio 1 tipos de operadores
 */

let numeroUno = 25.6
let numeroDos = 8

//Operadores aritméticos
let suma = numeroUno + numeroDos //operador suma
console.log(suma)
let resta = numeroUno - numeroDos //operador resta
console.log(resta)
let multiplicacion = numeroUno * numeroDos //operador multiplicación
console.log(multiplicacion)
let division = numeroUno / numeroDos //operador division
console.log(division)
let resto = numeroUno % numeroUno //operador resto
console.log(resto)
let exponenciacion = 2 ** 3 //operador exponenciación
console.log(exponenciacion)
let incremento = numeroDos //8
incremento++ //operador incrementoconsole.log()
console.log(incremento)
let decremento = numeroUno //25.6
decremento-- //operador decremento
console.log(decremento)
let cantidad = 22
let valorNegativo = -cantidad //Operador negativo, resultado esperado -22
console.log(valorNegativo)

//asignación
let enteroNumero = 65897
console.log(enteroNumero)
let asigSuma = (enteroNumero += 1)
console.log(asigSuma)
let asigResta = (enteroNumero -= 1)
console.log(asigResta)
let asigMultiplo = (enteroNumero *= 2)
console.log(asigMultiplo)
let asigDivisor = (enteroNumero /= 2)
console.log(asigDivisor)
let asigExponente = (enteroNumero **= 3)
console.log(asigExponente)
let asigResto = (enteroNumero %= 6)
console.log(asigResto)
let xorBit = (enteroNumero ^= 365)
console.log(xorBit)
let andBit = (enteroNumero &= 3256)
console.log(andBit)
let andClassic = (enteroNumero &&= 3256)
console.log(andClassic)
let orBitwise = (enteroNumero |= 3256)
console.log(orBitwise)
let orClassic = (enteroNumero ||= 3256)
console.log(orClassic)

// Operadores lógicos
let andLogico = 11 > 5 && 3654 < 12
console.log(andLogico)
let orLogico = 12 + 55 > 33 || 9987.2 < 254
console.log(orLogico)
let testNull = 12 / 22 ?? 12
console.log(testNull)
let negar = !isNaN(12212)
console.log(negar)

//Operadores de comparación
let mayorQue = 45 > 80
console.log(mayorQue)
let menorQue = 10 < 100000
console.log(menorQue)
let mayorIgual = 35.7 >= 10.8
console.log(mayorIgual)
let menorIgual = 99 <= 35
console.log(menorIgual)
let igualdad = 1254 == "1254" //compara por valor
console.log(igualdad)
let fullTest = 1254 === "1254" //compara por valor y tipo
console.log(fullTest)
let noIgual = 687 != 3587
console.log(noIgual)
let estrictoNot = 68 !== 3525487
console.log(estrictoNot)

//String operadores
let nameUser = "Yerlany"
let lastname = "Double"
let fullname = nameUser + lastname //concatenar string
console.log(fullname)

let value1 = 56
let value2 = 3698

//Bitwise operadores
let andOperador = value1 & value2 //and
console.log(andOperador)
let orOperador = value1 | value2 //or
console.log(orOperador)
let xor = value1 ^ value2 //Xor
console.log(xor)
let notOperador = ~value1 //Not
console.log(notOperador)

//Ternario Operador
let age = 28
let isAdult = age > 18 ? true : false
console.log(isAdult)

/**
 * Ejercicio 2 estructuras de control
 */

let saltoA = 2.45
let saltoB = 2.32

// Estructura if
if (saltoA > 3) {
  console.log("No es record olímpico")
}

//Estructura if - else
if (saltoA > saltoB) {
  console.log("Ha ganado el primer saltador")
} else {
  console.log("Ha ganado el segundo saltador")
}

let cuentaFin = 10
let inicio = 0

while (inicio <= cuentaFin) {
  console.log(`Faltan: ${cuentaFin - inicio} para terminar`)
  inicio++
}

/*let paso = 0
do {
  console.log("¡Welcome to JavaScript roadmap!")
} while (paso < 2)
*/
let result = []
let paso = 0

do {
  paso++
  result.push(paso)
} while (paso < 5)

console.log(result)
// Expected output: "12345"

//switch
let estacion = "verano"

switch (estacion) {
  case "otoño":
    console.log("Estación Otoño")
    break
  case "verano":
    console.log("Estación Verano")
    break
  case "invierno":
    console.log("Estación Invierno")
    break
  case "primavera":
    console.log("Estación Primavera")
    break
  default:
    console.log("Tipo de estación no encontrada")
}

// for

for (let index = 0; index < 10; index++) {
  //iteracion clasica
  console.log(index)
}

// for of  (objetos y array)
let animales = ["tigre", "tiburón", "oso", "leon"]
for (let values of animales) {
  console.log(`Animales del zoológico ${values}`)
}

//foreach array
let miPropiedad = { name: "Yoandy", profession: "front-end", code: "leon" }

let listaAnimales = animales.forEach((element) => {
  if (element == miPropiedad["code"]) {
    console.log("found")
  } else {
    console.log("No found")
  }
})

/**
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

function parEjercicio() {
  for (let index = 10; index <= 55; index++) {
    if (index !== 16 && index % 2 === 0 && index % 3 !== 0) {
      console.log("Numero par, no es 16 y no es múltiplo de 3: ", index)
    }
  }
}
parEjercicio()
