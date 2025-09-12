<?php

// Vamos a hacer un script que muestre todas las operacioens sobre cadenas que existen en php

// 1. Concatenar cadenas
$cadena1 = "Hola";
$cadena2 = "Mundo";
$cadena3 = $cadena1 . " " . $cadena2;
echo $cadena3 . "\n";

// 2. Longitud de una cadena
echo strlen($cadena3) . "\n";

// 3. Mostrar o no mostrar caracteres
echo substr($cadena3, 0, 5) . "\n";
echo substr($cadena3, 5, 5) . "\n";

// 4. Buscar una cadena dentro de otra
echo strpos($cadena3, "Mundo") . "\n";
echo strpos($cadena3, "mundo") . "\n";

// 5. Reemplazar una cadena por otra
echo str_replace("Mundo", "Universo", $cadena3) . "\n";

// 6. Convertir a mayúsculas y minúsculas
echo strtoupper($cadena3) . "\n";
echo strtolower($cadena3) . "\n";
// 7. Dividir una cadena en array
$cadena4 = "Hola Mundo";
$cadena5 = explode(" ", $cadena4);
echo $cadena5[0] . "\n";
echo $cadena5[1] . "\n";

// 8. Convertir un array en una cadena
$cadena6 = implode(" ", $cadena5);
echo $cadena6 . "\n";

// 9. Eliminar espacios en blanco
$cadena7 = " Hola Mundo ";
echo trim($cadena7) . "\n";

// 10. Eliminar etiquetas HTML
$cadena8 = "<h1>Hola Mundo</h1>";
echo strip_tags($cadena8) . "\n";

// 11. Convertir caracteres especiales en entidades HTML
$cadena9 = "Hola Mundo";
echo htmlentities($cadena9) . "\n";

// 12. Convertir entidades HTML en caracteres especiales
$cadena10 = "Hola Mundo";
echo html_entity_decode($cadena10) . "\n";

// Funcion para comprobar si una cadena es palindroma
function esPalindroma($cadena) {
    $cadena = strtolower($cadena);
    $cadena = str_replace(" ", "", $cadena);
    $cadenaInvertida = strrev($cadena);
    if ($cadena == $cadenaInvertida) {
        return true;
    } else {
        return false;
    }
}

$resultado = esPalindroma("Dabale arroz a la zorra el abad") ? "Verdad" : "Falso";
echo "¿Es palindroma la cadena 'Dabale arroz a la zorra el abad'? ? $resultado\n";
$resultado = esPalindroma("Esto deberia devolver falso") ? "Verdad" : "Falso";
echo "¿Esto deberia devolver falso'? ? $resultado\n";

// Funcion para comprobar si es anagrama
function esAnagrama($cadena1, $cadena2) {
    $cadena1 = strtolower($cadena1);
    $cadena2 = strtolower($cadena2);
    $cadena1 = str_replace(" ", "", $cadena1);
    $cadena2 = str_replace(" ", "", $cadena2);
    $cadena1 = str_split($cadena1);
    $cadena2 = str_split($cadena2);
    sort($cadena1);
    sort($cadena2);
    $cadena1 = implode("", $cadena1);
    $cadena2 = implode("", $cadena2);
    if ($cadena1 == $cadena2) {
        return true;
    } else {
        return false;
    }
}

$resultado = esAnagrama("roma", "amor") ? "Verdad" : "Falso";
echo "¿Es anagrama la cadena 'roma' y 'amor'? ? $resultado\n";
$resultado = esAnagrama("Paco", "capa") ? "Verdad" : "Falso";
echo "¿Es anagrama la cadena 'Paco' y 'capa'? ? $resultado\n";

// Funcion para comproabr si una cadena es isograma
function esIsograma($cadena) {
    $cadena = strtolower($cadena);
    $cadena = str_replace(" ", "", $cadena);
    $cadena = str_split($cadena);
    $cadena = array_count_values($cadena);
    foreach ($cadena as $valor) {
        if ($valor > 1) {
            return false;
        }
    }
    return true;
}

$resultado = esIsograma("murcielago") ? "Verdad" : "Falso";
echo "¿Es isograma la cadena 'murcielago'? $resultado\n";
$resultado = esIsograma("murcielagoo") ? "Verdad" : "Falso";
echo "¿Es isograma la cadena 'murcielagoo'? $resultado\n";






