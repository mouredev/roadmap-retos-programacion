<?php

// Puedes encontrar la documentación en https://www.php.net/

// Comentario de una línea

/* Este es un ejemplo
  de como podemos poner un 
  comentario en varías líneas
*/

$lenguaje = "php"; // Declaración de una variable de tipo string


define("PI", 3.14); // Declaracion de constante
const e = 2.7182; // Otra forma de declarar constantes

// Tipos de datos

$entero = 3; // Tipo entero
$booleano = true; // booleano. Solo toma valores true o false
$real = 125.00; // Tipo float
$nulo = null; // Tipo null 
$cadena = "Hola"; // Tipo string
$arreglo = array(1, 2, 3); // Tipo array
$otro_arreglo = [1, 2, 3]; // Otra forma de declarar un arreglo
$asociativo = array("nombre" => "Juan", "apellido" => "Perez"); // Arreglo asociativo
$otro_asociativo = ["nombre" => "Juan", "apellido" => "Perez"]; // Otra forma de declarar un arreglo asociativo
$fecha = new DateTime(); // Tipo objeto

// Imprimir en pantalla
echo $cadena . ' ' . $lenguaje."\n";
print "El numero entero es $entero\n";
print "El numero real es $real\n";
print "El numero PI es ".PI."\n";
print "El numero e es ".e."\n";
print "El valor nulo es $nulo\n";
print "El valor booleano es $booleano\n";
print "El arreglo es $arreglo[0], $arreglo[1], $arreglo[2]\n";
print "El arreglo asociativo es $asociativo[nombre] $asociativo[apellido]\n";


?>