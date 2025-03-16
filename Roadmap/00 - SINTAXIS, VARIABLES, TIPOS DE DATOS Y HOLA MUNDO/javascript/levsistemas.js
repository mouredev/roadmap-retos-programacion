/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

console.clear()

console.log("Javascript")
console.log("https://nodejs.org/es")

console.log("comentario1")
console.info("comentario2")
console.error("comentario3")
console.warn("comentario4")

let data = [["Leandro", 38], ["Brais", 37]]
console.table(data)

console.group("Usuario:")
console.log("Nombre: Leandro")
console.log("Edad: 38")
console.log("otra linea")
console.groupEnd()

console.time("Tiempo de ejecución")

for (let i = 0; i < 20000; i++ ) {

}

console.timeEnd("Tiempo de ejecución")

let age = 18
console.assert(age >= 18, "El usuario debe ser mayor de edad.")

console.count("Click")
console.count("Click")
console.countReset("Click")

function funcionA() {
    funcionB()
}

function funcionB() {
    console.trace("Seguimiento de la ejecución")
}

funcionA()

let miNombre = 'Leandro'
const fechaNacimiento = 1986

let string = 'Hola Mundo'
let number = 38
let float = 20.5
let boolean = true
let boolean_f = false
let vacio = null
let empty // Undefined
let mySymbol = Symbol('Mouredev')
let BigInt = 1000000000000000

console.log("¡Hola, Javascript!")