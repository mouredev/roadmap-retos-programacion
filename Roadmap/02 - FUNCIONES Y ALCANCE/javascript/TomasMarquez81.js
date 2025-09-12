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

// Función basica sin parámetros
function basica() {
  console.log("Basica");
}
basica();

// Función basica con parámetro
function basicaParametro(string) {
  console.log(string);
}
basicaParametro("Básica con parámetro");

// Función basica con parámetro por defecto
function basicaParametroDefecto(string = "Con parámetro por defecto") {
  console.log(string);
}
basicaParametro();

// Función basica con retorno
function basicaRetorno() {
  let string = "Básica con retorno";
  return string;
}
console.log(basicaRetorno());

// Función básica con  retorno y parámetros
function basicaRetornoParametro(a, b) {
  return a + b;
}
console.log(basicaRetornoParametro(1, 3));

// Función expression
const sum = function (a, b) {
  return a + b;
};
console.log(sum(3, 5));

// Función flecha
const saludar = (nombre) => {
  console.log("Hola " + nombre);
};
saludar("Tomás");

// Función flecha con return implícito
const sumarFlecha = (a, b) => a + b;
let sumar = sumarFlecha(5, 6);
console.log(sumar);

// Función con variable de argumentos
function variableArg(...names) {
  for (let name of names) {
    console.log("hola " + name);
  }
}

variableArg("Tomas", "Paco", "Pepe");

//Funciones dentro de funciones

function outerFunction() {
  function innerFunction() {
    console.log("Hola JavaScript");
  }
  innerFunction();
}
outerFunction();

// Funciones del lenguaje (built-in)

console.log(Math.abs(-4)); // 4
console.log(Math.cbrt(27)); // 3

let string = "hola";
console.log(string.toUpperCase());

// Variables glovales y locales

let globalVar = "JavaScript";

function varGlobalLocal() {
  let localVar = "Local var";
  console.log(globalVar + " " + localVar);
}
varGlobalLocal();

/// Dificultad Extra

function extraFunction(str1, str2) {
  let dato = 0;
  for (let i = 1; i < 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(str1 + " " + str2);
    } else if (i % 3 === 0) {
      console.log(str1);
    } else if (i % 5 === 0) {
      console.log(str2);
    } else {
      console.log(i);
      dato += 1;
    }
  }
  return dato;
}

extraFunction("Perro", "Gato");
