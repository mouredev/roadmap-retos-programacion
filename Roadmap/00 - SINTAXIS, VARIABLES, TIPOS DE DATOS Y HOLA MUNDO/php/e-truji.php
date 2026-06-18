<?php
// En inglés: https://www.php.net/
// En castellano: https://www.php.net/manual/es/

// Comentario de una sola línea

/*
Comentario de
múltiples
líneas
*/  

### Comentario de una sola línea con almohadilla tipo shell

//-------------------------------------------------------------//
// Variables
//-------------------------------------------------------------//

$name = 'Estefania';
$language = 'PHP';

//-------------------------------------------------------------//
// Constantes
//-------------------------------------------------------------//

const GLOBO = 'Globo verde'; // Definición de una constante con const

/*
Las constantes también se pueden definir con la función define() 
dentro de una función o condicional, 
a diferencia de las constantes definidas con const.
*/

if ($name === 'Estefania') {
    define('SURPRISE', 'Globos de pikachu!');
}

//-------------------------------------------------------------//
// Datos primitivos
//-------------------------------------------------------------//

$v_int = 35; // Número entero (int)
$v_float = 7.45; // Número decimal (float)
$v_string = "Esta es una cadena de texto con comillas dobles"; // Cadena de texto con comillas dobles
$v_string_2 = 'Esta es una cadena de texto de comillas simples'; // Cadena de texto con comillas simples
$v_boolean_t = true; // Booleano
$v_boolean_f = false; // Booleano


// Imprimir variables por pantalla

echo "¡Hola, $language!";

?>