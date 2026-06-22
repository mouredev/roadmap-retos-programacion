/*EJERCICIO:
  Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
*/

let a = 2;
let b = 5;
let c = "5";

// Aritméticos

console.log("Suma = ", a + b)
console.log("Resta = ", a - b)
console.log("División = ", a / b)
console.log("multiplicación = ", a * b)
console.log("Resto = ", a % b)

// De comparación

console.log("Mayor que = ", b > a)
console.log("Menor que = ", b < a)
console.log("Mayor igual = ", b >= a)
console.log("Menor igual = ", b <= a)
console.log("Igual = ", b == c) // Compara solo el valor
console.log("Estrictamente igual = ", b === c) // Compara valor y tipo de dato
console.log("Distinto = ", b != c) // Compara solo el valor
console.log("Estrictamente Distinto = ", b !== c) // Compara valor y tipo de dato

//Lógicos

let d = true;
let e = false;

console.log("AND = ", d && e)
console.log("OR = ", d || e)
console.log("NOT = ", !d)
console.log("NOT = ", !e)

// Asignación

let num = 10

num += 5; // 15
num -= 5; // 5
num *= 5; // 50
num /= 5; // 2
num %= 5; // 0

console.log(num);


/*Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
    Debes hacer print por consola del resultado de todos los ejemplos.
*/

