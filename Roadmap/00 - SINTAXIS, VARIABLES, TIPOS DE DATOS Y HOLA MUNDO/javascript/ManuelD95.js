//https://www.javascript.com/

// Este es un comentario de una línea

/* Este es un comentario
Entre varias lineas
Y se puede usar para 
Explicar algo mas extenso*/

// Crea una variable
var Nombre = 'Java'
var Apellido = ' Script'

console.log (Nombre)
console.log (Apellido)
console.log (Nombre+Apellido)
console.log ('Hola Manuel')

// Crea una constante

const Pi = 3.1416 
console.log (Pi)

const Nombre1 = "Juan"; // Correcto
const Nombre2 = " Maria";

console.log(Nombre1 + Nombre2); // María

// Crear variables de diferentes tipos primitivos

let Nombre3 = "Manuel"; //string
let Edad = 30; // number int
let Agua = 4.20; // number float
let Enorme = 11170225n; // bigint
let esEncendido = true // boolean
let sinValor; // undefined, variable no inicializada 
let Vacio = null; // Sin valor
let id = Symbol("Clave"); // Identidicador

console.log (typeof Nombre);
console.log (typeof Enorme)
console.log (sinValor);

// Otras primitivas

let Persona = {       // object
    Nombre4: "Camilo",
    Edad: 29
};
console.log (Persona.Nombre4);
console.log (Persona.Edad);

let Colores = ["Amarillo", "Azul", "rojo"]; // Array
console.log (Colores)

// Imprime por terminal el texto "hola JavaScript"

function saludar(Nombre) {    //Function
    return `Hola, ${Nombre+Apellido}`;
  }
console.log(saludar(Nombre));


