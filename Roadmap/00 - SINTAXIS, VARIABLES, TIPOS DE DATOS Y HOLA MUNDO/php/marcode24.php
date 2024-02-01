<?php
/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// - Crea una variable (y una constante si el lenguaje lo soporta).
$miVariable = 'Hola, mundo';
// Definir una constante en PHP (a partir de PHP 7.0)
define('MI_CONSTANTE', 42);

// - Crea variables representando todos los tipos de datos primitivos
//   del lenguaje (cadenas de texto, enteros, booleanos...).
$cadenaTexto = 'Hola';
$numeroEntero = 42;
$numeroDecimal = 3.14;
$booleano = true;
$bigInt = 9007199254740991; // PHP no tiene un tipo de dato BigInt como JavaScript
$nulo = null;
$indefinido = null; // En PHP, una variable sin valor asignado es nula
$objeto = [
  'nombre' => 'Pepe',
  'edad' => 42,
];
$array = [1, 2, 3];

// - Imprime por terminal el texto: "¡Hola, PHP!"
echo '¡Hola, PHP!';

// Otra forma de imprimir por terminal con salto de línea
echo PHP_EOL;

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
?>
