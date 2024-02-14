// Operadores en TypeScript

// Operadores Aritméticos
let suma = 10 + 5
console.log("El resultado de la suma 10 + 5 es:" + suma)

let resta = 10 - 5
console.log("El resultado de la resta 10 - 5 es:" + resta)

let multiplicacion = 10 * 5
console.log("El resultado de la multiplicación 10 * 5 es:" + multiplicacion)

let division = 10 / 5
console.log("El resultado de la división 10 / 5 es:" + division)

let modulo = 10 % 5
console.log("El resultado del módulo 10 % 5 es:" + modulo)

let potencia = 10 ** 5
console.log("El resultado de la potencia 10 ** 5 es:" + potencia)

// Operadores de Asignación
let asignacion = 10
console.log("El resultado de la asignación es:" + asignacion)

asignacion += 5
console.log("El resultado de la asignación += 5 es:" + asignacion)

asignacion -= 5
console.log("El resultado de la asignación -= 5 es:" + asignacion)

// Operadores de Comparación
let a = 10
let b = 5

let igualdad = a == b
console.log("El resultado de la igualdad de a == b es:" + igualdad)

let igualdadEstricta = a === b
console.log("El resultado de la igualdad estricta de a === b es:" + igualdadEstricta)

let desigualdad = a != b
console.log("El resultado de la desigualdad de a != b es:" + desigualdad)

let mayorQue = a > b
console.log("El resultado de la mayor que de a > b es:" + mayorQue)

let menorQue = a < b
console.log("El resultado de la menor que de a < b es:" + menorQue)

let menorQueOigual = a <= b
console.log("El resultado de la menor que o igual de a <= b es:" + menorQueOigual)

let mayorQueOigual = a >= b
console.log("El resultado de la mayor que o igual de a >= b es:" + mayorQueOigual)

// Operadores de Lógicos
let and = true && false
console.log("El resultado de la conjunción de and es:" + and)

let or = true || false
console.log("El resultado de la disyunción de or es:" + or)

let not = !true
console.log("El resultado de la negación de not es:" + not)

// Estructuras de Control
// if else
let ifElse = 10
if (ifElse > 5) {
  console.log("El valor de ifElse es mayor que 5")
} else {
  console.log("El valor de ifElse es menor o igual que 5")
}

// switch
let switchCase = 10
switch (switchCase) {
  case 5:
    console.log("El valor de switchCase es 5")
    break
  case 10:
    console.log("El valor de switchCase es 10")
    break
  default:
    console.log("El valor de switchCase no coincide con ninguno de los casos")
    break
}

// for
for (let i = 0; i < 10; i++) {
  console.log("El valor de i es:" + i)
}

// while
let whileLoop = 0
while (whileLoop < 10) {
  console.log("El valor de whileLoop es:" + whileLoop)
  whileLoop++
}

// try catch
let tryCatch = 10
try {
  console.log("El valor de tryCatch es:" + tryCatch)
} catch (error) {
  console.log("Error:" + error)
} finally {
  console.log("Este es un bloque finally")
}

// Numeros entre 10 y 55
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i % 3 !== 0 && i !== 16) {
    console.log(i)
  }
}
