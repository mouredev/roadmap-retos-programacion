/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
02 FUNCIONES Y ALCANCE
---------------------------------------
* - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
*/

// ________________________
// Funciones
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Functions

// Función Básica
function aMessage() {
    console.log("Texto");
}

aMessage(); // Llamar

// Función con Parámetro
function displayMessage(msgText) {
    console.log(msgText);
}

displayMessage("¡Hola mundo!");

// Función con Parámetros Opcionales
function sumNums(a, b=5) {
    console.log(a + b)
}

sumNums(2)
sumNums(2, 2)

// ________________________
// Función con retorno
// https://developer.mozilla.org/es/docs/Learn/JavaScript/Building_blocks/Return_values

function squared(num) {
    return num * num;
}

let result = squared(4);
console.log(result); // 16

// Retorna múltiples datos
function calculateRectangleProperties(width, height) {
    return {
      area: width * height,
      perimeter: 2 * (width + height)
    };
}

const rectangle = calculateRectangleProperties(5, 10);
console.log(`Área: ${rectangle.area}`);           // Área: 50
console.log(`Perímetro: ${rectangle.perimeter}`); // Perímetro: 30

// ________________________
// Funciones anidadas
function sumOfSquares(a, b) {
    function square(x) {
      return x * x;
    }
    return square(a) + square(b);
}
  
  console.log(sumOfSquares(2, 3)); // 13

// ________________________
// ejmp de funcion incorporada
const maxNumber = Math.max(10, 20, 5, 30);
console.log(maxNumber); // 30

/* 
EJERCICIO:
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/

function exs(str1, str2) {
    nPrintsNums = 0;

    for (let num = 1; num <= 100; num++) {
        if (num % 3 === 0 && num % 5 === 0) {
            console.log(str1 + str2);
        } else if (num % 3 === 0) {
            console.log(str1);
        } else if (num % 5 === 0) {
            console.log(str2);
        } else {
            nPrintsNums += 1;
            console.log(num);
        }
    }
    return nPrintsNums;
}

pNums = exs(" múltiplo de 3", " múltiplo de 5")
console.log("Número de veces que se imprimió un número: " + pNums);
