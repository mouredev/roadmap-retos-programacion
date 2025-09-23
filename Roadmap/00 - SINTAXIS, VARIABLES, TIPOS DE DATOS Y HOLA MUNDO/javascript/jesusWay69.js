/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.   
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/

// Comentario en una línea

/*
Comentario
en varias 
líneas
*/

let myString = "Javascript"
const myConstString = "Typescript"
let myNum = 50
let myBigNum = 646448546854584368458464n
let myFloat = 6.5
let myBool = true
let myUndef
let myNul = null
const mySymbol = Symbol('mySymbol')

console.log("Hola" + " " + myString) // Concatención string
console.log(`Hola ${myConstString}`) // Formateo string
console.log(50 + myNum) // Operiación numérica
console.log(60 + myNum + myConstString + 25) // opera y cuando aparece un string concatena

console.group("Agrupación de impresiones por consola:") // Agrupar logs
console.log(`tipo de dato: ${typeof(myString)}, valor: ${myString}`)
console.log(`tipo de dato: ${typeof(myConstString)}, valor: ${myConstString}`)
console.log(`tipo de dato: ${typeof(myNum)}, valor: ${myNum}`)
console.log(`tipo de dato: ${typeof(myBigNum)}, valor: ${myBigNum}`)
console.log(`tipo de dato: ${typeof(myFloat)}, valor: ${myFloat}`)
console.groupEnd() // Fin del grupo de logs

console.log(`tipo de dato: ${typeof(myBool)}, valor: ${myBool}
tipo de dato: ${typeof(myUndef)}, valor: ${myUndef}
tipo de dato: ${typeof(myNul)}, valor: ${myNul}
tipo de dato: ${typeof(mySymbol)}, valor: ${mySymbol.description}
`) //Impresión en varias líneas con un solo console.log




