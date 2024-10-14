// ##00 - SINTAXIS, VARIABLES, TIPOS DE DATOS, Y "HOLA MUNDO"*/

/*EJERCICIO: 
Crea un comentario en el código y coloca la URL del sitio web oficial del
  lenguaje de programación que has seleccionado. */

//https://developer.mozilla.org/es/docs/Web/JavaScript

/*EJERCICIO:
  Representa las diferentes sintaxis que existen de crear comentarios
   en el lenguaje (en una línea, varias...)*/

//  Esta es la forma de comentar el código con una sola línea
/*Esta es la forma de comentar el código usando más de una línea. Es muy similar a otros lenguajes de programación */

/*EJERCICIO:
   Crea una variable (y una constante si el lenguaje lo soporta)
    */

// Variable  usando "let"
let variableNueva = "Variable no constante";

//Variable usando "var" (en desuso)
var variableVieja = "Variale no constante vieja";

// Variable llamada Constante. Sólo se usa para crear una variable que no se modificará
const variableConstante = "Variable constante";

/*EJERCICIO:
 Crea variables representando todos los tipos de datos primitivos
   del lenguaje (cadenas de texto, enteros, booleanos...)*/

/*Los tipos de datos son la naturaleza del contenido de una variable o constante.Javascript dispone de muchos tipos de datos, sin embargo, se suelen catalogar en dos grupos: tipos de datos primitivos (básicos) y tipos de datos no primitivos (complejos). Los datos primitivos son siete*/

// "String" o Cadena de texto
let cadenaDeTexto = "Esteban";

// "Number" o valor numérico
let valorNumérico = 45;

// "Bigint". Es un valor numérico muy grande

let valorNumericoGrande = 50n;

// "Boolean" o booleano: Tipo de valor "Falso" o "Verdadero"
let valorBooleanoFalso = false,
  valorBooleanoVerdadero = true;

//"Symbol": Tipo de dato para crear valores únicos.
const valorUnico = Symbol("Único");

// "Unefined": Valor sin definir (variable sin inicializar)
let valorIndef = undefined;

//"Null": Representa un valor vacío o ausencia de información
let valorNulo = null;

/*EJERCICIO:
Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" */

console.log("¡Hola, Javascript!");
