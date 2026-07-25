/*Operadores aritméticos

    **
    Operador de Exponenciación.

    *
    Operador de multiplicación.

    /
    Operador de división.

    %
    Operador de residuos.

    + 
    Operador de suma.

    -
    Operador de resta.

*/

console.log(5 ** 4);
console.log(3 * 2);
console.log(20 / 4);
console.log(15 % 5);
console.log(2 + 3);
console.log(365 - 65);

/*Operadores lógicos

    &&
    Operador lógico AND.

    ||
    Operador lógico OR.

*/

let a =  4;
let b = -6;

console.log(a > 0 && b > 0);

let a1 = 28;
let b2 = -12;

console.log(a1 > 0 || b2 > 0);

/*Operadores de comparación

==
Comprueba si sus 2 operandos son iguales y retorna un valor booleano.

!=
Operador de desigualdad.

===
Operador de igualdad estricta.

!==
Operador de desigualdad estricta.

*/

let X = 256;
let Y = 256;

console.log(X == Y);

let number = 128;
let letter = "128";

console.log(number != letter);

let valor = 0;
let booleano = false;

console.log(valor === booleano);

let value = '1';
let bool = 1;

console.log(value !== bool);

//Operadores de asignación

//Asignación
let numberA = 2;
console.log(numberA);

//Adición
let numberB = 4;
let numberC = 6;
console.log(numberB += numberC); /* ==>Esto es X = X + Y*/

//Resta
let numberD = 5;
let numberE = 3;
console.log(numberD -= numberE); /* ==>Esto es X = X - Y*/

//Multiplicación
console.log(numberA *= numberB); /* ==>Esto es X = X * Y*/

//División
let numberX = 10;
let numberY = 5;
console.log(numberX /= numberY); /* ==>Esto es X = X / Y*/

/*Operadores lógicos*/
//AND lógico &&
console.log(true && true);
console.log(true && false);
console.log(false && false);
console.log(false && true);

//OR lógico ||
console.log(true || false);
console.log(false || true);
console.log(true || true);

//NOT lógico !
console.log(!true);
console.log(!false);

//Operador condicional (Ternario)
let numero = 10;
let resultado = numero % 2 === 0 ? "Par" : "Impar";
console.log(resultado); // Imprime "Par"

//Dificultad extra
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 == 0) {
        console.log(i);
    }
}
