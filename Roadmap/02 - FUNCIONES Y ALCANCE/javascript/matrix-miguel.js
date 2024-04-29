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

// Function without param
function withoutParam() {
  console.log("Hello Matrix");
};
withoutParam();

//with arg and default value
function withParam(a = 1, b = 2) {
  console.log(a + " " + b);
};
withParam("Hi", "Matrix");
withParam((b = 20), (a = 30));
withParam();

// with args
function greetComunity(...names) {
  console.log(names);
  for (const name of names) {
    console.log(`hello ${name}`);
  }
};
greetComunity("Matrix", "Machine Learning", "Anonymous");

// with return
function withReturn() {
  return ["Hello", "Matrix"];
};
console.log(withReturn());
let [word, name] = withReturn();

console.log(word);
console.log(name);

// function inside function
function doubleFunction() {
  function print() {
    return "Hello Matrix double function";
  }

  return print();
};
console.log(doubleFunction());

//Function Built in - random number
console.log(Math.random());
console.log("matrix".toUpperCase());
console.log("matrix".toLowerCase());

//variable local - global
let global = "global";

function scope() {
  let local = "local";
  console.log(global);
  console.log(local);
}
scope();

console.log(global);
console.log(local);

//Fizz-Buzz-Counter
function matrix(fizz = "Fizz", buzz = "Buzz") {
  let counter = 0;
  for (let i = 0; i <= 100; i++) {
    if (i % 3 == 0) {
      console.log(i + fizz);
    }
    if (i % 5 == 0) {
      console.log(i + buzz);
    }
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(i + fizz + buzz);
    }

    counter++;
  }
  return counter;
}

let counter = matrix();
console.log(counter);
