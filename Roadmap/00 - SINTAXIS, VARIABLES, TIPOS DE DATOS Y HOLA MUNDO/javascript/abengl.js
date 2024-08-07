//Ejercicio 00

//1- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
//https://developer.mozilla.org/es/docs/Web/JavaScript

//2- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

//JavaScript (JS) es un lenguaje de programación ligero, interpretado, o compilado justo-a-tiempo.

/*
    Si bien es más conocido como un lenguaje de scripting (secuencias de comandos) para páginas web, y es usado en muchos entornos fuera del navegador, tal como Node.js, Apache CouchDB y Adobe Acrobat JavaScript es un lenguaje de programación basada en prototipos, multiparadigma, de un solo hilo, dinámico, con soporte para programación orientada a objetos, imperativa y declarativa (por ejemplo programación funcional). Lee más en acerca de JavaScript.
*/

//3- Crea una variable (y una constante si el lenguaje lo soporta).
let counter = 0;    //Variable
const PI = 3.1415;  //Constante

//4- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
const text = "Hello";    //string
const interestRate = 5.3;  //number
const population = 149_597_870_700n //bigint
const status = true;    //boolean
let sum;    //undefined
const userID = Symbol("id");    //symbol
const array = null;     //null

//5- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
console.log("¡Hola, JavaScript!");