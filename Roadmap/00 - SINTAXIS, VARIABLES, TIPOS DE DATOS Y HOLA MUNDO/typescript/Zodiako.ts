// Oficcial Site https://www.typescriptlang.org/

/**
 * Muchas
 * lineas
 * de
 * comentarios
 */

let myName: string = "Zodiako";
const language: string = "TypeScript";

// Primitive Types
let isBoolean: boolean = true;
let isNumber: number = 123;
let myString: string = "Hello World";
let myUndefined: undefined = undefined;
let myNull: null = null;
let mySymbol: symbol = Symbol("mySymbol");

//Change value primitive
isBoolean = false;
isNumber = 321;
myString = "Bye World";
myUndefined = undefined;
myNull = null;
mySymbol = Symbol("mySymbol");

// Arrays
let myArray: string[] = ["Hello", "World"];
let myNumberArray: number[] = [1, 2, 3, 4, 5];

//object
let myObject: object = { name: "Zodiako", age: 25 };

// Tuple
let myTuple: [string, number] = ["Zodiako", 25];

// Enum
enum Colors {
  Red,
  Green,
  Blue,
}

console.log(`¡Hola, ${language}!`);
