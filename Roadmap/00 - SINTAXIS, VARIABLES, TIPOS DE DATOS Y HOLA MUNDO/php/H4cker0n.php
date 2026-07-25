<?php
// https://www.php.net/ //

/* COMENTARIOS */

// Esto es un comentario de una sola línea en PHP.

/*
Esto es un comentario de varias líneas en PHP.
Puedes usarlo para bloques de texto más largos.
*/

# También puedes usar el signo de número (#) para comentarios de una sola línea,
# aunque las dos barras (//) son más comunes.

/* VARIABLES Y CONSTANTES */
$Variable = "¡HOLA MUNDO!"; // Una variable en PHP siempre comienza con $.
define("hello", 3.14159); // Una constante definida con define().
const GRAVEDAD = 9.81; // Otra forma de definir una constante a partir de PHP 5.3.

/* TIPO DE DATOS */

$cadena = "Esto es una cadena de texto."; // string
$numeroEntero = 150; // integer
$numeroFlotante = 20.5; // float (o double, son similares en PHP)
$booleanoVerdadero = true; // boolean
$booleanoFalso = false; // boolean
$valorNulo = null; // null
$array = [1, 2, 3]; // array (o puedes usar la sintaxis corta [])

/* IMPRIMIR */
$miVariable = "¡Hola, PHP!";
echo $miVariable; // Imprime el valor de la variable 

?>