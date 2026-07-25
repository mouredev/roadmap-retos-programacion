<?php

/*
documentacion oficial de PHP:
https://www.php.net/manual/es/
*/

// Este es un comentario de una linea
# Este tambien es un comentario de una linea

/*
   Este es un comentario multilinea 
   en php.
*/


// variables
$my_variable = "hola mundo";
$my_variable = "nuevo valor";

// constantes ( const , define)
const CONSTANTE = "HOLA"; #constante con "const"S
define('CONSTANTE_CON_DEFINE', "Esta tambien es una constante"); #constante con define


#Variables con todos los tipos de datos primitivos
$my_int = 12;
$my_float = 23.02;
$my_str = "carlos";
$my_str2 = 'samuel';
$my_bool = false;

// Imprimir por terminal (echo, print)
echo "¡Hola, PHP!";
echo "Imprimiendo texto con Echo.";
echo "Echo no es una funcion, y no es necesario
utilizar parentesis, ademas, hace salto de linea.
";

print("Hola mundo!");
print 'Print tambien funciona sin parentesis';
print "Tambien serpara los
saltos de lineas utilizando print.";
