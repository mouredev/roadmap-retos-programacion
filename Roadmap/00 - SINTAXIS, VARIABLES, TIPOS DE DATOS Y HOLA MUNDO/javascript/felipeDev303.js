// Documentación

// Los estándares de javascript los escuentras aquí: https://www.ecma-international.org/publications/standards/Ecma-262.html
// Documentación de Javascript en español: https://developer.mozilla.org/es/docs/Web/JavaScript
// Manz.dev tiene un recurso que también puede ayudar https://lenguajejs.com/

// SINTAXIS

// Este es un comentario de una sola línea en JavaScript y se utilizan principalmente para explicar el porqué no el cómo

/* Si prefieres puedes utlizar este tipo sintaxis 
para crear un comentario de varias líneas 
Es útil en el caso de que quieras "esconder" 
código y no tener que borrarlo*/

/* Crear una variable en JavaScript se hace con la palabra reservada var y let, 
se escriben en minúsculas, se usa camelCase y se pueden modificar */
var nombreDesarrollador = "Felipe";
var edadDesarrollador = 35;
var lenguajeDesarrollador = "JavaScript";

let nombreDesarrollador = "Felipe";
let edadDesarrollador = 35;
let lenguajeDesarrollador = "JavaScript";

/* Crear una constante en JavaScript se hace con la palabra reservada const, 
se escriben en mayúsculas y no se pueden modificar */
const NOMBRE_DESARROLLADOR = "Felipe";
const EDAD_DESARROLLADOR = 35;
const LENGUAJE_DESARROLLADOR = "JavaScript";

// Tipos de datos primitivos en JavaScript
// 1. String: cadena de texto
var nombreDesarrollador = "Felipe Morales";

// 2. Number: números enteros o decimales (javascript no diferencia entre enteros y decimales)
var edadDesarrollador = 35;

// 3. Boolean: verdadero o falso
var esDesarrollador = true;

// 4. Undefined: Variable declarada pero sin valor
var lenguajeDesarrollador;

// 5. Null: Valor nulo que representa la ausencia intencionada de un objeto
var lenguajeDesarrollador = null;

// 6. Symbol: Tipo de dato cuyas instancias son únicas e inmutables
var simbolo = Symbol();

// 7. BigInt: Tipo de dato numérico que permite representar números enteros de longitud arbitraria, mayor que 2^53 - 1
var numeroGrande = 1234567890123456789012345678901234567890n;

// Imprime en consola el texto: "¡Hola [Lenguaje de programación]!"
console.log("¡Hola, " + lenguajeDesarrollador + "!"); // concatenación de strings
let lenguajeDesarrollador = "JavaScript"; // reasignación de variable
console.log(`¡Hola, ${lenguajeDesarrollador}!`); // template string
