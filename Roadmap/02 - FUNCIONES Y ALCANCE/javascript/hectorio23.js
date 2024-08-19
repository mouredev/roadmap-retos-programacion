"use strict";
 // Variable global
let globalVariable = "Soy global";

// Función sin parámetros ni retorno
const doSomething = () => console.log("¡Hola!");

// Función con un parámetro y retorno
function square(number) {
    return number * number;
}

// Función con múltiples parámetros y retorno
const  sum = (a, b) =>  a + b;

// Función que retorna una función
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

// Función dentro de otra función
function outerFunction() {
    let outerVariable = "Soy local externa";

    function innerFunction() {
        let innerVariable = "Soy local interna";
        console.log(innerVariable);
        console.log(outerVariable); // Puede acceder a la variable local de la función externa
    }

    innerFunction();
}

// Ejecutando las funciones
doSomething2();
console.log(square(5));
console.log(sum(3, 4));

let multiplyBy2 = createMultiplier(2);
console.log(multiplyBy2(5));

outerFunction();
// console.log(innerVariable); // Esto dará un error ya que la variable local de la función interna no está disponible fuera de ella

// Función según tu descripción
function printNumbers(text1, text2) {
    let count = 0; // Variable local

    for (let i = 1; i <= 100; i++) {
        let output = "";

        if (i % 3 === 0) output += text1;

        if (i % 5 === 0) output += text2;

        if (output) {
            console.log(output);
            count++;
        }
    }

    return count;
}

console.log(printNumbers("Múltiplo de 3", "Múltiplo de 5"));
console.log(`Variable Global: ${ globalVariable }`);
// console.log(outerVariable); // Esto dará un error ya que la variable local de la función externa no está disponible fuera de ella
