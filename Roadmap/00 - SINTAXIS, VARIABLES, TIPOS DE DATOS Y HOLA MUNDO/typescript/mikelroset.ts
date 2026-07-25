// ------------------------- DOCUMENTACIÓN OFICIAL ------------------------- //

// https://www.typescriptlang.org/


// -------------------------- TIPOS DE COMENTARIOS -------------------------- //

// Esto es un comentario de línea
let x = 10; // Comentario al final de la línea

/*
 Esto es un comentario de bloque
 Puede abarcar varias líneas
*/
let y = 20;

/**
 * Suma dos números
 * @param {number} a - El primer número
 * @param {number} b - El segundo número
 * @returns {number} - La suma de a y b
 */
function sum(a, b) {
  return a + b;
}


// ------------------------- VARIABLES Y CONSTANTES ------------------------- //

// Let
let age: number = 25;
age = 30; // OK, ya que 'let' permite reasignación

// Var
/**
 * var también se usa para declarar variables, pero tiene un ámbito global o de
 * función (function scope), lo que puede llevar a comportamientos inesperados,
 * por lo que en TypeScript se prefiere el uso de let
 */

var username: string = "Alice";
// OK, 'var' también permite reasignación, pero su uso es menos recomendable
username = "Bob"; 

// Const
const PI: number = 3.1416;
// PI = 3.15; // Error: no se puede reasignar una constante

// Plus: Inferir tipos
let city = "Madrid"; // TypeScript infiere que 'city' es de tipo 'string'
// TypeScript infiere que 'numberOfPlanets' es de tipo 'number'
const numberOfPlanets = 8; 


// ---------------------------- DATOS PRIMITIVOS ---------------------------- //
// Y datos no estrictamente primitivos pero valen la pena mencionarlos para TS)

// number
let myAge: number = 25; 

// string
let myName: string = "John"; 

// boolean
let isActive: boolean = true; 

// null
let value: null = null; 

// undefined
let notAssigned: undefined = undefined; 

/*
  Array
  Ambas formas son equivalentes en términos de funcionalidad, varían en estilo:
  
  1. `number[]`: Es más concisa y comúnmente usada por simplicidad y legibilidad
  2. `Array<number>`: Usa sintaxis genérica, útil para casos más complejos o 
     cuando se trabaja con programación genérica (ej. arrays multidimensionales)

  Elección:
  - Para arreglos simples, como `number[]`, se prefiere la notación simplificada
  - En tipos de datos más complejos, `Array<T>`, puede ofrecer mayor claridad
  
  No hay una forma "más correcta", la elección depende de las convenciones de
  estilo del proyecto y del equipo.
*/

let numbers: Array<number> = [1, 2, 3];
let numbers2: number[] = [1, 2, 3];

let strings: Array<string> = ["a", "b", "c"];
let strings2: string[] = ["a", "b", "c"];

// Object
let obj: object = { key: "value" };

// Tupla
let tuple: [number, string] = [25, "John"];

// Enum
enum Color {
  Red,
  Green,
  Blue
}
let c: Color = Color.Green;

// Union
let id: number | string;
id = 10;  // OK
id = "ABC123";  // OK

// Literales
let direction: "up" | "down";
direction = "up"; // OK
// direction = "left"; // Error

// Any (Desactiva la verificación de tipos. Útil cuando no se conoce el tipo)
let randomAnyValue: any = "Hello";
randomAnyValue = 10;  // OK

// Void (Se utiliza principalmente en funciones que no devuelven un valor)
function logMessage(message: string): void {
  console.log(message);
}

// Never (Representa el tipo de valores que nunca ocurren)
// útil para funciones que nunca terminan o que siempre lanzan errores
function throwError(message: string): never { 
  throw new Error(message);
}

// Interface
interface Person {
  name: string;
  age: number;
}
let employee: Person = { name: "Bob", age: 25 };

// Personalizados (Permiten crear alias para un tipo o una combinación de tipos)
type ID = number | string;
let userId: ID = 123;

// Functions (Se pueden tipar tanto los parámetros como el valor de retorno)
function add(a: number, b: number): number {
  return a + b;
}

// Symbol
let sym1: symbol = Symbol();
let sym2: symbol = Symbol("description");

/* 
  Unknown 
   Es un tipo seguro que se usa cuando no sabemos de antemano cuál será el tipo
   de una variable. A diferencia de any, no se pueden realizar operaciones
   sobre un valor unknown sin verificar su tipo primero.
*/
let randomUnknownValue: unknown = "Hello";
if (typeof randomUnknownValue === "string") {
  console.log(randomUnknownValue.toUpperCase()); // OK
}

/* 
  BigInt
  Es un tipo de dato que representa números enteros muy grandes, mayores de lo
  que puede manejar el tipo number.
  Los valores de tipo bigint se crean añadiendo una n al final de un número
  entero o usando el constructor BigInt().
*/
  let bigNumber: bigint = 9007199254740n; // Usando 'n'
  let anotherBigNumber: bigint = BigInt(9007199254740); // Usando el constructor


  // ------------------------- IMPRIMIR POR CONSOLA ------------------------- //
let language = 'TypeScript';
console.log(`Hola ${language}`);