<?php //así se inicia un archivo

//Comentarios:

//Comentario de una línea

/*
Comentarios de más
de una línea.
*/ 

//Variables: Las variables se definen con "$" delante
$variableInteger = 10; //Número entero
$variableFloat = 5.7; //Número decimal
$variableString = "Esta es mi cadena de texto"; //Cadenas de texto
$variableBool = true; //Verdadero o falso
$array = array("elemento1", "elemento2", "elemento3");
define("PI", 3.14); //constantes

//Imprimir datos en pantalla
echo "Hola Mundo en PHP\n"; // El "\n" se usa para saltar una línea
//O así:
$HolaMundo = "Hola Mundo en PHP\n";
echo $HolaMundo;

//Concatenar:
$lenguaje = "PHP";
echo "Hola mundo en " . $lenguaje . "\n";

/*Si ejecutas, el output será:
Hola Mundo en PHP
Hola Mundo en PHP
Hola mundo en PHP
*/