//// Author: Jheison Duban Quiroga Quintero
//// Github: https://github.com/JheisonQuiroga
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 **/

// 1. Función Simple

// Declaración de una función
function helloWorld() {
    console.log("Hello World!")
}

// Llamada a la función.
helloWorld()

// 1.1. Función con parámetros.

greet("Duban")

function greet(name) {
    console.log(`Hello, ${name}`)
}

// 1.3. Retorno de una función (retornando un valor)

function yourName(name) {
    return name
}

console.log(yourName("Duban"))


// 1.4. Function Expressions

const addNumbers = function(n1, n2) {
    return n1 + n2
}

console.log(addNumbers(2, 3))

// 1.5. Arrow Functions

const multiply = (n1, n2) => n1 * n2
console.log(multiply(5, 7)) 

const divide = (n1, n2) => {
    if (n2 === 0) {
        throw new Error("No se puede dividir entre cero 💀")
    }
    return n1 / n2
}

try {
    console.log(divide(10, 0))
} catch (err) {
    console.error(err.name, err.message)
}

// 2. Función dentro de otra función

function outerFunction() {
    function innerFunction() {
        return "Función interna"
    }
    return innerFunction()
}

console.log(outerFunction())

// 3. Funciones globales dentro del lenguaje

console.log(typeof parseInt("10"))
console.log(typeof parseFloat("10.69"))

// Métodos del objeto Math
Math.max(1, 2, 3, 4, 5) // Retorna el número mayor
Math.min(1, 2, 3, 4, 5) // Retorna el número menor


//// 4. Variables globales y locales
const pi = Math.PI // Variable global

const circleArea = function(radius) {
    const piFunction = 3 // Variable local
    return piFunction * radius ** 2
}

console.log(`Área del círculo: ${circleArea(5)}`)

// Accediendo a la variable local de la función
// console.log(piFunction) // ReferenceError piFunction is not defined

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

function fizzBuzz(firstString, secondString) {
    for (let i = 1; i <= 100; i++) {
        switch (true) {
            case i % 3 === 0 && i % 5 === 0:
                console.log(`${firstString} ${secondString}`)
                break
            case i % 3 === 0:
                console.log(firstString)
                break
            case i % 5 === 0:
                console.log(secondString)
                break
            default:
                console.log(i)            
        }
    }
}

fizzBuzz("Fizz", "Buzz")