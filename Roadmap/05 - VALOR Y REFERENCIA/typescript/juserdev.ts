/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

let variable1 = 10
let variable2 = variable1
// variable2 = 20
variable1 = 30
console.log(variable1)
console.log(variable2)

// tipos de datos por refernecia

let myListA = [10, 20]
let myListb = myListA
myListb.push(30) //aqui se agrego el valor a ambos arrays
console.log(myListA)
console.log(myListb)

let myNumber: number = 10

function myFunctionA(myInt:number):number {
    myInt = 20
    return myInt
}

console.log(myFunctionA(myNumber))
console.log(myNumber)
