// Tipos de datos por valor
let a = 1
let b = 2
let c = b

// console.log(a)
// console.log(b)
// console.log(c)


// Tipos de datos por referencia
let d = [1, 2, 3]
let e = d
e.push(4)

// console.log(d)
// console.log(e)

// Funciones por valor
function f(a) {
  a = 5
  console.log(a)
}

// f(a)
// console.log(a)

// Funciones por referencia
function g(d) {
  d.push(20)
  console.log(d)
}

// g(d)
// console.log(d)


// Dificultad extra

// Funcion que intercambia dos variables por valor
function myFunc1(a, b) {
  let aux = a
  a = b
  b = aux
  return { a, b }
}

let myVar1 = 1
let myVar2 = 2

console.log(`Valores originales -> myVar1: ${myVar1}, myVar2: ${myVar2}`)

let { a: myVar3, b: myVar4 } = myFunc1(myVar1, myVar2)
console.log(`Valores Intercambiados -> myVar3: ${myVar3}, myVar4: ${myVar4}`)

// Funcion que intercambia valores por referencia
function myFunc2(a, b) {
  let aux = a
  a = b
  b = aux
  return { a, b }
}

let myArray1 = [1, 2, 3]
let myArray2 = [4, 5, 6]

console.log(`Valores originales -> myArray1: ${myArray1}, myArray2: ${myArray2}`)

let { a: myArray3, b: myArray4 } = myFunc2(myArray1, myArray2)
console.log(`Valores Intercambiados -> myArray3: ${myArray3}, myArray4: ${myArray4}`)
