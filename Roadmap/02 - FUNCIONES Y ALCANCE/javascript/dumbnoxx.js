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

// Ejemplo de funciones con la keywork function

// Funciones sin retorno y sin parametros
function hola() {
  console.log("Hola, Mundo");
}

const adios = () => {
  console.log("Adios Mundo");
}

// Funciones con retorno sin parametros
function retorno() {
  return "Retorna este string esta funcion.";
}

const retornoFlecha = () => {
  return "Rertorna otra string esta funcion";
}

// Funciones con parametros sin retorno
function sum(a, b) {
  console.log(a + b);
}

const sumas = (a, b) => {
  console.log(a + b);
}

// Funciones con retorno y con parametros
function sutra(a, b) {
  return a - b;
}

const resta = (a, b) => {
  return a - b;
}

// Funciones dentro de funciones
function funcionInFuncion() {
  function suma(a, b) {
    return a - b;
  }
  return suma(3, 3);
}

const functionInFunction = () => (a, b) => a - b;


functionInFunction(2, 3); // Asi se usaria

// Funciones ya creadas en el lenguaje

const parseInts = parseInt("2"); // Output 2
console.log(parseInts);

const parseFloats = parseFloat("2.3"); // Output 2.3
console.log(parseFloats);



const variableGlobal = 2; // Esta variable podra estar en cualquier funcion en el documento

const functionVariableLocal = () => {
  const variableLocal = 2; // Esta variable solo podra estar disponible dentro de la funcion
  console.log(variableGlobal);
  console.log(variableLocal);
}

functionVariableLocal();
// console.log(variableLocal); // Da un error

/*
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

const retoExtra = (string1, string2) => {
  let count = 0;
  for (let i = 0; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(string1 + string2);
    }
    if (i % 5 === 0) {
      console.log(string2);
    }
    if (i % 3 === 0) {
      console.log(string1);
    }
    else {
      console.log(i);
      count += 1;
    }
  }
  return `El numero de veces que se ha impreso el numero en lugar de los textos es: ${count}`;
}

console.log(retoExtra("Hola, ", "Mundo"));
