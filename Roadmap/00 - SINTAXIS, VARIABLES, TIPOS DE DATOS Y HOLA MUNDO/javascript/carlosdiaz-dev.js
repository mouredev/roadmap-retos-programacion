// https://developer.mozilla.org/es/docs/Web/JavaScript

// Sintaxis de comentario para una sola línea 

/* Sintaxis de 
comentario para 
varias líneas 
(bloque de código)*/

//Variables y constantes JS
var nombre = 'Carlos';
let edad = 32; // Disponible sólo dentro del bloque en que se decla
const lenguaje = 'JavaScript'; // Su valor no cambia una vez asignado

// Datos primitivos JS
// undefined: Variable sin valor asignado
let a;
// null: Objeto sin valor
let b = null;
// boolean: Valor lógico 1|0
let c = true;
let d = false;
// number: Valor numérico enteros y flotantes. Valores especiales infinity, NaN (Not a Number)
let e = 32;
let f = 3.14
let g = Infinity;
let h = NaN;
// string: Cadena de caracteres, admite "", '', ´´
let i = 'Esto es un string';
// symbol: Valor único, identificadores únicos para propiedades de objetos
let j = Symbol('descripcion');
// bigint: Enteros fuera del rango de number
let k = 123456778900009877765432346789000n;

console.log('Hola, ' + lenguaje);