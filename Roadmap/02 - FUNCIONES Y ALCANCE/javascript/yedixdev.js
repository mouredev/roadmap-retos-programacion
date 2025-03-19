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

//Sin parametros ni retrono
function javaScript() {
  console.log("Hola mundo");
}

javaScript();

// Con parámetros
const nombre = "Yedixon";
const apellido = "Ramones";

function yoSoy(nombre, apellido) {
  console.log(`Hola, soy ${nombre} ${apellido}`);
}

// Con parámetros y retorno
const a = 6;
const b = 5;

function edad(a, b) {
  return (a + b) * 2;
}

const result = edad(a, b);
console.log(result); // Mostrará 22

//Funcion dentro de un a funcion

const precioTotal = 100;
const descuentoTotal = 15; //15 %

function calcularPrecioFinal(precioTotal, descuentoTotal) {
  function calcularDescuento(precio, descuento) {
    return precio * (descuento / 100);
  }

  const descuento = calcularDescuento(precioTotal, descuentoTotal);
  return precioTotal - descuento;
}

const precioFinal = calcularPrecioFinal(precioTotal, descuentoTotal);
console.log(`El precio final es: $${precioFinal}`); // Muestra: El precio final es: $85

//Variables Global y locales
const mensajeGlobal = "Soy variable Global";

function comprobarVariables() {
  const mensajeLocal = "Soy variable Local";
  console.log(mensajeGlobal);
  console.log(mensajeLocal);
}

comprobarVariables();
