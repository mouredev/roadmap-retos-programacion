<?php

// Esto es un comentario de una línea

/*
  Este es un comentario de varias líneas o multilinea
*/

// Sitio oficial: 

//   Variables: se representan con un signo de dolar $ seguido del nombre de la variable
//   De forma predeterminada, las variables siempre se asignan por valor. 
//   Para asignar por referencia se antepone un signo ampersand (&) al comienzo de la variable 
//   cuyo valor se está asignando (la variable fuente). 

$mi_variable = 1;

// Tipos

// Tipo null: representa una variable sin valor
$var = null;         // insensible a minúsculas/mayúsculas - null - NULL
$var2;               // Si a una variable no se le ha asignado valor su valor es null

// Booleanos: expresa un valor que indica verdad.  Puede ser true(verdadero) o false(falso)
$verdadero = true;
$falso = false;

// Números enteros (Integers)
$entero = 127;
$octal = 020;
$hexadecimal = 0xFF;
$binario = 0b1111;

// Números de punto flotante (floats)
$float = 1.23;
$float2 = 1.23e10;
$float3 = 5E-10;
$float4 = 1_234.54;

// cadenas de caracteres (Strings)
$simple = 'Hola';
$doble = "PHP";
$con_secuencias = "Esto es un ejemplo con \n secuencias de escape";

$heredoc = <<<EOD
Ejemplo de una cadena
expandida en varias líneas
empleando la sintaxis heredoc.
EOD;

$str = <<<'EOD'
Ejemplo de un string
expandido en varias líneas
empleando la sintaxis nowdoc.
EOD;

// Arrays: mapas ordenados
$arreglo = [
  "foo" => "bar",
  "bar" => "foo",
];
$arreglo2 = [1, 2, 3, 4, 5];

// Imprimir por consola o terminal
echo "¡{$simple}, {$doble}!";
