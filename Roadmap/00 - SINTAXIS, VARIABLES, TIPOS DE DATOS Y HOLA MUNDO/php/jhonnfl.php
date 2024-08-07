<?php

// https://php.net

// Esto es un comentario en una línea

/* 
Esto es un comentario
de varias líneas
*/

// Crea una variable (y una constante si el lenguaje lo soporta).
$variable = "Esto es una variable";

const CONSTANTE = "Esto es una constante";

define("Constante 2", "Esto es una constante con define");

/*
Crea variables representando todos los tipos de datos primitivos
del lenguaje (cadenas de texto, enteros, booleanos...).
*/

$variableNumeroEntero = 6;

$variableBooleanoTrue = true;

$variableBooleanoFalse = false;

$variableNumeroFlotante = 54312.78;

$variableNula = null;

$variableString = "PHP";

$variable_con_array = array(6, 8, 10);

$array_con_corchetes = [5, 6, 7];

$arrayAsociativo = [
    "nombre" => "Jhonn",
    "apellido" => "Flores",
    "Nacionalidad" => "VZLA",
];


//Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
echo "¡Hola, {$variableString}!\n";
echo "Esto es una segunda forma de concatenar en " . $variableString;
?>