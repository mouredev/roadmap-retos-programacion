/*
    EJERCICIO:
    1) Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    2) Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    3) Crea una variable (y una constante si el lenguaje lo soporta).
    4) Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// 1) https://www.typescriptlang.org/docs/

// 2) Comentario de una linea y varias

/*
    Comentario de varias lineas
 */
// 3) Variable y constante
let variable: string = "texto";
const pi: number = 3.1416;
// 4) Tipos de variables primitivas https://www.typescriptlang.org/docs/handbook/2/everyday-types.html

// Tipos de dato undefined, null o cualquier cosa
let nulo = null;
let indefinido: undefined = undefined;
let cualquier_cosa: any = "Cualquier cosa";

// Tipos de dato numericos, number,BigInt
let numero: number = 123;
let decimal: number = 3.1416;
let color: number = 0xFF0000;
let numeroGrande: bigint = 9007199254740991n;

// Tipos de dato texto
let cadena: string = "Texto";

// Tipos de dato boleano
let boleanoVerdadero: boolean = true;
let boleanoFalso: boolean = false;

// Tipos de dato Symbol, se usa crear identificadores unicos
let variableSymbol: symbol = Symbol("descripcion");

// Tipos de dato lista y objetos
let lista: Array<number> = [1, 2, 3];
let objecto: object = { 1: "primero", 2: "segundo" };

// 5) print JavaScript
console.log("¡Hola, TypeScript!");
