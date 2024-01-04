// Comentario + URL del programa
// www.javascript.com

//Sintaxis de comentarios

// Este es un comentario en una línea.

/*
Este
es
un
comentario
en 
varias
líneas.
*/


// Variables (Let y Var) y una constante (Const)
let EsUnaVariable = "Limitada" // Permite declarar una variable limitando su alcance al bloque, declaración o expresión donde se esté usando.
var EsOtraVariable = "Ilimitada" // Permite definir una variable global o local en una función sin importar el ámbito del bloque.
const PI = 3.14 // Es para declarar una constante. Es un valor que no se puede cambiar.


// Ejemplos de variables con datos primitivos

// String
let my_string = "Esta es una cadena de texto"; //Se usa para escribit texto

// Number
let my_number = 8; // Se usa con numeros enteros.
let other_number = 1.5; // También con números decimales.
let bigInt = 1234567898765432123456789n; // Es una variable para números largos.

// Boolean: tipo lógico
let my_boolean = true;
let other_boolean = false;

// Undefined y Null
let undefined; // Es un valor no asignado.
let abc = null; // Es un valor desconocido. Vacío. Nada.

// Symbol y Object
let object = new Date("2024-03-14")  // Se usan para almacenar colecciones de datos y entidades más complejas
let symbol = Symbol(); // Se utiliza para crear identificaodres únicos para los objetos.

//Imprimir un texto dentro de la consola.
console.log("Hola, Javascript!")