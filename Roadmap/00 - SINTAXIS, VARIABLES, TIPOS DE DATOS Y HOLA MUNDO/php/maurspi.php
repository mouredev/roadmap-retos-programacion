<?php

//URL DEL LENGUAJE ELEGIDO: https://www.php.net/manual/es/intro-whatis.php

/*Comentarios 
muchas 
lineas
*/

 $variable = 0;
//FORMAS DE DECLARAR CONSTANTES

const GATO_GORDO = "PEPO";
define("CONSTANTE", 8);

echo 'Valor de la primera constante: '. GATO_GORDO . PHP_EOL; // salto de linea php_eol
echo 'Valor de la segunda constante: '. CONSTANTE .PHP_EOL;

//Datos primivitos. Es un lenguaje de tipado dinamico por eso no se declaran los tipos de datos
$numero=123;
$decimal=12.12;
$esVerdad=true;
$esFalso = false;
$cadenaTexto='Hola Pepo';
$otraCadenaDeTexto = "Buenas tardes China";
$arreglos = array('Hola',12,332,"tres");
$variableNula = null;

$lenguaje = 'PHP';

echo 'Hola '. $lenguaje .PHP_EOL;
