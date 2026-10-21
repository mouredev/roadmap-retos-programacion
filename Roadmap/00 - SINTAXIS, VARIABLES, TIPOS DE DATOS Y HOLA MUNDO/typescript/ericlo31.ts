// https://www.typescriptlang.org/

// Comentario en una línea

/* Comentarios en multiples líneas
   Comentarios en multiples líneas
   Comentarios en multiples líneas
*/

// Puedes declarar el tipo de variable
let números: number = 31;
let decimales: number = 125.934; // number cubre los decimales también.
let cadenasDeTexto: string = "TypeScript";
let númerosGrandes: bigint = 928517264937259n;
let booleanos: boolean = true;

// También puedes  dejar que TypeScript asuma su tipo
let número = 15;
let decimal = 125.934;
let cadenaDeTexto = "JavaScript < TypeScript";
let númeroGrande = 12432482342582n;
let booleano = false;

// Aqui TypeScript no controla el tipo de la variable
let cualquier: any = "Variable";

// Esto es una forma que se utilizaba anteriormente para declarar una variable. Evita utilizarlo
var variable = 123;

// Se declaran las constantes poniendo el prefijo const
const númeroPI: number = 3.14;

console.log(`Hola, ${cadenasDeTexto}`);
