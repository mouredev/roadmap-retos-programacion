// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";

/***********************************************
********** DECLARACION DE FUNCIONES ************
************************************************/
function recursiveFoo(valorInicial) {
    // Función recursiva para imprimir números desde valorInicial hasta 0
    if (valorInicial < 0) {
        return;
    }
    console.log(valorInicial + ", ");
    recursiveFoo(valorInicial - 1);
}

function factorial(ivalue) {
    // Función recursiva para calcular el factorial de ivalue
    if (ivalue === 1) {
        return 1;
    }
    return ivalue * factorial(ivalue - 1);
}

function fibonacci(n) {
    // Función recursiva para calcular el valor en la posición n de Fibonacci
    if (n <= 0) {
        console.log("La posición debe ser un entero positivo");
        return -1; // o manejo de error según sea necesario
    } else if (n === 1) {
        return 0;
    } else if (n === 2) {
        return 1;
    } else {
        let a = 0, b = 1, temp;
        for (let i = 2; i < n; ++i) {
            temp = b;
            b = a + b;
            a = temp;
        }
        return b;
    }
}

/*************************************************
******************* PROGRAMA PRINCIPAL **********
**************************************************/
const numeroCalcularFactorial = 3;
const posicion = 10;

console.log("********* NUMEROS DEL 100 - 0 *********");
recursiveFoo(100);
console.log("\n");

console.log(`El factorial de <<${numeroCalcularFactorial}>> es: ${factorial(numeroCalcularFactorial)}`);

const valor = fibonacci(posicion);
console.log(`El valor en la posición ${posicion} de la sucesión de Fibonacci es: ${valor}`);
