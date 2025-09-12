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

// Ejemplos de funciones básicas
function funcionSinParametrosNiRetorno() {
  console.log('¡Hola desde la función sin parámetros ni retorno!');
}

function funcionConParametros(parametro1, parametro2) {
  console.log('Parámetro 1:', parametro1);
  console.log('Parámetro 2:', parametro2);
}

function funcionConRetorno(num1, num2) {
  return num1 + num2;
}

// Funciones dentro de funciones
function funcionExterna() {
  console.log('Función externa');

  function funcionInterna() {
    console.log('Función interna');
  }

  funcionInterna();
}

// Variable GLOBAL y LOCAL
const variableGlobal = 'Soy global';

function funcionConVariables() {
  const variableLocal = 'Soy local';
  console.log(variableGlobal);
  console.log(variableLocal);
}

// Utilizar función ya creada en el lenguaje
const numeros = [1, 2, 3, 4, 5];
const cuadrados = numeros.map((numero) => numero * numero);

console.log('Cuadrados:', cuadrados);

// Función Extra (DIFICULTAD EXTRA)
function funcionExtra(texto1, texto2) {
  let contador = 0;

  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(texto1 + texto2);
    } else if (i % 3 === 0) {
      console.log(texto1);
    } else if (i % 5 === 0) {
      console.log(texto2);
    } else {
      console.log(i);
    }

    contador++;
  }

  return contador;
}

console.log('Número de impresiones:', funcionExtra('Fizz', 'Buzz'));

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
