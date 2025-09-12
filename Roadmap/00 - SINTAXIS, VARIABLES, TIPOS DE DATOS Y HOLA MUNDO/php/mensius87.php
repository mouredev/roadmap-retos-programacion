<?php

/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 * 
 */

// Existen tres tipos de comentarios:

// Comentario de una sola línea

# Otro comentario de una sola línea con otro formato

/* Comentario multilínea:
    línea
    línea
    línea
*/


/**
 * Comentario de documentación (lleva 2 astericos al principio). Sirve para generar docuemntación
 * automáticamente.
 * Esta es una descripción de la función
 * 
 * Más detalles sobre esta función aquí.
 */

// variables
$variableString = "Hola MoureDev"; // variable String
$variableInteger = 12; // variable entera
$variableFloat = 12.5; // variable decimal
$variableBoolean = true; // variable booleana
$variableArray = array("a", "b","c"); // variable tipo array

// Constantes
const CONSTANTEPI = 3.14; // forma de crear constante (debe de ir en mayúscula)
define("CONSTANTEPI2",3.14); // otra forma de crear constante, también tiene que ir en mayúscula

$nombreLenguage = "PHP";

// Imprimir mensaje con el nombre del lenguaje
echo "¡Hola, " . $nombreLenguage . "!";
?>