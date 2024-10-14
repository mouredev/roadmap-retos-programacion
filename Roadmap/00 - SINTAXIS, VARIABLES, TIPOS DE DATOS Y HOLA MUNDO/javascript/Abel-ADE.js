// Página Web Oficial: https://developer.mozilla.org/es/docs/Web/JavaScript

//Tipos de comentarios en JS:

    // Comentario de una sola línea
    /*  Comentario 
        multilínea 
    */

    /**
     * Comentario multilínea 
     * que se utiliza 
     * para generar documentación del programa
     */

//Declaración y asignación de variables
var miVariableGlobal = 'Soy otra variable';
let miVariableLocal = 'Soy una variable'; //Se recomienda usar esta

//Declaración y asignación de constantes
const MI_CONSTANTE = 12; //Se define en tiempo de compilación

//Mostrar el contenido
console.log(miVariableGlobal);
console.log(miVariableLocal);
console.log(MI_CONSTANTE);

//Tipos de datos primitivos en JS
let miNumero = 100;
let miBooleano = true;
let miTexto = 'Soy un texto';
let miNulo = null;
let miVariableNoDefinida; // devuelve 'undefined'

//Formas de declarar strings
let miTexto1 = 'Soy un texto';
let miTexto2 = "Soy un texto";
let miTexto3 = `Soy un texto`;

//Imprime por terminal el texto: 'Hola, Js!'
console.log('Hola, Js!');
