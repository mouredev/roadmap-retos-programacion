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

// Funcion sin argumentos y sin retorno
function greeting() {
  console.log("Hola!, Javascript");
}

greeting();

// Funcion con argumentos y sin retorno
function greetingUser(user) {
  console.log(`Hola!, ${user}`);
}

greetingUser("Diego");

// Funcion con argumentos y retorno
function mult(a, b) {
  return a * b;
}

console.log(mult(2, 10));

// funcion anonima
const counterWords = function (text) {
  const words = text.split(" ");
  return words.length;
};

console.log(
  counterWords(
    "Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda."
  )
);

// Funcion flecha o arrow function

const bigNumber = (array) => {
  return array.sort().pop();
};

console.log(bigNumber([1, 10, 2, 334, 290, 2, 1, 3]));

// Funciones anidadas

function extern(a) {
  console.log("Hola!, Externo");
  function intern(a) {
    console.log("Hola!, interno");
  }
  intern();
}

extern();

// Funciones de ordern superior
function operationNumber(a, b, callback) {
  return callback(a, b);
}

console.log(operationNumber(2, 100, mult));

/*
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 */

const fizzbuzz = (fizz, buzz) => {
  let count = 0
  for (let i = 1; i < 101; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(fizz + buzz)
    } else if (i % 3 == 0) {
      console.log(fizz)
    } else if (i % 5 === 0) {
      console.log(buzz)
    } else {
      console.log(i)
      count++
    }
  }
  return count
}

console.log(fizzbuzz("fizz", "buzz"))
