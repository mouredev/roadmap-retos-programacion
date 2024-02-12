// #02 FUNCIONES Y ALCANCE

/**
 * Crea ejemplos de funciones básicas que representen las diferentes
 * posibilidades del lenguaje:
 */

//Declaración y tipos de funciones en JavaScript
// 01. Función sin parametros ni retorno
function saludoSimple() {
  console.log("Hola JavaScript.");
}
saludoSimple(); // 'Hola JavaScript.'

// 02. Función con un parametro y retorno
function saludoRetorno(string) {
  console.log(`Hola ${string}.`);
  return string;
}
saludoRetorno("JavaScript"); // Hola JavaScript.

// 03. Función con 2 o mas parámetros
function multiplicar(num1, num2) {
  return console.log(num1 * num2);
}
multiplicar(10, 7); // 70

// 04. Función expresión
const multiplicar2 = function mult(num1, num2) {
  return console.log(num1 * num2);
};
multiplicar2(10, 6); // 60

// 05. Función expresión (Anonima)
const multAnonima = function (num1, num2) {
  return console.log(num1 * num2);
};
multAnonima(10, 5); // 50

// 06. Función Flecha o Arrow Function
let myArray = [-5, -10, 80, 0, 7, -155];

let ABSOLUTO = (arr) => {
  let arrAbsoluto = [];
  for (let i = 0; i < arr.length; i++) {
    let valAbsoluto = Math.abs(arr[i]);
    console.log(valAbsoluto);
    arrAbsoluto[i] = valAbsoluto;
  }
  console.log(arrAbsoluto);
  return arrAbsoluto;
};

ABSOLUTO(myArray); // [5, 10, 80, 0, 7, 155]

// 07. Variables LOCALES y GLOBALES
let globalVar = "Esta es una variable GLOBAL";

function ejemplo() {
  let localVar =
    "Esta es una variable LOCAL de la función.\nUna variable local solo puede ser accedida desde\ndentro de la función en la que se define.";
  console.log(globalVar);
  console.log(localVar);
}

ejemplo();
/*
"Esta es una variable GLOBAL"
"Esta es una variable LOCAL de la función.
Una variable local solo puede ser accedida desde
dentro de la función en la que se define."; 
*/

console.log(globalVar); // "Esta es una variable GLOBAL"

// Acceso desde fuera del bloque de la función: error de referencia
// console.log(localVar); // Uncaught ReferenceError: localVar is not defined

// 08. Crear una funcion dentro de otra funcion
let numeros = [1, 3, 5];

function multiplicadora(arr, multi) {
  let multiplicados = [];
  let recorrer = () => {
    for (let numero of arr) {
      let resultado = numero * multi;
      multiplicados.push(resultado);
    }
    return multiplicados;
  };
  return recorrer();
}

console.log(multiplicadora(numeros, 5)); // [5, 15, 25]

/** DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 */

function extra(string1, string2) {
  let numberHasBeenPrinted = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(string1 + string2);
    } else if (i % 3 === 0) {
      console.log(string1);
    } else if (i % 5 === 0) {
      console.log(string2);
    } else {
      numberHasBeenPrinted++;
      console.log(i);
    }
  }
  console.log(`The number has been printed ${numberHasBeenPrinted} times.`);
  return numberHasBeenPrinted;
}

extra("Road", "map");
