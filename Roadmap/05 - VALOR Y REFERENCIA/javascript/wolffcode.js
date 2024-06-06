/*
* EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
*/

        // asignación por valor
let color = 'naranja'
let fruta = color

color = 'amarillo'
console.log(color)
console.log(fruta)

        // asignación por referencia
const arr = [1,2,3,4,5]
const arr2 = arr

arr.push(10)
console.log(arr)
console.log(arr2)

        // funciones por valores
function valor(numero){
    numero --
    console.log(numero)
}
let numero = 5
valor(numero)
console.log(numero)

        // funciones por referencia
function referencia(fruta){
    fruta.cantidad = 3
    console.log(`la cantidad de ${frutaObj.nombre} es: ${frutaObj.cantidad} dentro de la función`)
}
const frutaObj = {
    nombre: 'banana',
    cantidad: 4
}
referencia(frutaObj)
console.log(`la cantidad de ${frutaObj.nombre} es: ${frutaObj.cantidad} fuera de la función`)
