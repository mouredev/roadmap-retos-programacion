<?php

/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
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
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */



// Lenguaje seleccionado PHP https://www.php.net/

# Comentario en una sola linea

/* 
Comentario en varias lineas
*/

# VARIABLE
$variable = "Soy una variable"; 

$variable = "Acabo de cambiar el valor de esta variable";

# CONSTANTE
define ("CONSTANTE",  "Soy una constante");
const CONSTANTE1 = "Creaste otra constante satisfactoriamente"; 


#string 

$str = "Soy un string";

#integer == numero entero 

$integer = 1; 

#float == numero decimal 

$float = 0.3 ;

#booleano 

$verdader0 = true; 
$falso = false; 

#null 

$nulo = null; 

#array 

$lista_simple = ["papel", "jabon", "hielo", "madera"]; 

#array asociativo 


$lista_cantidades = [
        "arroz" => "bastante",
        "fideos" => "tambien",
        "cristale" => "masomenos" 
];


echo $lista_simple[0]; 

echo $lista_cantidades['cristale'];

echo "Hola, PHP";

var_dump($str);

var_dump($integer);

var_dump($float);

var_dump($verdader0);

var_dump($falso);

var_dump($lista_cantidades['fideos']);

var_dump(CONSTANTE);
var_dump(CONSTANTE1);
