<?php
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


//Concatenación

$nombre = "Cecilia";
$saludo = "Hola";

echo $saludo . ", " . $nombre . "!\n";

//Repetición
print str_repeat("Hola\n", 3);

//Indexación
print $nombre[0] . $nombre[1] . $nombre[2] . $nombre[3] . $nombre[4] . $nombre[5] . $nombre[6] ."\n";

//Longitud
print strlen($nombre);

//Slycing
print substr($nombre, 2, 3) . "\n";

//Busqueda
print strpos($nombre, "c") . "\n";
print strpos($nombre, "e") . "\n";

//Reemplazo
print str_replace("C", "o", $nombre) . "\n";

//División
$nombre = "CeciliaPorras01";
$partes = str_split($nombre);

print_r($partes);

//Mayúsculas , minúsculas y primera letra en mayúscula

print strtoupper($nombre) . "\n";
print strtolower($nombre) . "\n";
print ucfirst($nombre) . "\n";

//Eliminación de espacios en blanco al inicio y al final
$nombre = " Cecilia ";
print trim($nombre) . "\n";

//Busqueda al inicio y al final
print str_starts_with($nombre, "C") . "\n";
print str_ends_with($nombre, "o") . "\n";


//Busqueda de posición
$nombre = "Cecilia Porras01";
print strpos($nombre, "P") . "\n";


//Busqueda de ocurrencias
print substr_count($nombre, "1") . "\n";


//Formateo

$nombre = "Cecilia";
$edad = 25;

$cadenaFormateada = sprintf("Hola, %s. Tienes %d años.", $nombre, $edad);
echo $cadenaFormateada;

//Interpolación
echo "Hola, $nombre. Tienes $edad años.\n";

//Transformación en lista de caracteres
$nombreArray = str_split($nombre);
print_r($nombreArray);

//Transformación de lista en cadena
$nombreArray = str_split($nombre);
$nombre = implode('-', $nombreArray);
echo $nombre;


//Extra

function validText($text1, $text2) {
    print "\n";

    // Palíndromos
    if ($text1 == strrev($text1)) {
        print "$text1 es palíndromo\n";
    } else {
        print "$text1 no es palíndromo\n";
    }

    if ($text2 == strrev($text2)) {
        print "$text2 es palíndromo\n";
    } else {
        print "$text2 no es palíndromo\n";
    }

    // Anagramas
    $text1Normalized = strtolower($text1);
    $text2Normalized = strtolower($text2);

    if (count_chars($text1Normalized, 1) == count_chars($text2Normalized, 1)) {
        print "$text1 y $text2 son anagramas\n";
    } else {
        print "$text1 y $text2 no son anagramas\n";
    }

    // Isogramas
    $textIso1 = strtolower($text1);
    $textIso2 = strtolower($text2);

    if (count(str_split($textIso1)) == count(array_unique(str_split($textIso1))) &&
        count(str_split($textIso2)) == count(array_unique(str_split($textIso2)))) {
        print "$text1 y $text2 son isogramas\n";
    } else {
        print "$text1 y $text2 no son isogramas\n";
    }

}

// Prueba de ejemplo
validText("amor", "roma");  // Debería decir que son anagramas
validText("murcielago", "jamon");  // "murcielago" es isograma, "jamon" también
validText("oso", "radar");  // Ambos son palíndromos

