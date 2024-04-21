<!-- 
EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!
-->

<?php

// URL web oficial
// https://www.php.net/


// comentario en una linea

# Comentario de una linea en un formato diferente

/**
 * Comentario multilineal:
 * comentario1
 * comentario2
 */

 /*
  Otra sintaxis de comentario multilineal:
  comentario1
  comentario2
 */

//variable
$nombre = "JuanRCoder";
$languaje = 'php';

//Constante definida
M_PI //-> 3.141516

//Constante a definir
define('NACIMIENTO', 310301);
echo NACIMIENTO; //-> 310301

//Variables primitivas
$int = 23;
$float = 4.21;
$string = 'hello joe';
$boolean = true;
$nulo = null;
$array = array('pera', 'manzana', 'fresa');

echo "¡Hola, $languaje!";
?>