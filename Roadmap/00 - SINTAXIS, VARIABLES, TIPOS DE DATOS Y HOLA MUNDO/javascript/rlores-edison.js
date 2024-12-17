//00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
//Ejercicio

/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */





//este es el comentario de mi lenguaje de programación

/* este es un comentario de más de una línea que contiene la página web oficial 
del lenguaje elegido, que es javascript y la página oficial es 
https://262.ecma-international.org/14.0/ y también https://developer.mozilla.org/es/*/

let miVariable = "hola mundo"; // se utiliza si no se puede usar const
var MiOtraVariable = "hello world"; //se utiliza en código escrito para navegadores antiguos
const miConstante = "ciao mondo"; // esta es una constante, cuyo valor no debería cambiar (arrays y objetos)


const actor = "Chuck Norris", //esto es un string o cadena de texto
age = 69, 
isMale = true, //este dato es un boolean: true or false
height = 1.8, //float = decimales
weight = 70, // integer = entero
eyeColor = "blue", 
hairColor = "blond", 
birthday = new Date("1980-01-01"), 
hobbies = ["chess", "baseball", "snowboarding"], //Esto es un array
favFood = "", //esta variable tiene un valor undefined
language = "English";

Array.isArray(hobbies);


var numeroGrande = 9007199254740991n; // esto es un bigint, se añade "n" al final
const nullAux = null // esto es un valor nulo. En javascript, el valor null es una forma de representar la ausencia de un valor
typeof {name: "Raquel", age: 99} // devuelve object


console.log("¡Hola, JavaScript!");

