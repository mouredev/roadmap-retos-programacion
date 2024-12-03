<?php

// La documentacion oficial de php la puedes encontrar en https://www.php.net

// Comentario de una linea

# Otra forma de realizar comentarios de una sola linea

/*
    Esta es la forma de realizar comentarios de multiples lineas en PHP. 
    
    ¿Existen otras formas de realizar comentarios?
*/

/* CONSTANTES */

define('Prueba', 'Hola Mundo'); // De esta forma puedes definir una constante, el primer parametro sera su nombre, y el segundo su valor
const Prueba2 = 'Hola Mundo'; // Esta es otra forma de definir una constante, personalmente esta es la que mas me gusta


/* VARIABLES */

$cadena = "Hola Mundo"; // Variable de tipo string
$entero = 10; // Variable de tipo int
$real = 10.5; // Variable de tipo float
$booleano = true; // Variable de tipo boolean
$nulo = null; // Variable de tipo null
$array = array(1, 2, 3, 4, 5); // Variable de tipo array
$array_alterno = [1, 2, 3, 4, 5]; // Esta es otra forma de declarar un array en php
$asociativo = array('nombre' => 'Luis', 'apellido' => 'Fernández'); // Variable de tipo array asociativo
$asociativo_alterno = ['nombre' => 'Luis', 'apellido' => 'Fernández']; // Esta es otra forma de declarar un array asociativo en php


/* OBJETOS */

$fecha = new DateTime(); // Variable de tipo objeto


/* IMPRIMIR EN PANTALLA */

echo $cadena . ' ' . 'Disfrutar del Roadmap' . "\n"; // Esta es la forma de imprimir en pantalla en php
print "El numero entero es $entero\n"; // Esta es otra forma de imprimir en pantalla en php 
