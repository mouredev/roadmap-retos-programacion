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

// Operadores aritmeticos
let x = 10;
let y = 5;

console.log(`Suma: ${x + y}`);
console.log(`Resta: ${x - y}`);
console.log(`Multiplicacion: ${x * y}`);
console.log(`Division: ${x / y}`);
console.log(`Modulo: ${x % y}`);
console.log(`Potencia: ${x ** y}`);

// Operadores de comparacion
console.log(`Igualdad: ${x == y}`);
console.log(`Estrictamente igual: ${x === y}`);
console.log(`Mayor que ${x > y}`);
console.log(`Menor que ${x < y}`);
console.log(`Mayor o igual que ${x >= y}`);
console.log(`Menor o igual que ${x <= y}`);
console.log(`Distinto: ${x != y}`);

// Operadores de asignacion
let z = 2;
console.log(`Suma: ${(z += 1)}`);
console.log(`Resta: ${(z -= 1)}`);
console.log(`Multiplicacion: ${(z *= 2)}`);
console.log(`Division: ${(z /= 1)}`);
console.log(`Modulo: ${(z %= 3)}`);
console.log(`Potencia: ${(z **= 2)}`);

// Operadores de bit a bit
console.log(`Desplazamiento a la izq: ${(z <<= 8)}`);
console.log(`Desplazamiento a la der: ${(z >>= 3)}`);
console.log(`Desplazamiento a la der sin signo: ${(z >>>= 1)}`);
console.log(`Asignación AND bit a bit ${(x &= y)}`);
console.log(`Asignación XOR bit a bit ${(x ^= y)}`);
console.log(`Asignación OR bit a bit ${(x |= y)}`);
console.log(`Asignación AND lógico ${(x &&= y)}`);
console.log(`Asignación OR lógico ${(x ||= y)}`);
console.log(`Asignación de anulación lógica ${(x ??= y)}`);

// Operadores lógicos

// AND &&
console.log(5 > 10 && 15 > 20); // false
console.log(5 < 10 && 15 > 20); // false
console.log(5 > 10 && 15 < 20); // false
console.log(5 < 10 && 15 < 20); // true

// OR ||
console.log(5 > 10 || 15 > 20); // false
console.log(5 < 10 || 15 > 20); // true
console.log(5 > 10 || 15 < 20); // true
console.log(5 < 10 || 15 < 20); // true

console.log(5 < 10 || (15 < 20 && 30 > 30)); // true

// NOT !
console.log(!(5 > 10 && 15 > 20)); // true
console.log(!(5 > 10 || 15 > 20)); // true

// Operadores ternarios
const isRaining = true;

isRaining ? console.log("Esta lloviendo") : console.log("No esta lloviendo");

// Estructuras de control o condicionales

// if
let myVariable = "Diego";

if (myVariable === "Diego") {
  console.log("Diego");
}

// if else
let number = -2;

if (number > 0) {
  console.log("Numero positivo");
} else {
  console.log("El numero no es positivo");
}

// if else if else
if (number > 0) {
  console.log("Numero positivo");
} else if (number < 0) {
  console.log("Numero negativo");
} else {
  console.log("El numero es cero");
}

// Switch
let lenguage = "it";

switch (lenguage) {
  case "es":
    console.log("hola");
    break;
  case "en":
    console.log("Otoño");
    break;
  case "it":
    console.log("achiao");
  default:
    break;
}

// Estructuras iterativas

// for
for (let i = 0; i < 21; i++) {
  console.log(i);
}

// for of
let myArray = ["Ana", "Carlos", "Lucía", "Pedro", "Marta"];
for (const name of myArray) {
  console.log(name);
}

// for in
let car = {
  color: "red",
  model: "sedan",
  wheels: 4,
};

for (const key in car) {
  if (car.hasOwnProperty.call(car, key)) {
    const element = car[key];
    console.log(key, element);
  }
}

// forEach
myArray.forEach((element) => {
  console.log(element);
});

// while
const word = "arroz";
const lengthWord = word.length;
let result8 = "";
count = 0;
while (count < lengthWord) {
  result8 = result8 + word[lengthWord - 1 - count];
  count++;
}
console.log(result8);

// do while
i = 6
do {
    console.log(`Hola ${i}`)
    i++
} while (i < 5)


// excepciones

// try - catch - finally
let a = 0
try {
  console.log(...a);
} catch (error) {
  console.log(`Error: ${error.message}`);
} finally {
  console.log("Fin de la funcion");
}


/*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*
* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

for (let i = 10; i < 56; i++) {
  if (i % 2 === 0 && i !== 16 && (i % 3 !== 0)) console.log(i) 
}