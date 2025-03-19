// Ejemplos de todos los operadores de Javascript

// Asignación

let a = 1;

// Asignación de suma

a += 1;

// Asignación de resta

a -= 1;

// Asignación de multiplicación

a *= 2;

// Asignación de división

a /= 2;

// Asignación de resto

a %= 2;

// Asignación de exponente

a **= 2;

// Left shift

a <<= 2;

// Right shift

a >>= 2;

// Unsigned right shift

a >>>= 2;

// Asignación BITWISE AND

let b = 5;

b &= 2;

// BITWISE XOR

b ^= 2;

// BITWISE OR

b |= 2;

// Deestructuración

const foo = ["one", "two"];

const one = foo[0];
const two = foo[1];

// Comparación

// Igual

var num1 = 1;

console.log(num1 == 1);

// No igual

console.log(num1 != 1);

// Igual estricto

console.log(num1 === 1);

// No igual estricto

console.log(num1 !== 1);

// Greater than

console.log(num1 > 1);

// Greater than or equal

console.log(num1 >= 1);

// Less than

console.log(num1 < 1);

// Less than or equal

console.log(num1 <= 1);

// ARITMÉTICOS

// Módulo
console.log(12 % 5);

// Incremento

let x = 3

console.log(++x);
console.log(x++);
console.log(x);

// Decremento

let y = 3

console.log(--y);
console.log(y--);
console.log(y);

// Negación unitaria

let z = 3
console.log(-z);

// Suma unitaria (intenta convertir el operando a número)

let num3 = true;

console.log(+num3);

// Concatenación de strings

console.log("Hola" + "mundo");

let myString = "Hola"

console.log(myString += "mundo");

// Condicionales

var age = 18;

const adultOrNot = age >= 18 ? "Adulto" : "Menor"

console.log(adultOrNot);

if (age >= 18) {
    console.log("Adulto");

} else {
    console.log("Menor");

}

// Tipo de variable

console.log(typeof adultOrNot);


// In

const myCar = { make: "Aston Martin", model: "AMR25", year: 2025 };
console.log("make" in myCar);
console.log("color" in myCar);


// Bucle for

for (i = 0; i <= 2; i++) {
    console.log(`Iteración nº ${i}`);
}

// Bucle while

i = 0;

while (i <= 2) {
    console.log(`Iteración nº ${i}`);
    i++;
}

// Manejo de excepciones

try {
    console.log(Hola);

} catch {
    console.log("Se ha producido un error");
} finally {
    console.log("Ha finalizado el manejo de errores");

}


/* DIFICULTAD EXTRA:
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55(incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

for (i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
        console.log(i);
    }
}
































