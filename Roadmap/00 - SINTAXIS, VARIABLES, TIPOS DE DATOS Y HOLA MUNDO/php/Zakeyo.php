<?php

// https://www.php.net

// Esta es la primera forma de escribir comentarios con PHP, como una sola linea
/*
    Y para escribir lineas multiples se puede usar de esta manera
    Así puedo escribir varias lineas sin necesidad de agregar una
    doble barra cada vez (y hace el código más legible a veces, a mi parecer)
*/

$varDobl = "Hola, soy una variable de doble comillas";
$varSimpl = 'Y yo de comillas simples!';
const CONSTANTE = "Y yo soy una constante!!";

$lang = "PHP";


// Tipos de datos

$integer = "Esto es una cadena de texto";  // Texto plano
$number = 123;  // numérico
$float = 123.45;  // flotante (o decimal)
$bool = true;  // booleano (también puede ser 'false')
$null = NULL;  // null (vacío)
$array = array(
    'clave'  => 'valor',
    'clave2' => 'valor2',
    'clave3' => 'valor3',
);  // Tipo array


echo "Hola, $lang!"

?>