// Operadores Aritméticos
let suma = 1 + 1;
let resta = 1 - 1;
let multi = 1 * 1;
let division = 1 / 1;
let modulo = 10 % 3;
let exponente = 4 ** 2;
let leftShift = 5 << 2;
let rightShift = 5 >> 2;
let rightShiftNoSign = 5 >>> 2;
let andBit = 5 & 4;


let incremento = suma++;
let decremento = resta--;

// Operadores de asignación
let normal = 1;
suma += 1;
resta -= 1;
multi *= 1;
division /= 1;
modulo %= 1;
exponente **= 2;
leftShift <<= 2;
rightShift >>= 1;
rightShiftNoSign >>>= 1;
andBit &= 3;
normal &&= 5;
normal ||= 3;
normal ??= 2;

// Operadores de comparación
let mayorQue = 5 > 1;
let menorQue = 5 < 1;
let mayorOIgualQue = 5 >= 1;
let menorOIgualQue = 5 <= 1;
let iguales = 5 === '5';
let igualesNoEsticto = 5 == '5';
let desigual = 5 != '5';
let desigualEstricto = 5 !== '5';

// Estructuras de control: CONDICIONALES

// IF ELSE IF ELSE
let variable = 1;
if (variable) {
    console.log(1);
} else if (variable) {
    console.log(2);
} else {
    console.log(0);
}

// OPERADOR TERNARIO
let nuevaVar = variable > 1 ? console.log('es mayor que uno') : console.log('es menor que uno');;

// SWITCH
switch(variable) {
    case 1:
        console.log('switch dice que es 1');
        break;
    case 2:
        console.log('switch dice que es 2');
        break;
    default:
        console.log('no hay concidencias');
        break;
}

// Estructuras de control: BUCLES

// FOR
for (let i = 1; i <= 10; i++) {
    console.log('FOR - i es ', i);
}

// WHILE
let i = 1;
while (i <= 10) {
    console.log('WHILE - i es ', i);
    i++;
}

// DO WHILE
let j = 1;
do {
    console.log('DO WHILE - j es ', j);
    j++;
} while (j <= 10);

// FOR OF
let array = ['apple', 'banana', 'mango'];

for (fruta of array) {
    console.log('la fruta del momento es ', fruta);
}

// FOR IN
let grace = {
    genero: 'f',
    edad: 25,
    carrera: 'medicina',
    hobbies: ['escalada', 'repostería', 'bucear'],
    mascota: 'Loki'
}

for (prop in grace) {
    console.log('Props de Grace', prop);
}

// Estructuras de control: MANEJO DE ERRORES

try {
    let x = y;
} catch (error) {
    console.log(`Ha ocurrido el siguiente error: ${error}`);
} finally {
    console.log('Acabas de intentar ejecutar un código con errores pero el catch te ha salvado');
}

/**
 * Resumen de estructuras de control en JavaScript:
 * Condicionales: if, else if, else, switch, operador ternario.
 * Bucles: for, while, do...while, for...of, for...in.
 * Manejo de excepciones: try...catch...finally, throw.
 * Control de flujo: break, continue.
 * Declaraciones de salto: return y throw.
 */

/* DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

const programa = () => {
    for (let i = 10; i <= 55; i++) {
        if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
            console.log(i);
        }
    }
}

programa();