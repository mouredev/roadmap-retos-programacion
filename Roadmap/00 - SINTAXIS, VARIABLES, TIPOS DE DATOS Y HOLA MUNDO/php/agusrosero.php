<?php
/*
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

// https://www.php.net/

// Comentario en una linea
# Esto tambien es un comentario en una linea
/*
Comentario de
varias lineas
*/

// Variables y constantes
$miVariable = "Mi variable";
define("MI_CONSTANTE", "Valor de mi constante");

// Tipos de datos
$entero = 23;
$cadena = "Mi cadena";
$flotante = 3.14;
$booleano = true;
$arrays = array("Rojo", "Negro", "Blanco");
$nulo = null;

// Imprime por terminal 
print "¡Hola, PHP!";
?>