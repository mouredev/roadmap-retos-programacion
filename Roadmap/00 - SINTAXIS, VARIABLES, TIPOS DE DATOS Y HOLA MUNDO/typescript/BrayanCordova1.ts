//Url del lenguaje: https://www.typescriptlang.org/docs/
// Soy un comentario
/* Soy un comentario
   Soy un comentario */
/** Soy un Comentario
 * Soy un comentario
 * Soy un comentario
 */
let myVariable1: String = 'Hola'; // let es una variable local
var myVariable2: String = 'Mundo'; // var es una variable global
// const no se puede cambiar a diferencia de let y var
const myVariable3: String = 'Typescript';

let myNumber: number = 4; // Number es un tipo de dato primitivo que representa un número entero o decimal positivo o negativo con una precisión de 64 bits
let myString: string = 'Hola mundo'; // String es un tipo de dato primitivo que representa una secuencia de caracteres.
let myBoolean: boolean = true; // Boolean es un tipo de dato primitivo que representa un valor lógico verdadero o falso
let myNull: null = null; // Null es un tipo de dato primitivo que representa un valor nulo.
let myUndefined: undefined = undefined; // Undefined es un tipo de dato primitivo que representa un valor no definido
let myBigint: bigint = BigInt(10n); // BigInt es un tipo de dato primitivo que representa un número entero mayor que 2^53 - 1 o menor que -2^53 + 1
let mySymbol: symbol = Symbol('Hola'); // Symbol es un tipo de dato primitivo que representa un valor único e inmutable que puede ser utilizado como clave de una propiedad de un objeto.
let myObject: object = {
  // Object es un tipo de dato primitivo que representa un objeto que contiene una colección de pares de clave-valor
  name: 'Brayan',
  age: 20,
};

let myArray: Array<number | string> = [1, 2, 3, 4, 5, 'hola', 'a']; // Array es un tipo de dato primitivo que representa una lista ordenada de elementos que pueden ser de cualquier tipo de dato

function myFunction(): string {
  // Function es un tipo de dato primitivo que representa una función
  return 'Hola Typescript';
}

console.log('¡Hola, Typescript!');
