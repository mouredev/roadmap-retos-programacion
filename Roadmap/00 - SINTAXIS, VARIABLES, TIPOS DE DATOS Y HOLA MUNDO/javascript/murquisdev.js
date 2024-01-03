
// DOCUMENTACIÓN JS
// https://developer.mozilla.org/es/docs/Web/JavaScript 

// COMENTARIOS
// Se pueden crear comentarios en una línea

/* O en 
varias líneas
*/

x = 3 // tanto los "slash" (barra /) como el "slash" + *  crean el comentario después /*, no a línea completa
x = x + 5 // 8

// VARIABLES Y CONSTANTES
// JS tiene dos formas de crear variables, la diferencia se explicará más adelante
// Al ser un lenguaje debilmente tipado, NO es necesario añadir el tipo de variable

// Usando la palabra reservada var
var variableUno = 1 // tipo number (número)
variableUno = "Uno" // tipo String (cadena)

// Usando la palabra reservada let
let variableDos = 2
variableDos = "Dos"

// Las constantes se crean con la palabra CONST

const CONSTANTE = "Soy una constante"

// DATOS PRIMITIVOS

/* JS tiene 7 tipos de datos primitivos y NO es necesario indicar que tipo de dato va almacenar la variable
    Los 3 "básicos"
    number
    string
    boolean

    null --> valor literal de JS, indica el valor nulo o "vacío" --> https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/null
    undefined --> Sin definir, una variable a lo que no se le asigna un valor --> https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/undefined
    symbol  --> Un objeto para crear valores únicos --> https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Symbol
    bigint --> Como number pero para almacenar números muy grandes

*/
let numero = 1 // number

let cadena = "String" // String --> Se puede indicar un String con "", con '' o ``.
let comillasSimples = 'Cadena con comillas simples'
let comillasInclinadas = `Cadena con comillas inclinadas`

let boleano = true // boolean --> Solo acepta true o false (verdadero o falso)

// ESCRIBIR POR CONSOLA
// Para escribir por consola se utiliza la función console.log()
console.log("!Hola, JavaScript!")
