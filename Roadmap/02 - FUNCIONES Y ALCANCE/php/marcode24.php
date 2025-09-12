<?php

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
  echo '¡Hola desde la función sin parámetros ni retorno!' . PHP_EOL;
}

function funcionConParametros($parametro1, $parametro2) {
  echo 'Parámetro 1: ' . $parametro1 . PHP_EOL;
  echo 'Parámetro 2: ' . $parametro2 . PHP_EOL;
}

function funcionConRetorno($num1, $num2) {
  return $num1 + $num2;
}

// Funciones dentro de funciones
function funcionExterna() {
  echo 'Función externa' . PHP_EOL;

  function funcionInterna() {
    echo 'Función interna' . PHP_EOL;
  }

  funcionInterna();
}

// Variable GLOBAL y LOCAL
$variableGlobal = 'Soy global';

function funcionConVariables() {
  $variableLocal = 'Soy local';
  global $variableGlobal;
  echo $variableGlobal . PHP_EOL;
  echo $variableLocal . PHP_EOL;
}

// Utilizar función ya creada en el lenguaje
$numeros = [1, 2, 3, 4, 5];
$cuadrados = array_map(function($numero) {
  return $numero * $numero;
}, $numeros);

echo 'Cuadrados: ' . implode(', ', $cuadrados) . PHP_EOL;

// Función Extra (DIFICULTAD EXTRA)
function funcionExtra($texto1, $texto2) {
  $contador = 0;

  for ($i = 1; $i <= 100; $i++) {
    if ($i % 3 === 0 && $i % 5 === 0) {
      echo $texto1 . $texto2 . PHP_EOL;
    } elseif ($i % 3 === 0) {
      echo $texto1 . PHP_EOL;
    } elseif ($i % 5 === 0) {
      echo $texto2 . PHP_EOL;
    } else {
      echo $i . PHP_EOL;
    }

    $contador++;
  }

  return $contador;
}

echo 'Número de impresiones: ' . funcionExtra('Fizz', 'Buzz') . PHP_EOL;

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

?>
