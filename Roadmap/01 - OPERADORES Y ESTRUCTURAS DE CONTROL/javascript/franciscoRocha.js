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

// OPERADORES ARITMÉTICOS
const suma = 5 + 5;
const resta = 9 - 5;
const multiplicacion = 2 * 5;
const division = 10 / 2;
const modulo = 10 % 3;
console.log("Aritméticos:", suma, resta, multiplicacion, division, modulo);

// OPERADORES LÓGICOS
const and = true && false;
const or = true || false;
const not = !true;
console.log("Lógicos:", and, or, not);

// OPERADORES DE COMPARACIÓN
const igual = 4 == 4;
const diferente = 4 != 5;
const mayor = 5 > 4;
const menor = 4 < 5;
const mayorIgual = 5 >= 4;
const menorIgual = 4 <= 5;
const estricto = 4 === '4';
const noEstricto = 4 !== '4';
console.log("Comparación:", igual, diferente, mayor, menor, mayorIgual, menorIgual, estricto, noEstricto);

// OPERADORES DE ASIGNACIÓN
let x = 5;
x += 9;
x -= 4;
x *= 2;
x /= 3;
x %= 5;
console.log("Asignación:", x);

// OPERADORES DE PERTENENCIA
const persona = { nombre: "Juan", edad: 25 };
console.log("Pertenencia:", "nombre" in persona, "apellido" in persona);

class Animal {}
class Perro extends Animal {}
const dog = new Perro();
console.log("Instanceof:", dog instanceof Perro, dog instanceof Animal, dog instanceof Object, dog instanceof Array);

// OPERADORES DE BITS
let a = 5;   // 00000101
let b = 3;   // 00000011
console.log("Bits:", a & b, a | b, a ^ b, ~a, a << 1, a >> 1, a >>> 1);

// CONDICIONALES
let edad = 18;
if (edad >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}

// SWITCH
let dia = 3;
switch (dia) {
    case 1: console.log("Lunes"); break;
    case 2: console.log("Martes"); break;
    case 3: console.log("Miércoles"); break;
    default: console.log("Día no válido");
}

// BUCLE FOR
for (let i = 1; i <= 5; i++) {
    console.log("Número:", i);
}

// BUCLE WHILE
let contador = 3;
while (contador > 0) {
    console.log("Contador:", contador);
    contador--;
}

// BUCLE DO WHILE
let num = 0;
do {
    console.log("Número en do-while:", num);
    num++;
} while (num < 3);

// ITERANDO UN ARRAY CON forEach
const numeros = [10, 20, 30];
numeros.forEach(num => console.log("forEach:", num));

// USANDO MAP
const dobles = numeros.map(num => num * 2);
console.log("Map:", dobles);

// MANEJO DE EXCEPCIONES
try {
    let resultado = 10 / 0;
    if (!isFinite(resultado)) {
        throw new Error("División por cero detectada");
    }
} catch (error) {
    console.log("Error:", error.message);
} finally {
    console.log("Fin del bloque try-catch");
}

//Crea un programa que imprima por consola todos los números comprendidos
//entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for ( let i = 10; i <= 55; i++){
    if( i % 2 === 0 && i !== 16 && i % 3 !== 0){
        console.log(`${i}`);
    }
}
