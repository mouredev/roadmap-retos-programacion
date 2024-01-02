<?php
//https://www.php.net/

//Esto es un comentario de una línea

/* Esto es un comentario
de varias líneas
*/

//Definiendo una variable y dos constantes con const y define
$variable = "variable";
const CONSTANTE = "constante";
define("const2", "constante con define");

//Definiendo los tipos de variables que hay
$numeroEntero = 8;
$booleano = true;
$numeroFloat = 54312.78;
$variableNula = null;
$variableCadena = "PHP";
$variableArray = array(1, 2, 3);
$arrayCorchetes = [1, 2, 3];
$arrayAsociativo = [
    "nombre" => "Jaime",
    "apellido" => "Maciá",
    "estudios" => "DAW",
];

//Imprimiendo por pantalla
echo "Hola, {$variableCadena}";
?>