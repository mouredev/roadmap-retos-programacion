<?php

# https://www.php.net/docs.php

# comentario de una sola linea
/* 
    comentario de 
    muchas lineas
*/

$name = "Alejandro toro";
define("TYPE", "admin");

/* Representación de de tipos de variables */

$age = 31;
$name = "Héctor toro";
$isAdmin = true;
$numberFloat = 12.3;
$isNull = null;

// tipos compuestos

$fruits = ["manazana","pera"];
$fruits2 = [
    "manzana" => 2,
    "pera" => 6,
];
$person = (object) [
    "name" => "Alejandro toro",
    "age" => 31
];

$lenguaje = "php";
echo "Hola, $lenguaje";





