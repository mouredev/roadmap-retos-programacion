//Url del lenguaje: https://developer.mozilla.org/es/docs/Web/JavaScript
// Soy un comentario
/* Soy un comentario 
   Soy un comentario */
let Variable1 = 'Hola'; // let es una variable local
var Variable2 = 'Mundo'; // var es una variable global
z = 1; // z es una variable global
// const no se puede cambiar a diferencia de let y var
const Varible3 = 'JavaScript';

let number = 4; // Number es un tipo de dato primitivo que representa un número entero o decimal positivo o negativo con una precisión de 64 bits
let string = 'Hola mundo'; // String es un tipo de dato primitivo que representa una secuencia de caracteres.
let boolean = true; // Boolean es un tipo de dato primitivo que representa un valor lógico verdadero o falso
let Null = null; // Null es un tipo de dato primitivo que representa un valor nulo.
let undefined = undefined; // Undefined es un tipo de dato primitivo que representa un valor no definido
let Bigint = BigInt(10n); // BigInt es un tipo de dato primitivo que representa un número entero mayor que 2^53 - 1 o menor que -2^53 + 1
let Symbol = Symbol('Hola'); // Symbol es un tipo de dato primitivo que representa un valor único e inmutable que puede ser utilizado como clave de una propiedad de un objeto.
let Object = {
  // Object es un tipo de dato primitivo que representa un objeto que contiene una colección de pares de clave-valor
  name: 'Brayan',
  age: 20,
};

let Array = [1, 2, 3, 4, 5]; // Array es un tipo de dato primitivo que representa una lista ordenada de elementos que pueden ser de cualquier tipo de dato

let Function = function () {
  // Function es un tipo de dato primitivo que representa una función
  console.log('Hola JavaScript');
};

console.log('¡Hola, JavaScript!');
