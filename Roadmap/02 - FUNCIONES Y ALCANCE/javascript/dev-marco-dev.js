//#02 FUNCIONES Y ALCANCE
/*EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...*/

function greet() {
  console.log("hi");
}

function sum(a, b, c) {
  return a + b + c;
}

// Comprueba si puedes crear funciones dentro de funciones.

function outerFunction() {
  function innerFunction() {
    console.log("I am inside of the innerFunction");
  }
  innerFunction();
}

//Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
console.log("hi");

//- Pon a prueba el concepto de variable LOCAL y GLOBAL.

let greet1 = "HI";
console.log(greet1);

function greet1() {
  let greet2 = "HI";
}

//DIFICULTAD EXTRA (opcional):
/*Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

function test(fizz, buzz) {
  let contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(fizz + buzz);
    } else if (i % 3 === 0) {
      console.log(fizz);
    } else if (i % 5 === 0) {
      console.log(buzz);
    } else {
      console.log(i);
      contador++;
    }
  }
  return contador;
}
console.log(test("fizz", "buzz"));
