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

console.log(3 + 4)     // Suma -> 7
console.log(3 - 4)     // Resta -> -1
console.log(3 / 4)     // División -> 0.75
console.log(3 * 4)     // Multiplicación -> 12
console.log(3 % 4)     // Módulo -> 3
console.log(3 ** 4)    // Potencia -> 81


// OPERADORES LÓGICOS

console.log(true && false)     // AND -> false
console.log(true || false)     // OR -> true
console.log(!true)             // NOT -> false


// OPERADORES DE COMPARACIÓN

console.log(3 > 4)     // Mayor que -> false
console.log(3 < 4)     // Menor que -> true
console.log(3 >= 4)    // Mayor o igual que -> false
console.log(3 <= 4)    // Menor o igual que -> true


// OPERADORES DE ASIGNACIÓN

let assignSum: number = 7
assignSum += 3                     // Suma y asignación
console.log(assignSum)             // 10

let assignSubtract: number = 7
assignSubtract -= 4                // Resta y asignación
console.log(assignSubtract)        // 3

let assignMultiplication: number = 7
assignMultiplication *= 2          // Multiplicación y asignación
console.log(assignMultiplication)  // 14

let assignDivision: number = 7
assignDivision /= 2                // División y asignación
console.log(assignDivision)        // 3.5

let assignModule: number = 7
assignModule %= 2                  // Módulo y asignación
console.log(assignModule)          // 1

let assignPow: number = 7
assignPow **= 2                    // Potencia y asignación
console.log(assignPow)             // 49


// OPERADORES DE PERTENENCIA

let arr: number[] = [0, 1, 2, 3, 4];
console.log(3 in arr);      // true
console.log(11 in arr);     // false


// OPERADORES DE BITS

console.log(3 & 4);         // AND -> 0
console.log(3 | 4);         // OR -> 7
console.log(3 ^ 4);         // XOR -> 7
console.log(~3);            // NOT -> -4
console.log(3 << 4);        // Desplazamiento a izquierda -> 48
console.log(3 >> 4);        // Desplazamiento a derecha -> 0


// ESTRUCTURA DE CONTROL: if - else if - else

let score: number = 8;

if (score >= 5) {
    console.log('You have passed the exam!');  // prints this
} else if (score < 5) {
    console.log('You haven\'t passed the exam...');
} else {
    console.log('The scores are not available yet.');
}


// ESTRUCTURA DE CONTROL: switch

let month: number = 6;
let monthName: string = '';

switch (month) {
    case 1:
        monthName = 'January';
        break;
    case 2:
        monthName = 'February';
        break;
    case 3:
        monthName = 'March';
        break;
    case 4:
        monthName = 'April';
        break;
    case 5:
        monthName = 'May';
        break;
    case 6:
        monthName = 'June';
        break;
    case 7:
        monthName = 'July';
        break;
    case 8:
        monthName = 'August';
        break;
    case 9:
        monthName = 'September';
        break;
    case 10:
        monthName = 'October';
        break;
    case 11:
        monthName = 'November';
        break;
    case 12:
        monthName = 'December';
        break;
    default:
        monthName = 'Not a valid month number';
}
console.log(`Month: ${monthName}`);    // Month: June


// ESTRUCTURA DE CONTROL: for

for (let i: number = 0; i < 5; i++) {
    console.log(i);
}
/* Se imprimen los siguientes números:
    0
    1
    2
    3
    4
*/


// ESTRUCTURA DE CONTROL: for-in

type Person = {
    name: string
    username: string
    age: 25
}

const person: Person = {
    name: 'Naia',
    username: 'nlarrea',
    age: 25
};

for (let key in person) {
    // Se imprimen las claves:
    console.log(key);

    // Si quisiéramos imprimir los valores:
    // console.log(person[key]);
}
/* Se imprimen los siguientes strings:
    name
    username
    age
*/


// ESTRUCTURA DE CONTROL: for-of

const numArr: (string | boolean | number | string[])[] = ['hola', true, 7, ['a', 'b', 'c']]

for (let item of numArr) {
    console.log(item);
}
/* Se imprime:
    'hola'
    true
    7
    [ 'a', 'b', 'c' ]
*/


// ESTRUCTURA DE CONTROL: while

let i: number = 0;
while (i < 5) {
    console.log(i);
    i++;
}
/* Se imprimen los siguientes números:
    0
    1
    2
    3
    4
*/


// ESTRUCTURA DE CONTROL: do-while

let j: string = 'Not empty';
do {
    console.log(j);
} while (j === '');
/* Se imprime el mensaje 'Not empty' 1 vez aunque no se cumpla la condición del
while, porque siempre se va a ejecutar aunque sea una vez.

CUIDADO: si la condición del while se cumpliera, sería un bucle infinito
*/


// ESTRUCTURA DE CONTROL: try-catch

try {
    throw new Error('This is an error');
    console.log('This is not printed');
} catch (error) {
    console.log(error);                     // [Error: This is an error]
}


// ESTRUCTURA DE CONTROL: try-catch-finally
try {
    throw new Error('This is an error');
    console.log('This is not printed');
} catch (error) {
    console.log(error);                     // [Error: This is an error]
} finally {
    console.log('This is always printed');  // This is always printed
}


// EJERCICIO EXTRA

/* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

for (let num: number = 10; num <= 55; num++) {
    if (
        num % 2 === 0 &&
        num !== 16 &&
        num % 3 !== 0
    ) {
        console.log(num);
    }
}
/* Se imprimen los siguientes números:
    10 
    14 
    20 
    22 
    26 
    28 
    32 
    34 
    38 
    40 
    44 
    46 
    50 
    52
*/