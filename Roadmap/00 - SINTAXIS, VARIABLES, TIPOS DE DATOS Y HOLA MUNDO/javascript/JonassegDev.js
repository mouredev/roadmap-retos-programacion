// Este es el repositorio que seguire https://developer.mozilla.org/en-US/docs/Web/JavaScript
/* Puedo hacer comentarios
en varias lineas tambien*/ 

//Variables Constante

/*la variable "const"
es una variable con datos constantes o que no se cambian*/
const PI = 3.1416
console.log(PI)
// PI = 3.15; // Error: asignación a variable constante.

//Variable var

/*la variable "var" puede ser 
reasignada y redeclarada*/
var nombre = "Juan";
nombre = "Carlos"; // Reasignación
var nombre = "Pedro"; // Redeclaración

//variables var diferentes comillas.
var texto1 = "Mis Primeras Variables" //comillas dobles
var texto2 = 'Texto Con Comillas Simples' // Comillas Simples
var texto3 = "comillas 'simples' dentro de unas dobles" // Comillas mixtas

console.log(texto1)
console.log(texto2)
console.log(texto3)

//Variable let

/*la variable let puede ser
reasignada pero no redeclarada*/
let edad = 25
edad = 30 // Reasignacion
// let edad = 32 // Error "edad" no puede ser redeclarada la misma variable.

// Tipos de datos.

/*JavaScript es un lenguaje de tipado dinámico, 
lo que significa que no necesitas especificar el tipo de dato de una variable al declararla. 
JavaScript determinará el tipo de dato en tiempo de ejecución. 
Los tipos de datos principales son:*/

//Numeros (number).
let entero = 10
let decimal = 3.14

//Cadena (string).
let saludo = "Hola Mundo"

//Booleanos (booleans) representan valores logicos como: "true" o "false"
let soyEstudiante = true
let soyDocente = false

//Indefinido (indefined) Representa una variable que ha sido declarada pero no se le ha asignado un valor.

let sinValor
console.log (sinValor) // Resultado "undefined"

//Nulo (null) Representa un valor nulo o vacío.

let valorNulo = null

//Objetos (object) Representan colecciones de propiedades (pares clave-valor).
let gato = {
nombre: "Michi",
edad: 2
}

//Simbolo (symbol) Representan valores únicos e inmutables.

let simbolo = Symbol("mySymbol")

// Imprimir el Hola mundo.

let miSaludo = 'Hola, JavaScript'
console.log (miSaludo)

