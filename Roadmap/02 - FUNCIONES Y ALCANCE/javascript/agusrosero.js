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

function sinParametroNiRetorno() {
  console.log("Hola Javascript!");
}

sinParametroNiRetorno();

function conParametro(name) {
  console.log(`Hola ${name}`);
}

conParametro("Hernan");

function conRetorno(n1, n2) {
  return n1 + n2;
}

console.log(conRetorno(100, 125));

function funcionDentroDeOtra() {
  function saludo() {
    console.log("Saludo desde la otra funcion");
  }
  return saludo();
}

funcionDentroDeOtra();

// funciones ya creadas en el lenguaje
function funcionYaCreada() {
  alert("¡Hola Mundo!");
}

// variables LOCALES y GLOBALES
let varGlobal = "Variable global!";

function mostrarGlobal() {
  console.log(varGlobal);
}

mostrarGlobal();

function mostrarLocales() {
  let varLocal = "Variable local!";
  console.log(varLocal);
}

mostrarLocales();

// DIFICULTAD EXTRA:
function main(str1, str2) {
  contador = 0;
  for (let i = 1; i <= 100; i++) {
    if (i % 5 == 0 && i % 3 == 0) {
      console.log(str1 + str2);
    } else if (i % 5 == 0) {
      console.log(str2);
    } else if (i % 3 == 0) {
      console.log(str1);
    } else {
      contador++;
    }
  }
  return contador;
}

console.log(main("hello", "javascript"));
