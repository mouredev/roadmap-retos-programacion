/*
 * EJERCICIO:
 * 1- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
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


//Aritmeticos

let valor1 = 5;
let valor2 = 8;
let valor3 = 12;

let suma = valor2 + valor3;
let resta = valor3 - valor1;
let multiplicar = valor1 * valor2;
let dividir = valor3 / valor1;
let modulo = valor3 % valor2;
let exponencial = valor1 ** valor2;

console.log(suma);
console.log(resta);
console.log(multiplicar);
console.log(dividir);
console.log(modulo);
console.log(exponencial);


//Logicas
let a = 4
let b = 8

let and = (a > 2) && (b > 2);
let or = (a > 5) || (b > 5);

console.log(and);
console.log(or);


//Comparación
let c = 2
let d = 5

if (c >= d){
    console.log(c + " es mayor o igual que " + d)       
    }else {
        console.log(c + " es menor que " + d);       
    };  


//Operador de concatenación 
let name = "John";
let lastName = "Connor";
let fullName = name + " " + lastName;
console.log(fullName);


//Condicionales
let e = 7
let f = 3
if (e > f){
    console.log("it's large than");  
}


//Ternario
let age = 20
let message = (age >= 18) ? "you are adult" : "Under age";
console.log(message);


//Switch es para evaluar una expresión y ejecute el bloque de codigo correspondiente al valor que coincide
let days = 6 //Saturday

switch (days) {
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    case 4:
        console.log("Thursday");
        break;
    case 5:
        console.log("Friday");
        break;
    case 6:
        console.log("Saturday");
        break;
    case 7: 
        console.log("Sunday");
        break;
    default:
        console.log("number to day invalid");
}


//Manejo de excepcion
try {
    let multiplicacion = 8 * 4;
    console.log("El resultado es: " + multiplicacion);
} catch (error) {
    console.log("Se ha producido un error: " + error.message);
}


//Ejercicio extra
for (let i = 10; i <= 55; i++){
    if(i % 2 === 0 && i !== 16 && i % 3 !== 0)
    console.log(i); 
}