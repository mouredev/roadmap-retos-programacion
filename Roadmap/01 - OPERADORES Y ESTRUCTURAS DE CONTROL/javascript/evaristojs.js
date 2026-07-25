/*Operadores aritmeticos*/
let suma = 10 + 5
let resta = 10 - 5
let multiplicacion = 10 * 5
let division = 10 / 5
let modulo = 10 % 3 //esto me dio especial curiosidad porque no sabia que existia
let incremento = 1
incremento++ // incremento = incremento + 1
let decremento = 1
decremento-- // decremento = decremento - 1

/*Operadores de asignacion en especial estos operadores hasta ahora le veo como utilidad que te hacen escribir menos codigo*/

let x = 10
x += 5 // x = x + 5
x -= 5 // x = x - 5
x *= 5 // x = x * 5
x /= 5 // x = x / 5
x %= 3 // x = x % 3

/*Operadores de comparacion*/

let a = 10
let b = '10'

console.log(a == b) // true (solo compara el valor y puede causar muchos problemas)
console.log(a === b) // false (compara valor y tipo de dato este te salva de muchos problemas porque no solo compara valores, tambien compara tipos de datos)
console.log(a != b) // false (solo compara el valor se puede usar pero no es recomendable)
console.log(a !== b) // true (compara valor y tipo de dato)
console.log(a > 5) // true
console.log(a < 5) // false
console.log(a >= 10) // true
console.log(a <= 10) // true

/*Operadores logicos*/

let c = 5
let d = 10

console.log(c > 0 && d > 0) // true (AND)
console.log(c > 0 || d < 0) // true (OR)
console.log(!(c > 0)) // false (NOT)

/*Estructuras de control*/

// Estructura condicional if...else
let edad = 18

if (edad < 18) {
    console.log('Menor de edad')
} else if (edad === 18) {
    console.log('Recién mayor de edad') /*se aplica === en vez de == para evitar errores en el codigo*/
} else {
    console.log('Mayor de edad')
} 
/* resumen en estas 3 condiciones es que si la edad es menor a 18 imprime menor de edad, si la edad es exactamente 18 imprime recien mayor de edad y si no se cumple ninguna de las dos condiciones anteriores imprime mayor de edad*/

// Estructura condicional switch
let color = 'rojo'

switch (color) {
    case 'rojo':
        console.log('El color es rojo')
        break
    case 'azul':
        console.log('El color es azul')
        break
    case 'verde':
        console.log('El color es verde')
        break
    default:
        console.log('Color no reconocido')
        break
} /*esta estructura switch es como un if pero mas ordenado y facil de leer cuando se tienen muchas condiciones, en este caso si el color es rojo imprime "El color es rojo", si es azul imprime "El color es azul", si es verde imprime "El color es verde" y si no es ninguno de esos colores imprime "Color no reconocido" puede parecer que nunca se usara algo como esto en la vida real pero creeme si se usa*/

// Estructura de bucle for
for (let i = 0; i < 5; i++) {
    console.log('Iteración número ' + i)
} /*esta madre siempre me dio problemas entenderlo por alguna razon ancestral que desconozco, pero ya lo entendi por fin y es muy util, en este caso imprime "Iteración número " seguido del numero de la iteracion desde 0 hasta 4 (5 no se incluye porque la condicion es i < 5)*/

// Estructura de bucle while
let j = 0
while (j < 5) {
    console.log('Iteración número ' + j)
    j++ /*no olvidar incrementar j para evitar un bucle infinito y dato curioso: ++ siempre suma 1 por si te preguntas porque no se pone de manera explicita, es raro porque la programacion a veces hay que ser sumanete especificos pero en este caso donde magicamente ++ suma 1 sin nadie construir esa funcion (al menos no de manera manual porque luego busque y resulta que si esta construida y es el mismo lenguaje que la tiene dentrod de el mismo supongo que es para ahorranos tiempo como devs)*/}

// Estructura de bucle do...while
let k = 0
do {
    console.log('Iteración número ' + k)
    k++
} while (k < 5) 
    /*esta estructura es similar a while pero la diferencia es que do...while siempre ejecuta el bloque de codigo al menos una vez antes de verificar la condicion, en este caso imprime "Iteración número " seguido del numero de la iteracion desde 0 hasta 4 (5 no se incluye porque la condicion es k < 5) util en validaciones, menus y demas cosas que deben pasar al menos una vez y luego ejecutadas si las condiciones se dan otra vez*/ 

// https://developer.mozilla.org/es/docs/Web/JavaScript

// Esta es la forma de representar un comentario en una sola línea

/* Esta es la forma de representar un comentario en varias líneas */

// Variables y Constantes
var name = 'Pedro' /*no se recomienda usar var porque tiene un scope global y puede causar problemas en el codigo como por ejemplo que la re declares sin querer mas adelante, que llames la variable sin declararla no es prohibido usarla pero tiene sus usos especificos*/
let name = 'Juan' /*Let es mas recomendable usarla porque tiene un scope de bloque y no puede ser redeclarada en el mismo scope*/ 
const ten = 10

// Datos primitivos
let lastname = 'López' // String
let age = 25 // Numero
let isMale = true // Boolean

let address // Indefinido se usa cuando una variable no tiene valor asignado

let stockAvailble = null /* Nulo se usa para representar la ausencia intencional de cualquier valor*/

let myBigInt = 2343n /* BigInt se usa en numeros muy grandes que superan el limite de los numeros normales en JS */

let mySymbol = Symbol('unique') /* Symbol se usa para crear identificadores unicos para propiedades de objetos */