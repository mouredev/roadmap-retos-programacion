// #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
// https://www.javascript.com/

/*
    Comentario de
    varias
    lineas
 */


let variable;                       // Undefined
const variableConstante = 3.14; 

// Tipo de variables con datos primitivos numericos
let tipoInteger = 123;
let tipoFloat = 3.14;
let tipoEnteroNegativos = -354565;
let tipoBigInt = 123456789n         // Importante la "n" al final

// Tipo de variables con datos primitivos booleanos
let tipoBoolean = true;

// Tipo de variables con datos primitivos referenciados
let tipoArreglo = ['Pablo', 'Veiga', 'Argentino', 'Barcelona'];
let tipoObjeto = {
    nombre: "pablo",
    ciudad: "barcelona",
    nacionalidad: "Arg/Ita",
    edad: 35,
    trabaja: true
}
 
const saludoBienvenida = "¡Hola";
const lenguaje = "javascript";

console.log(`${ saludoBienvenida } desde ${ lenguaje }`)
