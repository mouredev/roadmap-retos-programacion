// Operadores de asignación
let x = 10; // Asignación
x += 5; // Suma y asignación
x -= 5; // Resta y asignación
x *= 5; // Multiplicación y asignación
x /= 5; // División y asignación
x %= 5; // Módulo y asignación

// Operadores aritméticos
let y = 2; // Asignación
const sum = x + y; // Suma
const rest = x - y; // Resta
const multi = x * y; // Multiplicación
const division = x / y; // División
const module = x % y; // Módulo
const exponent = x ** y; // Exponente

console.log("console log Raquel ~ sum:", sum);
console.log("console log Raquel ~ rest:", rest);
console.log("console log Raquel ~ multi:", multi);
console.log("console log Raquel ~ division:", division);
console.log("console log Raquel ~ module:", module);
console.log("console log Raquel ~ exponent:", exponent);

// Operadores de comparación
const equals = x == y; // Igual
const notEquals = x !== y; // Desigual
const extrictEqual = x === y; // Igual estricto
const extrictNotEqual = x !== y; // Desigual estricto
const greaterThan = x > y; // Mayor qué
const greaterThanOrEqual = x >= y; // Mayor o igual qué
const lessThan = x < y; // Menor qué
const isLessThanOrEqual = x <= y; // Menor o igual qué

console.log("console log Raquel ~ equals:", equals);
console.log("console log Raquel ~ notEquals:", notEquals);
console.log("console log Raquel ~ extrictEqual:", extrictEqual);
console.log("console log Raquel ~ extrictNotEqual:", extrictNotEqual);
console.log("console log Raquel ~ greaterThan:", greaterThan);
console.log("console log Raquel ~ greaterThanOrEqual:", greaterThanOrEqual);
console.log("console log Raquel ~ lessThan:", lessThan);
console.log("console log Raquel ~ isLessThanOrEqual:", isLessThanOrEqual);

// Operadores lógicos
const and = x < 5 && y < 5; // Y
const or = x || y; // O
const nullish = x ?? y; // Nullish

// Estructuras de control

// If-else
if (x != y) {
  console.log("x no es igual a y");
} else {
  console.log("x es igual a y");
}

// Ternario
x === 5 ? "x es igual a 5" : "x no es igual a 5";

// Switch
switch (x) {
  case 1:
    console.log("x es igual a 1");
    break;
  case 2:
    console.log("x es igual a 2");
    break;
  default:
    console.log("x no es igual a 1 ni 2");
    break;
}

// For loop
for (let i = 0; i < 10; i++) {
  console.log("i vale: " + i);
}

// While
while (x != 5) {
  let i = 0;
  console.log("x vale: " + x);
  i++;
}

// Do... while
let doWhile = 0;
do {
  console.log("Ejecutanto...");
  doWhile++;
} while (doWhile != 5);

// For... in
let countries = { Spain, Portugal, Germany };
for (let key in countries) {
  console.log("País: " + countries[key]);
}

// Try catch
try {
  let result = 20 / 5;
  console.log("The result is: ", result);
} catch (error) {
  console.error("Error: " + error.message);
}

// Throw
function divider(a, b) {
  if (b === 0) {
    throw new Error("Can't divide by zero");
  }
  return a / b;
}

// Extra optional
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 === 0) {
    console.log(i);
  }
}
