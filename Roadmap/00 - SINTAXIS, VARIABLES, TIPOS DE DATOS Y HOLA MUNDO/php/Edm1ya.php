<?php
/*
* EJERCICIO:
* - Crea un comentario en el código y coloca la URL del sitio web oficial del
* lenguaje de programación que has seleccionado.
* - Representa las diferentes sintaxis que existen de crear comentarios
* en el lenguaje (en una línea, varias...).
* - Crea una variable (y una constante si el lenguaje lo soporta).
* - Crea variables representando todos los tipos de datos primitivos
* del lenguaje (cadenas de texto, enteros, booleanos...).
* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*
* ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
* debemos comenzar por el principio.
*/


/*
Pagina web oficial de PHP
https://www.php.net/
*/

// Comentario en una sola linea

/*
comentario en
varias lineas
*/


// variable
$variable = "esta es una variable";

// contantes
define('CONSTANTE', "Esto es una constante antigua");
const CONSTANTE2 = "esto es una constante nueva";


// tipos de variables
$numeroEntero = 10;
$numeroDecimal =  13.5;
$texto = "Esto es un string";
$texto2 = 'esto es un string ccon comillas simples';
$boolean = true;
$nulo = null;


echo "Hola!. PHP";
