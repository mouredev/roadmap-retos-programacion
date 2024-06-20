"use strict";
// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23 

// Definición del decorador genérico
function customDecorator(func) {
    // Retorna una función que envuelve la función original
    return function() {
        console.log("Algo se está haciendo antes de llamar a la función");
        func();
        console.log("Algo se está haciendo después de llamar a la función");
    };
}

// Define la función doSomething
function doSomething() {
    console.log("Esta es mi función");
}

// Aplica el decorador customDecorator a la función doSomething
const doSomethingDecorado = customDecorator(doSomething);

// Llamada a la función doSomething decorada
doSomethingDecorado(); // Output esperado: Algo se está haciendo antes de llamar a la función
                       //                Esta es mi función
                       //                Algo se está haciendo después de llamar a la función

// Definición del decorador contador
function counter(func) {
    // Inicializa el contador de llamadas en 0
    let llamadas = 0;

    // Retorna una función que envuelve la función original
    return function(...args) {
        llamadas++;
        console.log(`Se ha llamado a ${func.name} ${llamadas} veces`);
        // Llama a la función original con los argumentos proporcionados
        return func.apply(this, args);
    };
}

// Define la función saludar
function saludar() {
    console.log("¡Hola Mundo!");
}

// Aplica el decorador counter a la función saludar
const saludarDecorado = counter(saludar);

// Llamadas a la función saludar decorada
saludarDecorado(); // Output esperado: Se ha llamado a saludar 1 veces
                   //                ¡Hola Mundo!
saludarDecorado(); // Output esperado: Se ha llamado a saludar 2 veces
                   //                ¡Hola Mundo!
saludarDecorado(); // Output esperado: Se ha llamado a saludar 3 veces
                   //                ¡Hola Mundo!
