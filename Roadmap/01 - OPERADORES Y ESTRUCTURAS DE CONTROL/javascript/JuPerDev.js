/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// Assignment

let cohete = '🚀';

// Arithmetics Operators
let add = 1 + 2; // 3
let substract = 5-3; // 2
let multiply = 2*2; // 4
let division = 4/2; // 2
let modulus = 8%2; // 0

let increment = 0;
++increment; // 1

let decrement = 5;
--decrement; //4

// Comparison Operators
let greaterThan = 5 > 1; // True
let lessThan = 1 < 5; // True
let greaterThanOrEqualTo = 3 >= 3; // True
let lessThanOrEqualTo = 1 <= 2; // True
let notEqual = 1 != '2'; // true
let notEqualValueOrType = 2 !== '2'; // true 
let equalValue = 2 === '2'; // true
let equalValueAndEqualType = 2 === '2'; //false
let ternaryOperator = (1 > 0) ? 'True':'false'; // true

// Logical Operators
// And &&
let andOne = true && true // true
let andTwo = true && false // false
// Or ||
let orOne = true || true // true
let orTwo = true || false //true
let orThree = false || false //false
// Denial
console.log(!true); // false

// Type Operators
typeof 'Juan'; // String
typeof 4; // Number
typeof NaN; // Number
typeof true; // Boolean
typeof [1,1,2,3]; // Object
typeof {name:'juan', lastName: 'Perez'}; // Object
typeof new Date(); // Object
typeof function hola(){}; // Function 
typeof varTest; // Undefined
typeof null; // Object

// Conditional Assignment

// IF, ELSE, IF ELSE
if(true){
    console.log('true');
} else if(false){
    console.log('false')
} else {
    console.log('Else')
}

// Switch
let variable = 2;
switch (variable){
    case 1:
        console.log('Monday')
        break
    case 2:
        console.log('Tuesday')
        break
    case 3:
        console.log('Wednesday')
        break
    default:
        console.log('Hola :D!')
}

// for

for(let i = 0; i < 5; i++){
    console.log(i);
}

// for in
const object = { name: 'Juan', lastName: 'Pérez'};
for (let i in object){
    console.log(object[i])
}

// for of
const array = ['Juan', 'Pedro', 'Javier'];
for(let i of array){
    console.log(i);
}

// while
let x = 0;
while( x <= 3 ){
    console.log(`While -> ${x}`);
    x++;
}

// do-while
let d = 0;
do{
    console.log(`do-while --> ${d}`);
    d++;
}while(d <= 5);

// EXTRA
/*
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for(let i = 10; i <= 55; i++){
    if(i%2 === 0 && i%3 !== 0 && i !== 16){
        console.log(i)
    }
}