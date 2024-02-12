// #01 OPERADORES Y ESTRUCTURAS DE CONTROL
// #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

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

//****************************************************** */
// OPERADORES ARITMÉTICOS CON NÚMEROS (+, -, *, /, %, **)
//****************************************************** */

const a: number = 2; // operando
const b: number = 4; // operando

// Suma
let resultado_suma: number = a + b; // operador binario

console.log(resultado_suma);

// Resta
let resultado_resta: number = a - b;

console.log(resultado_resta);

// Multiplicación
let resultado_multiplicacion: number = a * b;

console.log(resultado_multiplicacion);

// Division
let resultado_division: number = a / b;

console.log(resultado_division);

// Resto (remainder)

let resultado_resto = a % b;

console.log(resultado_resto);

// Exponenciación
let resultado_expo = a ** b;

console.log(resultado_expo);

//****************************************************** */
// OPERADORES ARITMÉTICOS CON CADENAS
//****************************************************** */

// Suma cadena de números

const numA: string = "2";
const numB: string = "4";

let concatena_num = numA + numB;
console.log(concatena_num); // No suma 8, sinó que concatena los números 2 y 4 (24).

// Suma cadenas

const palabra1: string = "Hola";
const palabra2: string = " mundo!";

let concatena_str = palabra1 + palabra2;
console.log(concatena_str);

// El operador de suma (+), aplicado delante de un único operando, cambia su tipo a número.

console.log(typeof numA); // Mantiene el tipo string
console.log(typeof +numA); // Cambia el tipo de string a number

// Tabla de Precedència de los operadores

//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence

// Assignación
const numC = 4;

// Modificación in situ
let euros: number = 1;
euros += 4;
console.log(euros);

//****************************************************** */
// OPERADORES COMPARACIÓN
//****************************************************** */

// ==
const check = numA == "2";
console.log("comparacion: " + check); // true;

// ===
const check_extricto = numA === 2;
console.log("comparacion: " + check_extricto); // false;

// !=
const check01 = numA != "2";
console.log("comparacion: " + check01); // false;

// !===
const check_extricto01 = numA !== "2";
console.log("comparacion: " + check_extricto01); // false;
// <
a < b;
// >
a > b;
// <=
a <= b;
// >=
a >= b;

//****************************************************** */
// OPERADORES LÓGICOS
//****************************************************** */

// OR
let aficion = "surf" || "tenis";

// AND
let juegos = "tetris" && "pong";

// !(NOT)

let result = !true; // false;

//****************************************************** */
// ESTRUCTURAS DE CONTROL
//****************************************************** */

// Condicional

const misCoches = ["Ferrari", "BMW", "Porche"];

// if
if (misCoches) {
  console.log("Tengo coches");
} else {
  console.log("No tengo coches");
}

// switch
let comprado = 1;
switch (misCoches[comprado]) {
  case "Ferrari":
    console.log("Has comprado un Ferrari!");
    break;
  case "BMW":
    console.log("Has comprado un BMW!");
    break;
  case "Porche":
    console.log("Has comprado un Porche!");
    break;

  default:
    console.log("Tienes un coche de baratija...");
    break;
}

// Iterativas

// for
for (let index = 0; index < misCoches.length; index++) {
  const coche = misCoches[index];
  console.log(coche);
}

// forOf
for (const coche of misCoches) {
  console.log(coche);
}

// forEach
misCoches.forEach((coche) => {
  console.log(coche);
});

// while
/* let vida: number = 100;
while (vida >= 50) {
  //console.log("Sigues jugando desde while.");
} */

// do while
/* do {
console.log("Sigues jugando desde do while.");
} while (vida >= 50); */

// Excepciones
try {
  // Alguna lógica.
} catch (error: unknown) {
  if (error instanceof Error) {
    console.log("instanceof: " + error.stack);
  } else if (error && typeof error === "object" && "message" in error) {
    console.log("object: " + String(error.message));
  } else if (typeof error === "string") {
    console.log("string: " + error);
  } else {
    console.log("default error message");
  }
}

//****************************************************** */
// EJERCICIO EXTRA
//****************************************************** */

function numeros_comprendidos(min: number, max: number): void {
  for (let num = min; num <= max; num++) {
    if (num % 2 == 0 && num != 16 && num % 3 != 0) {
      console.log(num);
    }
  }
}

numeros_comprendidos(10, 55);
