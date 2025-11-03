/*
_____________________________________
https://github.com/JDesing
2025 - JavaScript
_______________________________________
01 OPERADORES Y ESTRUCTURAS DE CONTROL
---------------------------------------
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
*/

// _______________________
// Referencias:
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference
// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide

// _______________________
// Tipos de operadores
// https://developer.mozilla.org/es/docs/Learn/Getting_started_with_the_web/JavaScript_basics#operadores

// _______________________
// Concatenación
console.log("===============================")
console.log("Concatenación")

let saludo = "🙋🏻 Hola " + "JavaScript!!!"
console.log(saludo)

let numero = 2025
console.log("Año: " + numero)

let mezcla = saludo + " " + "Estamos en " + numero + " ✅"
console.log(mezcla)

// _______________________
// Operador de asignación "=":
console.log("===============================")
console.log("Operador de asignación '='")

let miString = 'JDesing'
console.log(miString) // "JDesing"

let b = 3
b += 2 // Aplicable a todos los operadores aritméticos.
console.log(b) // 5

// _______________________
// Operadores aritméticos:
// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_Operators#arithmetic_operators

console.log("===============================")
console.log("Operadores aritméticos")
console.log("Suma (+), Resta (-), Multiplicación (*), División (/), Resto (%), Potenciación (**), Incremento (++), Decremento (--)")

let suma = 10 + 34
console.log(suma) // 44

let resta = 10 - 6
console.log(resta); // 4

let multiplicacion = 7 * 2
console.log(multiplicacion) // 14

let division = 12 / 3
console.log(division) // 4

let resto = 20 % 7
console.log(resto) // 6

let potenciacion = 2 ** 3
console.log(potenciacion) // 8

// Incremento
let incremento = 5
console.log(++incremento) // 6

// Decremento
let decremento = 5
console.log(--decremento) // 4

// _______________________
// Operadores de Comparación:
console.log("===============================")
console.log("Operadores de Comparación")
console.log("Igual a (==),Estrictamente igual (===),  Diferente de (!=), No estrictamente igual (!==), Menor que (<), Mayor que (>), Menor o igual (<=), Mayor o igual (>=)")

let igual = 5 == "5" // Igual a
console.log(`5 == 5 -> ${igual}`) // true

let estrictamenteIgual = 5 === 5 // Estrictamente igual
console.log(`5 === 5 -> ${estrictamenteIgual}`) // true

let noIgual = 5 != 5 // Diferente de
console.log(`5 != 5 -> ${noIgual}`) // false

let menorQue = 4 < 5 // Menor que
console.log(`4 < 5 -> ${menorQue}`) // true

let mayorQue = 4 > 5 // Mayor que
console.log(`4 > 5 -> ${mayorQue}`) // false

let menorOIgual = 4 <= 5 // Menor o igual
console.log(`4 <= 5 -> ${menorOIgual}`) // true

let mayorOIgual = 4 >= 5 // Mayor o igual
console.log(`4 >= 5 -> ${mayorOIgual}`) // false

// _______________________
// Operadores Lógicos:
console.log("===============================")
console.log("Operadores Lógicos")
console.log("AND (&&), OR (||), NOT (!)")

let operadorAnd = (5 < 10) && (10 > 5) // AND lógico
console.log(`(5 < 10) && (10 > 5) -> ${operadorAnd}`) // true

let operadorO = (5 < 10) || (10 < 5) // OR lógico
console.log(`(5 < 10) || (10 < 5) -> ${operadorO}`) // true

let operadorNo = !(5 < 10) // NOT lógico
console.log(`!(5 < 10) -> ${operadorNo}`) // false

// _______________________
// Operadores a nivel de bits:
console.log("===============================")
console.log("Operadores a nivel de bits")
console.log("AND (&), OR (|), XOR (^), Desplazamiento a la izquierda (<<), Desplazamiento a la derecha (>>), Desplazamiento a la derecha sin signo (>>>)")

let bitAnd = 5 & 3 // AND a nivel de bits
console.log(`5 & 3 -> ${bitAnd}`) // 1

let bitOr = 5 | 3; // OR a nivel de bits
console.log(`5 | 3 -> ${bitOr}`); // 7
let bitXor = 5 ^ 3; // XOR a nivel de bits
console.log(`5 ^ 3 -> ${bitXor}`); // 6
let leftShift = 5 << 1; // Desplazamiento a la izquierda
console.log(`5 << 1 -> ${leftShift}`); // 10
let rightShift = 5 >> 1; // Desplazamiento a la derecha
console.log(`5 >> 1 -> ${rightShift}`); // 2

// Estructuras de control
// _______________________
console.log("===============================")
console.log("Estructuras de control")
console.log("Condicionales: if-else")

// Condicionales:
if (5 == 5) { // Aplicable a todos los operadores de Comparación.
    console.log("Si lo es.")
} else if (5 == 6) {
    console.log("Si no, si es.")
}else {
    console.log("Si no lo es.")
}

// Con operadores lógicos:
if (5 == 5 && 7 < 10) { // Equivalente a 'and'
    console.log("Ambas condiciones son verdaderas.");
} else {
    console.log("Al menos una condición es falsa.");
}

// _______________________
// Estructura condicional: switch
console.log("===============================")
console.log("Estructura condicional: switch")

let dia = 3
switch (dia) {
    case 1:
        console.log("Lunes")
        break
    case 2:
        console.log("Martes")
        break
    
    default:
        console.log("Otro día")
        break
}

// _______________________
// Estructuras iterativas (Bucles):
// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Loops_and_iteration

console.log("===============================")
console.log("Estructuras iterativas (Bucles)")
console.log("for, while, do-while")

// Bucle for
console.log("Bucle for:")
for (let contar = 0; contar < 5; contar++) {
    console.log(`i = ${contar}`)
}

// Bucle while
console.log("Bucle while:")
let contar = 4
while (contar > 0) {
    console.log(`Contar = ${contar}`)
    contar--
}

// Bucle do-while
console.log("Bucle do-while:")
let numero2 = 0
do {
    console.log(`num = ${numero2}`)
    numero2++
} 
while (numero2 < 3)

console.log("===============================")
console.log("Fin del programa")
console.log("===============================")
// _______________________
// Fin del programa
//
