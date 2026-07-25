// #00 { retosparaprogramadores } SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// TypeScript - Official URL: https://www.typescriptlang.org/

/* by @duendeintemporal */

// One-line comments 
/* Comments
                of
                     many lines */

/* I set my environment in the following way:
1. First, run:
   npm init -y
2. Then, install TypeScript and ts-node globally:
   npm install -g typescript ts-node
3. Now I can run my TypeScript files directly using:
   ts-node ./src/my_file.ts
*/


let lang: string; // Variable to hold the programming language
let num: number; /* 
   The 'let' keyword declares a variable with block scope. 
   Unlike 'var' in JavaScript, 'let' does not attach to the window object in the global context.
*/

const MIN_VA: number = 0; /* 
   'const' declares a constant with block scope and must be initialized with a value. 
   By convention, constants are usually named using capital letters.
*/

// Primitive Types or Primitive Values

let hello: string = 'Hi Girl!'; // string type
console.log(hello); // Hi Girl!
console.log(`String type: ${hello}`, typeof hello); // String type: Hi Girl! string

let x_coord: number = 100; // number type
console.log(x_coord); // 100
console.log('Number type: ', typeof x_coord); // Number type:  number

let bool: boolean = true; // boolean type
console.log(bool); // true
console.log('Boolean type: ', typeof bool); // Boolean type:  boolean

let stack: number[] = [0, 1, 2, 3, 4, 5, 6]; // array type
console.log(stack); // [ 0, 1, 2, 3, 4, 5, 6 ]
console.log('Array type: ', typeof stack); // Array type:  object

let obj: { name: string; age: number; profession: string; greetings: () => void } = {
    name: 'Niko',
    age: 41,
    profession: 'Writer & Web Developer',
    // method
    greetings: function () {
        console.log(`Hello, I am ${this.name} and it's a pleasure to start and share this roadmap with you !!`);
    }
}; // object type

console.log(obj);
/* 
Object type:  {
    name: 'Niko',
    age: 41,
    profession: 'Writer & Web Developer',
    greetings: [Function: greetings]
  } */
    console.log('Object type: ', typeof obj);  // Object type:  object
    obj.greetings(); // Hello, I am Niko and it's a pleasure to start and share this roadmap with you !!

let tuple: [string, number, boolean, { webmaster: string }] = ['Soe', 35, true, { webmaster: 'Niko' }];
console.log(tuple); // [ 'Soe', 35, true, { webmaster: 'Niko' } ]
console.log('Tuple type: ', typeof tuple); // Tuple type:  object

enum Color {
    Red,
    Green,
    Blue,
    Black,
    Purple
}
console.log('Enum type: ', typeof Color); // Enum type:  object
let fontColor: Color = Color.Green;
console.log('Enum type: ', typeof fontColor); // Enum type:  number


let obj2: null = null; 
/* 
   Represents the absence of a value, helping to handle situations where a value is not available 
   or has not been intentionally defined.
*/
console.log('Null type: ', typeof obj2); // Null type:  object

let obj3: undefined; // undefined type 
/* 
   'undefined' indicates that a variable has been declared but not initialized.
*/
console.log('Undefined type: ', typeof obj3); // Undefined type:  undefined

let anything: any = "I can be anything!";
console.log('Any type: ', typeof anything); // Any type:  string
anything = 42; // Now it's a number type
console.log('Any type after reassignment: ', typeof anything); // Any type after reassignment:  number


let syn: symbol = Symbol('syn'); // symbol type
console.log('Symbol type: ', typeof syn); // Symbol type:  symbol
/* 
   Symbols can be used to prevent object collisions, such as creating hidden non-enumerable properties 
   on objects or private methods in a class.
*/

let amount: bigint = BigInt(3783787487877877887) * BigInt(2); // bigint type
console.log(amount) // 7567574975755755520n
console.log(`BigInt type: ${amount}`, typeof amount); // BigInt type: 7567574975755755520 bigint
/* 
   Using BigInt is especially useful in situations where accuracy is required in calculations 
   with large integers, such as in financial or crypto applications.
*/

/* 
   'typeof' is an operator that we can use to determine a type or make type comparisons.
*/
console.log('Is amount of bigint type:', (typeof amount === "bigint")); // Is amount of bigint type: true

// Short for console.log()
let log = console.log.bind(console); 

// Function with type annotations
function add(a: number, b: number): number {
    return a + b;
}
log('Function result: ', add(25, 18)); // Function result: 43

// Interfaces in Typescript are use to define a type with properties.
interface Person {
    name: string;
    age: number;
}

let person: Person = {
    name: 'Bob',
    age: 34
};
log('Interface type: ', typeof person); // object

// Ejemple of Type Assertion
let someValue: any = "this is a example string";
let strLength: number = (someValue as string).length;
log('String length: ', strLength); // String length: 24

// Arrow function with type annotations and Promises
const fetchData = (): Promise<string> => {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Data fetched!");
        }, 2000);
    });
};

fetchData().then(data => log(data)); // Data fetched! (after 2 seconds)

// Assigning a new value to a previously declared variable
lang = 'Typescript';

// Print in console
log(`Hello, ${lang}`); // Hello, Typescript
