<?php
// Realizado con https://www.php.net/

// Comentario de una línea
/* Comentario
  de varias
  líneas
*/

$variable = "Una variable";
const CONSTANTE = "Una constante";

// Numéricos
$entero = 12345;
$flotante = 1.2345;

// Nulo
$nulo = NULL;

// Booleanos
$verdadero = True;
$falso = False;

// Cadenas / Strings
$cadena = "PHP";
$cadena_larga = <<<EOD
  Esta es una cadena
  que ocupa varias líneas
  y que se escribe
  tal cual con la sintaxis
  heredoc.
EOD;

// Arreglos
$arreglo = array(
  "foo" => "bar",
  "bar" => "foo"
);

// a partir de PHP 5.4
$otro_arreglo = [
  "foo" => "bar",
  "bar" => "foo"
];

echo "¡Hola, $cadena!";
print "¡Hola, $cadena!";
