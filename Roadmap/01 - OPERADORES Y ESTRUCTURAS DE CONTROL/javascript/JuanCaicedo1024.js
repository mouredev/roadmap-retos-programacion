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
 * 
 */

let a = 1;
let b = 2;

//incrementar 
a ++
b++

//operadores Aritméticos 
console.log (`suma:${a + b}`);
console.log (`resta:${a - b}`);
console.log (`Multiplicacion:${a * b}`);
console.log (`divions:${a / b}`);
console.log (`modulo:${a % b}`);
console.log (`Exponente:${a ** b}`);

// Operadores logicos 
console.log (`And ${a == b & b == a}`)
console.log (`Or ${a == b || b == a}`)
console.log (`Or ${ a!=b }`)

//Operadores de comparacion 
console.log (`Igual ${a == b }`)
console.log (`Mayor ${a > b }`)
console.log (`Menor ${a < b }`)
console.log (`Mayor y igual ${a >= b }`)
console.log (`menor y igual ${a <= b }`)
console.log (`desigual ${a != b }`)

//Operadores de asignacion 
var X = 20

console.log(`Asigancion ${X = 10}`)
console.log(`Asignación de adición	 ${X += 10}`)
console.log(`Asignación de resta ${X -= 10}`)
console.log(`Asignación de multiplicación	 ${X *= 10}`)
console.log(`Asigancion de division ${X %= 10}`)


// Operadores de Cadena 

let nombre = "Joaquin"
let apellido = "Lopez"
let nombreCompleto = "Joaquin" + " " + "Lopez"

console.log('Nombre Completo:', nombreCompleto);


//Identidad var num = 0;
var obj = new String("0");
var str = "0";
var Xwwww = false;

console.log(num === num); // true
console.log(obj === obj); // true
console.log(str === str); // true

console.log(num === obj); // false
console.log(num === str); // false
console.log(obj === str); // false
console.log(null === undefined); // false
console.log(obj === null); // false
console.log(obj === undefined); // false

// estructura de control condicional

const namePerson = "ha";

if (namePerson == "Jeffrey") {
  console.log("El nombre es Jeffrey");
} else if (namePerson == "Josue") {
  console.log("El nombre es Josue");
} else {
  console.log("El mombre no es Jeffrey ni Josue ");
}

const interruptor = 3;
switch (interruptor) {
  case 0:
    console.log("El bombillo esta en off");
    break;
  case 1:
    console.log("El bombillio esta on");
    break;
  default:
    console.log("Ya no funciona");
    break;
}

// iterativas

for (let i = 0; i <= 10; i++) {
  console.log(i);
}

console.log(`Estructura con while`);
let i = 0;
while (i <= 10) {
  console.log(i);
  i++;
}


// */DIFICULTAD EXTRA (opcional):
//  * Crea un programa que imprima por consola todos los números comprendidos
//  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//  *
//  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo./*

for (let i= 10 ; i <= 55 ; i += 2) {
    if (i === 16 || i %3 === 0 ){
        continues
    }
    console.log(i);
}