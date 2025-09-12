// EJERCICIO:
//- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

// https://developer.mozilla.org/es/docs/Web/JavaScript

//- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

    // Esto es un comentario

    /*
        Esto es un comentario
        de varias líneas.
    */

//- Crea una variable (y una constante si el lenguaje lo soporta).

    let nombre;
    const Apellido = 'Torrealba';

//- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

    //String
    let name = 'Bob';

    //Number
    let edad = 10;

    //Boolean true/false
    let activo = true;

    //Array
    let miArray = [1,'Bob','Steve',10];

    //Object
    let miVariable = document.querySelector('h1');
//- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

let saludo = '¡Hola, ';
let lenguaje = 'JavaScript!'

console.log(saludo + lenguaje);