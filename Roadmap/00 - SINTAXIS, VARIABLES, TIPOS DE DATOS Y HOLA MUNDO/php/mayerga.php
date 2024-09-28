<?php

// Esto es un comentario de una sola línea de PHP
// https://www.php.net/
/* Esto es un comentario
    de varias líneas */

//Variable
$mi_nombre = 'Manuel';

//constante
define('mi_nombre', 'Manuel');
//Haciendo uso de mi variable
echo nombre;

//Tipos de datos
$var_null = NULL;
$var_boolT = True;
$var_boolF = False;
$var_entero = 1234;
$var_decimal = 123.4;
$var_string = 'Hola, me llamo Manuel';

  
// a partir de PHP 5.4
$arreglo = [
    "foo" => "bar",
    "bar" => "foo"
];

$nombreLenguage = "PHP";

echo "¡Hola, " . $nombreLenguage . "!";
print "¡Hola, $nombreLenguage!";
?>