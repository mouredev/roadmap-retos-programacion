// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";

// #############################################################
// #################### DEFINICIÓN DE FUNCIONES ################
// #############################################################

function sumaReferencia(value1, value2) {
    // Imprime a su vez la variable y su dirección de memoria
    console.log("*** Dentro de la funcion que recibe valores por referencia ***");
    console.log(`&a  ->   ${value1}`);
    console.log(`&b  ->   ${value2}`);
    return value1 + value2;
}

function sumaCopia(value1, value2) {
    // Imprime a su vez la variable y su dirección de memoria
    console.log("\n*** Dentro de la funcion que recibe valores por copia ***");
    console.log(`a   ->   ${value1}`);
    console.log(`b   ->   ${value2}`);
    return value1 + value2;
}

function intercambioValoresReferencia(value1, value2) {
    return [value2, value1];
}

function intercambioCopia(value1, value2) {
    return [value2, value1];
}

// #############################################################
// ################## PROGRAMA PRINCIPAL #######################
// #############################################################

// Variables las cuales se van a usar como conejillos de indias
let numero = 94;
let numero2 = 6;

// En esta sección se imprimirán la dirección en memoria de las variables
console.log("*** Estos son las direcciones en memoria de las variables previamente definidas***");
console.log(`Ubicación en memoria de numero: ${numero}`);
console.log(`Ubicación en memoria de numero2: ${numero2}`);

sumaReferencia(numero, numero2);
sumaCopia(numero, numero2);

console.log("\n******************\n");

console.log("Valor de las variables originales");
console.log(`a -> ${numero}`);
console.log(`b -> ${numero2}`);

// Después de hacer el cambio de variables mediante una función que recibe los parámetros por copia
let resultadoCopia = intercambioCopia(numero, numero2);
let copia1 = resultadoCopia[0];
let copia2 = resultadoCopia[1];

console.log("\nValor de las variables después de hacer un intercambio de valores (copia)");
console.log("Variables originales");
console.log(`a -> ${numero}`);
console.log(`b -> ${numero2}`);
console.log("Variables retornadas");
console.log(`copia a -> ${copia1}`);
console.log(`copia b -> ${copia2}`);

// Después de hacer el cambio de variables mediante una función que recibe los parámetros por referencia
let resultadoReferencia = intercambioValoresReferencia(numero, numero2);
let referencia1 = resultadoReferencia[0];
let referencia2 = resultadoReferencia[1];

console.log("\nValor de las variables después de hacer un intercambio de valores (referencia)");
console.log("Variables originales");
console.log(`a -> ${numero}`);
console.log(`b -> ${numero2}`);
console.log("Variables retornadas");
console.log(`copia a -> ${referencia1}`);
console.log(`copia b -> ${referencia2}`);
