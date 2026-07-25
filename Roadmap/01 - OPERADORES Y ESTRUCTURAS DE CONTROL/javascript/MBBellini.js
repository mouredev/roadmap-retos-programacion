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

let numInt = 8; 
let numFloat = 5.870;

// Operadores aritméticos 
let num1 = 4;  
let num2 = 10;
let suma = num1 + num2;        
let resta = num2 - num1;
let multiplicar = num1 * num2;
let division = num2 / num1;
let modulo = num2 % num1;
let exponencial = num2 ** num1;

console.log(suma);
console.log(resta);
console.log(multiplicar);
console.log(division);
console.log(modulo);
console.log(exponencial);


//operadores lógicos 
let l = 8;
let k = 10;
let j = 3;

let and = (l > 5) && (k > 7)
let or = (l < 5) || (j < 10)

console.log(and);
console.log(or);


//operador de comparación 
let a = 5;
let b = 10;

if (a >= b){
    console.log(a + " es mayor o igual que " + b)       
    }else {
        console.log(a + " es menor que " + b);       
    };  



//Operador de concatenación 
let name = "Jane";
let lastName = "Doe";
let fullName = name + " " + lastName;
console.log(fullName);


//Condicionales
var c = 7
var d = 3
if (c > d){
    console.log("it's large than");  
}


//Ternario
let age = 21
let message = (age >= 21) ? "you are adult" : "Under age";
console.log(message);


//Switch es para evaluar una expresión y ejecute el bloque de codigo correspondiente al valor que coincide
let month = 10 //Octubre

switch (month) {
    case 1:
        console.log("January");
        break;
    case 2:
        console.log("February");
        break;
        case 3:
        console.log("March");
        break;
        case 4:
        console.log("April");
        break;
        case 5:
        console.log("May");
        break;
        case 6:
        console.log("June");
        break;
        case 7: 
        console.log("July");
        break;
        case 8:
        console.log("August");
        break;
        case 9:
        console.log("September");
        break;
        case 10:
        console.log("October");
        break;
        case 11:
        console.log("November");
        break;
        case 12:
        console.log("December");
        break
    default:
        console.log("number to month invalid");
}


//Manejo de excepcion
try {
    let division = 12 / 2;
    console.log("El resultado es: " + division);
} catch (error) {
    console.log("Se ha producido un error: " + error.message);
}


//Ejercicio extra
for (let i = 10; i <= 55; i++){
    if(i % 2 === 0 && i !== 16 && i % 3 !== 0)
    console.log(i); 
}