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

// EJERCICIO:
let a = 1;
let b = 1;
let c = 1;


//Operadores aritmeticos

let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;
let modulo = a % c;
let exponente2 = a **2;

//Operadores de comparacion

console.log(a == b);//comprobacion de igualdad
console.log(a != b); //comprobacion de desigualdad
console.log(a > b); //comprobacion de q es mayor
console.log(a < b); //comprobacion de q es menor
console.log(a >= b); //comprobacion de q es mayor igual
console.log(a <= b); //comprobacion de q es menor igual

//operadores logicos
console.log("logica 1 " + (10 + 3 == 13 && 5 - 1 == 4));
console.log("logica 2 " + (10 + 3 == 14 || 5 - 1 == 4));
console.log("logica 3 " + (10 + 3 != 14 ));

//operadores de asignacion

let myNumber = 11;

myNumber += 1;
myNumber -= 1;
myNumber *= 1;
myNumber /= 1;
myNumber %= 1;
myNumber **= 1;

//Operadores de identidad

let myNewNumber = myNumber;
console.log(myNumber == myNewNumber);
console.log(myNumber != myNewNumber);

//Operadores de pertenencia
let string = "estos es un string"
console.log(string.includes('e'));

//Operadores de bit
let num1 = 10;
let num2 = 3;

console.log("and: "+ (num1 & num2));
console.log("or: "+ (num1 | num2));
console.log("xor: "+ (num1 ^ num2));

//Estructuras de control

//condicionales

let edad = 18;
if (edad >=18) {
    console.log("podes manejar");
}else{
    console.log("no podes manejar");
}

// iterativas

for (let i = 0; i < 11 ; i++) {
    console.log(i);;
}

//dificultad extra

for (let num = 10; num < 56; num++) {
    if (num % 2 == 0 &&
        num !== 16 &&
        num %3 !== 0
        ) {
        console.log(num);
    }
}