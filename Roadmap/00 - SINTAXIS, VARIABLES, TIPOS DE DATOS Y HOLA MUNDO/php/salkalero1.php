<?php
// https://www.php.net/

// Primera forma de escribir un comentario en una línea.

# Segunda forma de escribir un comentario en una línea.

/*
Tercera forma de escribir un comentario
en varias líneas.
*/

// Variable
$nombre = "Salkalero";

/* Constante usando define que es de ambito
global. Ya sea  usando define o const e escribe siempre
con mayusculas por convección.*/

define("PI", 3.1416);

echo PI . "\n";

/* Constante usando const que no necesita $ y es de ambito
global o de clase.
*/
const GRAVEDAD = 9.81;

echo GRAVEDAD . "\n";

// Variables según su tipo de dato primitivo.
$entero = 10; //Integer.
$float = 3.14; //Float o double.
$booleano = true; //Boolean.
$string = "Hola PHP"; //String.
$array = [0,1,2,3,4]; //Array.
$null = null; //Null.

// Hola Mundo en PHP.
$saludo = "Hola PHP";
echo $saludo ."\n";
