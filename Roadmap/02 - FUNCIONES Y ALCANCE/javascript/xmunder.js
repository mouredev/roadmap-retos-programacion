/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
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

// Tipos de funciones en JavaScript

// 1. Función mediante declaración.

// Sin parametros ni retorno.
function sayHello() {
  console.log("Hello World!");
}
sayHello(); //Hello World!

// Con parametros y retorno.
function sayHello2(name) {
  return `Hello ${name}!`;
}
console.log(sayHello2("World")); // Hello World!

// Con varios parametros y retorno.
function sayHello3(name, surname) {
  return `Hello ${name} ${surname}!`;
}
console.log(sayHello3("World", "in Javascript")); // Hello World in Javascript!

// -------------------------- // -------------------------- // -------------------------- //

// 2. Función mediante expresión.

// Sin parametros ni retorno.
const sayHello4 = function saludar() {
  console.log("Hello World!");
};
sayHello4(); // Hello World!

// Con parametros y retorno.
const sayHello5 = function saludar(name) {
  return `Hello ${name}!`;
};
console.log(sayHello5("World")); // Hello World!

// Con varios parametros y retorno.

const sayHello6 = function saludar(name, surname) {
  return `Hello ${name} ${surname}!`;
};
console.log(sayHello6("World", "in Javascript")); // Hello World in Javascript!

// -------------------------- // -------------------------- // -------------------------- //

// 3. Función anonima.

// Sin parametros ni retorno.
const sayHello7 = function () {
  console.log("Hello World!");
};
sayHello7(); // Hello World!

// Con parametros y retorno.
const sayHello8 = function (name) {
  return `Hello ${name}!`;
};
console.log(sayHello8("World")); // Hello World!

// Con varios parametros y retorno.
const sayHello9 = function (name, surname) {
  return `Hello ${name} ${surname}!`;
};
console.log(sayHello9("World", "in Javascript")); // Hello World in Javascript!

// -------------------------- // -------------------------- // -------------------------- //

// 4. Función flecha.

// Sin parametros ni retorno.
const sayHello10 = () => {
  console.log("Hello World!");
};
sayHello10(); // Hello World!

// Con parametros y retorno.
const sayHello11 = (name) => {
  return `Hello ${name}!`;
};
console.log(sayHello11("World")); // Hello World!

// Con varios parametros y retorno.
const sayHello12 = (name, surname) => {
  return `Hello ${name} ${surname}!`;
};
console.log(sayHello12("World", "in Javascript")); // Hello World in Javascript!

// -------------------------- // -------------------------- // -------------------------- //

// Comprueba si puedes crear funciones dentro de funciones.

// Funciones anidadas.
function Anidada(arg1) {
  return function Anidada2(arg2) {
    return `${arg1} ${arg2}`;
  };
}
console.log(Anidada("Hello")("World!")); // Hello World!

// -------------------------- // -------------------------- // -------------------------- //

// Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

// Función que recibe un rango de números y devuelve un numero aleatorio entre ellos.

function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}
console.log(getRandomNumber(1, 10));

// -------------------------- // -------------------------- // -------------------------- //

// Pon a prueba el concepto de variable LOCAL y GLOBAL.

// Variable global.
let globalVar = 10;

function global() {
  console.log(globalVar);
}
global(); // 10

// Variable local.
function local() {
  let localVar = 20;
  console.log(localVar);
}
local(); // 20

// -------------------------- // -------------------------- // -------------------------- //

// Dificultad extra

function extraChallenge(text1, text2) {
  let count = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(`${text1} + ${text2}`);
    } else if (i % 3 === 0) {
      console.log(text1);
    } else if (i % 5 === 0) {
      console.log(text2);
    } else {
      console.log(i);
      count += 1;
    }
  }
  return `Se han mostrado ${count} veces los números`;
}

console.log(extraChallenge("fizz", "buzz"));
