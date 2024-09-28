<?php
// 1.web oficial de PHP
//https://www.php.net/

// 2.Tipos de comentarios:

// 2.1. Con doble barra puedo crear un comentario de una sola linea

/* 2.2. Para crear comentarios de mas de una linea uso barra más asterisco para abrir y cierro con
asterisco más barra */

// 3.Creación de variables
//php es sensible a mayusculas y minusculas. 
$mi_variable = "Mi primera variable"
$Mi_variable = "Esta varables es diferente por la mayuscula"

// 3.1Creación de constantes en PHP
//Puedo nombras constantes de dos formas
define("MI_CONSTANTE_1",23);

//dentro de una clase
class Unaclase{
    const MI_CONSTANTE_2 = 5;
}

// 4.Variables con tipos de datos primitivos
//Null
$variable_1 = NULL;
//Boolean
$variable_2 = True;
//integer
$variable_3 = 3;
//float
$variable_4 = 3.141516;
//string
$variable_5 = 'Variable-string':
//arrays
$variable_6 = array("sin-clave", "con"=>"clave", "numero"=>23);

// 5. Imprimir

echo "¡Hola, PHP!";


?>