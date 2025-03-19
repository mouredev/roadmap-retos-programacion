let a = 15
let b = 7

//operadores aritméticos
let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;
let modulo = a % b;
let exponente = a ** b;
let raizCuadrada = Math.sqrt(a);
let raizCubica = Math.pow(a, 1/3);

console.log(suma);
console.log(resta);
console.log(multiplicacion);
console.log(division);
console.log(modulo);  // 5

// operadores de comparación

console.log (a == b); // comparador de igualdad
console.log (a === b); // comparador extrictamente igual
console.log (a != b); // comparador de desigualdad
console.log (a > b );// mayor que
console.log (a < b );// menor que
console.log (a >= b); // mayor o igual que
console.log (a <= b); // menor o igual que


// operadores lógicos

console.log(a + b == 22 && 22 > 7); // and &&
console.log((a + b ) > 10 || (a - b) > 30) ;// or ||
console.log(!(a + b == 22));// not !

// operadores de asignación
let c = 6
let d = 4
c = d; // asignación
console.log(c)
c += d; // suma y asignación
console.log(c)
c -= d; // resta y  asignación
console.log(c)
c *= d; // multiplicación y asignación
console.log(c)
c /= d; // división y asignación
console.log(c)
c %= d; // módulo y asignación
console.log(c)
c **= d; //exponente y asignación
console.log(c)


// operadores de bit a bit
console.log(a & b); // AND Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos son unos 
console.log(a | b); // OR Devuelve un cero en cada posición de bit para el cual los bits correspondientes de ambos operandos son ceros.
console.log(a ^ b); // XOR Devuelve un cero en cada posición de bit para la que los bits correspondientes son iguales. [Devuelve uno en cada posición de bit para la que los bits correspondientes son diferentes].
console.log(~a); // NOT Invierte los bits de su operando.
console.log(a << 2); // Desplaza a en representación binaria b bits hacia la izquierda, desplazándose en ceros desde la derecha.
console.log(a >> 2); // Desplaza a en representación binaria b bits a la derecha, descartando los bits desplazados.
console.log(a >>> 2); // Desplaza a en representación binaria b bits hacia la derecha, descartando los bits desplazados y desplazándose en ceros desde la izquierda.



// operadores de cadena
let nombre = "Singular";
let apellido = "Pigeon";
console.log("Singular" + "Pigeon");

let frase = "Super"
frase += "califragilistico"
console.log(frase);

//operador condicional ternario
let x = a > b ? "a es mayor que b" : "a es menor o igual que b";
console.log(x);

// devuelve una cadena que indica el tipo de operando
console.log(typeof 35); // number
console.log(typeof "cadena"); // string

/*
Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */
for ( let i = 10; i <= 55; i++) {
  if ( i % 2 === 0 && i !== 16 && i % 3 !== 0) {
    console.log(i);
    //
  }
   
}

