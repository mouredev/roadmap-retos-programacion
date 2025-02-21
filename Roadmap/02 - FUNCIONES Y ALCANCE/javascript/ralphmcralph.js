// Funciones

// Funciones básicas

// Con retorno
function square(number) {
    return number * number;
}

// Sin retorno

const myCar = {
    make: "Aston Martin",
    model: "AMR25",
    year: 2025
}

function changeMake(newMake) {
    newMake.make = "Honda";
}

console.log(myCar.make);
changeMake(myCar);
console.log(myCar.make);

// Nested function

function addSquares(a, b) {
    function square(x) {
        return x * x;
    }
    return square(a) + square(b);
}

console.log(addSquares(2, 4));

// Con retorno de varios valores

function multipleReturn() {
    return ["Hola", "Javascript"]
}

console.log(multipleReturn());

[greet, language] = multipleReturn();

console.log(greet);
console.log(language);

// Función con argumentos variables

function variableArgs(...names) {
    return names.map((name) => {
        console.log(`Hola ${name}`);
    })
}

variableArgs("Python", "Javascript", "Ruby", 1);

// Ejemplos de funciones ya creadas en el lenguaje

// Console.log

console.log("Esto es una built-in function de Javascript");

// Length

console.log("Javascript".length);

// Tipo
console.log(typeof ("Javascript"));

// Manipulación de strings

console.log("Javascript".toUpperCase());
console.log("Javascript".toLowerCase());

// Puesta a prueba del concepto de LOCAL y GLOBAL

var variableGlobal = "Javascript";

console.log(variableGlobal);

function helloJS() {
    var variableLocal = "Hola"
    console.log(`${variableLocal}, ${variableGlobal}`);
}

helloJS();

// console.log(variableLocal); # No se puede acceder desde fuera de la función

/*
 * DIFICULTAD EXTRA(opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

function extra(str1, str2) {
    count = 0;

    for (i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            console.log(str1 + str2);
        } else if (i % 5 == 0) {
            console.log(str2);
        } else if (i % 3 == 0) {
            console.log(str1);
        } else {
            console.log(i);
            count += 1;
        }
    }

    return count;
}

extra("Fizz", "Buzz");

var resultado = extra("Fizz", "Buzz")

console.log("Resultado: " + resultado);



