

// OPERADORES ARITMÉTICOS

console.log(3 + 4);     // Suma -> 7
console.log(3 - 4);     // Resta -> -1
console.log(3 / 4);     // División -> 0.75
console.log(3 * 4);     // Multiplicación -> 12
console.log(3 % 4);     // Módulo -> 3
console.log(3 ** 4);    // Potencia -> 81


// OPERADORES LÓGICOS

console.log(true && false);     // AND -> false
console.log(true || false);     // OR -> true
console.log(!true);             // NOT -> false


// OPERADORES DE COMPARACIÓN

console.log(3 > 4);     // Mayor que -> false
console.log(3 < 4);     // Menor que -> true
console.log(3 >= 4);    // Mayor o igual que -> false
console.log(3 <= 4);    // Menor o igual que -> true

console.log(3 == '3');  // Igual que -> true
console.log(3 != '3');  // Diferente a -> false
console.log(3 == 4);    // false
console.log(3 != 4);    // true

console.log(3 === '3'); // Igual que (estricta) -> false
console.log(3 !== '3'); // Diferente a (estricta) -> true


// OPERADORES DE ASIGNACIÓN

// OPERADORES DE ASIGNACIÓN

let asignarSuma = 7;
asignarSuma += 3;                     // Suma y asignación
console.log(asignarSuma);             // 10

let asignarResta = 7;
asignarResta -= 4;                // Resta y asignación
console.log(asignarResta);        // 3

let asignarMultiplicacion = 7;
asignarMultiplicacion *= 2;          // Multiplicación y asignación
console.log(asignarMultiplicacion);  // 14

let asignarDivision = 7;
asignarDivision /= 2;                // División y asignación
console.log(asignarDivision);        // 3.5

let asignarModulo = 7;
asignarModulo %= 2;                  // Módulo y asignación
console.log(asignarModulo);          // 1

let asignarPotencia = 7;
asignarPotencia **= 2;                    // Potencia y asignación
console.log(asignarPotencia);             // 49


// OPERADORES DE PERTENENCIA

let arreglo = [0, 1, 2, 3, 4];
console.log(3 in arreglo);      // true
console.log(11 in arreglo);     // false

// OPERADORES DE BITS

console.log(3 & 4);         // AND -> 0
console.log(3 | 4);         // OR -> 7
console.log(3 ^ 4);         // XOR -> 7
console.log(~3);            // NOT -> -4
console.log(3 << 4);        // Desplazamiento a izquierda -> 48
console.log(3 >> 4);        // Desplazamiento a derecha -> 0


// ESTRUCTURA DE CONTROL: if - else if - else

let puntuacion = 8;

if (puntuacion >= 5) {
    console.log('Has aprobado el examen!');
} else if (puntuacion < 5) {
    console.log('No has aprobado el examen...');
} else {
    console.log('Las puntuaciones aún no están disponibles.');
}


// ESTRUCTURA DE CONTROL: switch

let mes = 1;
let nombreMes = '';

switch (mes) {
    case 1:
        nombreMes = 'Enero';
        break;
    case 2:
        nombreMes = 'Febrero';
        break;
    case 3:
        nombreMes = 'Marzo';
        break;
    case 4:
        nombreMes = 'Abril';
        break;
    case 5:
        nombreMes = 'Mayo';
        break;
    case 6:
        nombreMes = 'Junio';
        break;
    case 7:
        nombreMes = 'Julio';
        break;
    case 8:
        nombreMes = 'Agosto';
        break;
    case 9:
        nombreMes = 'Septiembre';
        break;
    case 10:
        nombreMes = 'Octubre';
        break;
    case 11:
        nombreMes = 'Noviembre';
        break;
    case 12:
        nombreMes = 'Diciembre';
        break;
    default:
        nombreMes = 'Número de mes no válido';
}
console.log(`Mes: ${nombreMes}`);    // Mes: Enero


// ESTRUCTURA DE CONTROL: for

for (let i = 0; i < 5; i++) {
    console.log(i);
}
/* Se imprimen los siguientes números:
    0, 1, 2, 3, 4
*/


// ESTRUCTURA DE CONTROL: for-in

const person = {
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
    name, username, age
*/


// ESTRUCTURA DE CONTROL: for-of

const numArr = ['hola', true, 7, ['a', 'b', 'c']]

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

let i = 0;
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

let j = 'Not empty';
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

for (let num = 10; num <= 55; num++) {
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