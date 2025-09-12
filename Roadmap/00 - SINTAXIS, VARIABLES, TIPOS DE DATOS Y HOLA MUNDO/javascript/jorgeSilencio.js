//Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
// Documentación URL: https://developer.mozilla.org/en-US/docs/Web/JavaScript




// Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

// 1) Comentario de una línea

// 2) 
/* Comentario
de varias
líneas */




// Crea una variable (y una constante si el lenguaje lo soporta).

// Variables en Javascript
var numero = 9;
let letra = "A";
const texto = "Hola";

// También se pueden escribir varias variables separadas por comas.
let numero = 1, numero2 = 2, numero3 = 3;





 // Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...)

 // TIPOS DE DATOS

// String
let saludo = "Hola Mundo";

// Number
let entero = 135;
let flotante = 1.54;

// BigInt
let numeroGrande = 1238734534863143n;
let numeroGrande2 = BigInt(1237653465713654);

// Boolean
let booleano1 = true;
let booleano2 = false;

// Null
let nulo = null;

// Undefined
let indefinido = undefined;

// NaN
let notANumber = "Hola1" * "Hola2";

// Array
let arreglo = ['Elemento1', 'Elemento2', 'Elemento3', true, false, {propiedad1: 'valor1'}];

// Object
let objetos = {
    nombre: 'Jorge',
    apellido: 'Silencio',
    edad: 40,
    suscrito: true,
    tipoDeSuscripcion: {
        github: true,
        youtube: true,
    }
}




// Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
console.log("¡Hola Javascript!");