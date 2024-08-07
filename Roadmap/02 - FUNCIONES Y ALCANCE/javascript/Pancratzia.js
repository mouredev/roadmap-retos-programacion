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

function intro() {
  console.log(
    "¡Hola, Javascript!\n¿Sabías que puedes encontrar diferentes tipos de funciones en el lenguaje de programación?\nEsta por ejemplo no recibe parametros ni hace ni retorna ningún valor"
  );
}

function paramsFunction(param1, param2, ...params) {
  console.log(
    "Esta otra función recibe por parametros los números " +
      param1 +
      " y " +
      param2 +
      " y " +
      params
  );
}

function returnFunction(programmingLang) {
  mensaje =
    "Y esta función retorna un parametro l cual es el lenguaje de programación que estamos utilizando. En este caso es: " +
    programmingLang;
  return mensaje;
}

function functionInsideAntoherFunction() {
  console.log("¿Es posible crear funciones dentro de otras?");

  function isPossible() {
    return "Si, es posible! Pero las mismas solo pueden ser llamadas dentro de la función en la que fueron creadas.";
  }

  console.log(isPossible());
}

function javaScriptOriginalFunction() {
  console.log(
    "Existen funciones nativas de JavaScript. Por ejemplo, el método Math.max() que retorna el número mayor entre dos números o el console.log que muestra por consola el argumento que le pasemos"
  );
}

const arrowFunction = () => {
  console.log(
    "Existen las funciones flecha, que se definen de la siguiente manera: let arrowFunction = () => { }"
  );
};

//Una funcion declarada como function puede ser llamada antes o después de ser declarada. Pero una arrow function no puede ser llamada antes de ser declarada.

let globalVariable = "Variable Global";

function globalAndLocal() {
  let localVariable = "Variable Local";

  console.log(globalVariable);
  console.log(localVariable);

  globalVariable = "Variable Global Modificada";
}

intro();
paramsFunction(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
console.log(returnFunction("Javascript"));
functionInsideAntoherFunction();
// isPossible(); - Aquí esa función no está definida
javaScriptOriginalFunction();
globalAndLocal();
console.log(
  `En la función globalAndLocal() la variable global fue modificada a: ${globalVariable}. Además, la variable local solo existe dentro de la función.`
);

/**EXTRA**/

const imprimirSegunMultiplo = (param1, param2) => {
  let count = 0;

  for (let i = 1; i <= 100; i++) {
    let message = "";

    if (i % 3 === 0) {
      message += param1;
    }
    if (i % 5 === 0) {
      message += param2;
    }

    if (message !== "") {
      console.log(message);
    } else {
      count++;
      console.log(i);
    }
  }

  return count;
};

console.log(
  `La función imprimirSegunMultiplo() retorna: ${imprimirSegunMultiplo(
    "Fizz",
    "Buzz"
  )} impresiones de números`
);
