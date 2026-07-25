//EJERCICIOS:

//1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:

// Aritméticos (+, -, *, /, %, etc.):

console.log("Aritméticos:");

const suma = 10 + 20;
console.log(suma);

const resta = 20 - 10;
console.log(resta);

const multiplicacion = 10 * 20;
console.log(multiplicacion);

const exponenciacion = 10 ** 20;
console.log(exponenciacion);

const división = 10 / 20;
console.log(división);

const modulo = 10 % 20;
console.log(modulo);


// Lógicos (!, &&, ||)
console.log("Lógicos:");

// AND

let and = 10 + 3 === 13 && 5 - 1 === 4;
console.log("AND &&: 10 + 3 === 13 and 5 - 1 === 4 es:", and);

//OR
let or = 10 + 3 === 13 || 5 - 1 === 4;
console.log("OR ||: 10 + 3 === 13 or 5 - 1 === 4 es:", or);

//NOT
let not = !(10 + 3 === 13);
console.log("NOT !: 10 + 3=== 13 es:", not);



// De comparación (==, ===, !=, !==, >, <, >=, <=)
console.log("De comparación:");

const igualdadTipoValor = 10 === 10; //igual valor y tipo, true or false
console.log("Igualdad: ", igualdadTipoValor);

const desigualdadTipoValor = 10!== 10; // desigual valor y tipo
console.log("Desigualdad: ", desigualdadTipoValor);

const igualdad = 10 == 10; // igual
console.log("Igualdad: ", igualdad);

const desigualdad = 10 != 10; // desigual
console.log("Desigualdad: ", desigualdad);

const mayor = 12 > 10;
console.log("Mayor: ", mayor);

const mayorOigual = 12 >= 10;
console.log("Mayor o igual: ", mayorOigual);

const menor = 12 < 10;
console.log("Menor: ", menor);

const menorOigual = 12 <= 10;
console.log("Menor o igual: ", menorOigual);



// Asignación (=, +=, -=, *=, /=, etc.)
console.log("Asignación:");
let a = 10;
console.log("= ", a);

a += 5; //añade 5 a la variable a
console.log("= ", a);

let x = 50;
x -= 5; //sustrae 5 a la variable x
console.log("= ", x);

let y = 500;
y *= 5; //multiplica 5 a la variable y
console.log("= ", y);

let z = 600;
z /= 5; //divide 5 a la variable z
console.log("= ", z);

let w = 600;
w %= 5; //asigna un resto/módulo a la variable w: w tiene como valor el resto, que es 0.
console.log("= ", w);

x <<= y; // Asignación de desplazamiento a la izquierda: x = x << y
x >>= y; // Asignación de desplazamiento a la derecha: x = x >> y
x >>>= y; // Asignación de desplazamiento a la derecha sin signo: x = x >>> y
x &= y; // Asignación AND bit a bit: x = x & y
x ^= y; // Asignación XOR bit a bit
x |= y; // Asignación OR bit a bit: x = x | y
x && y; // Asignación AND lógico: x && (x = y)
x ||= y; // Asignación OR lógico: x || (x = y)
x ??= y; // Asignación de anulación lógica: x ?? (x = y)


//Bitwise (&, |, ^, ~, <<, >>)
console.log("Bitwise:");
// a & x; // AND a nivel de bits
// a | x; // OR a nivel de bits
// a ^ x; // XOR a nivel de bits
// ~ a; // NOT a nivel de bits
// a << x; // Desplazamiento a la izquierda
// a >> x; // Desplazamiento a la derecha de propagación de signo
// a >>> x; // Desplazamiento a la derecha de relleno de cero

let e = 5;
let b = 3;

console.log("Value of e:", e);
console.log("Value of b:", b);


let resultAnd = e & b;
let resultOr = e | b;
let resultXor = e ^ b;

console.log("e & b =", resultAnd);
console.log("e | b =", resultOr);
console.log("e ^ b =", resultXor);

// Print NOT operation
console.log("~5 =", ~e);

// Print shift operations
console.log("e << 1 =", e << 1);
console.log("b >> 1 =", b >> 1);
console.log("5 >>> 2 =", 5 >>> 2);


//Ternary operator (?)
let height = 1.50;
var status = height >= 1.50 ? "Tall enough to ride" : "Too short to ride";
 


// 2 . Utilizando las operaciones con operadores que tú quieras, crea ejemplos
//  que representen todos los tipos de estructuras de control que existan
//  en tu lenguaje:

//  Condicionales:

console.log("Condicionales:");

const myString = "raquelLoresDev";

if (myString === "raquelLoresDev") {
    console.log("Strings are equal");
} else if (myString === "raquel") {
    console.log("My string is 'raquel'");
} else {
    console.log("Strings are not equal and it is not 'raquel'");
}


//  Iterativas:
console.log("Iterativas (bucle for y while):");

for (let i = 0; i < 10; i++) {
    console.log(i);
}

let i = 0;
while (i < 10) {
    console.log(i);
    i++;
} 


//  Manejo de excepciones o errores:
console.log("Manejo de excepciones o errores:");

try {
    throw new Error("Error");
} catch (error) {
    console.log(error);
} finally {
    console.log("Finalizado el manejo de excepciones");
}     



// Dificultad EXTRA (opcional):
console.log("Dificultad EXTRA:");
//  * Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.


for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && !(i % 3)) {
    console.log(i);
    if (i === 54) { // Condición para parar el bucle
      break;
    }
  }
}



