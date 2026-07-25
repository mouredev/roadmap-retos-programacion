<?php
// Operaciones con cadenas en PHP

// Declaración de una cadena
$texto = "Hola, mundo!";

echo "Texto original: $texto\n";

// 1. Acceso a caracteres específicos
echo "1. Primer carácter: " . $texto[0] . "\n";

// 2. Subcadenas
echo "2. Subcadena: " . substr($texto, 0, 4) . "\n";

// 3. Longitud
echo "3. Longitud: " . strlen($texto) . "\n";

// 4. Concatenación
$otraCadena = " Bienvenidos";
echo "4. Concatenación: " . $texto . $otraCadena . "\n";

// 5. Repetición
echo "5. Repetición: " . str_repeat($texto, 3) . "\n";

// 6. Recorrido
echo "6. Recorrido:\n";
for ($i = 0; $i < strlen($texto); $i++) {
    echo $texto[$i] . "\n";
}

// 7. Conversión a mayúsculas y minúsculas
echo "7. Mayúsculas: " . strtoupper($texto) . "\n";
echo "   Minúsculas: " . strtolower($texto) . "\n";

// 8. Reemplazo
echo "8. Reemplazo: " . str_replace("mundo", "PHP", $texto) . "\n";

// 9. División
$palabras = explode(", ", $texto);
echo "9. División: " . print_r($palabras, true) . "\n";

// 10. Unión
$arrayPalabras = ["PHP", "es", "genial"];
echo "10. Unión: " . implode(" ", $arrayPalabras) . "\n";

// 11. Interpolación (PHP usa comillas dobles para interpolación)
$nombre = "Alice";
$edad = 30;
echo "11. Interpolación: Me llamo $nombre y tengo $edad años.\n";

// 12. Verificación
echo "12. Empieza con 'Hola': " . (strpos($texto, "Hola") === 0 ? "true" : "false") . "\n";
echo "    Termina con '!': " . (substr($texto, -1) === "!" ? "true" : "false") . "\n";
echo "    Contiene 'mundo': " . (strpos($texto, "mundo") !== false ? "true" : "false") . "\n";

// 13. Recorte de espacios
$textoConEspacios = "  Hola Mundo  ";
echo "13. Recorte de espacios: '" . trim($textoConEspacios) . "'\n";

// 14. Extracción de subcadenas
echo "14. Extracción (substring): " . substr($texto, 0, 4) . "\n";

// 15. Búsqueda de posición
echo "15. Posición de 'mundo': " . strpos($texto, "mundo") . "\n";

// DIFICULTAD EXTRA
echo "\nDIFICULTAD EXTRA:\n";

$palabra1 = "amor";
$palabra2 = "roma";

echo "Palabra 1: $palabra1\n";
echo "Palabra 2: $palabra2\n";

// Función para verificar si una palabra es un palíndromo
function esPalindromo($palabra) {
    return $palabra === strrev($palabra);
}

// Función para verificar si dos palabras son anagramas
function sonAnagramas($palabra1, $palabra2) {
    $palabra1 = strtolower($palabra1);
    $palabra2 = strtolower($palabra2);
    return count_chars($palabra1, 1) === count_chars($palabra2, 1);
}

// Función para verificar si una palabra es un isograma
function esIsograma($palabra) {
    return strlen($palabra) === count(array_unique(str_split(strtolower($palabra))));
}

echo "¿Son palíndromos? " . 
     (esPalindromo($palabra1) ? "true" : "false") . ", " . 
     (esPalindromo($palabra2) ? "true" : "false") . "\n";
echo "¿Son anagramas? " . (sonAnagramas($palabra1, $palabra2) ? "true" : "false") . "\n";
echo "¿Son isogramas? " . 
     (esIsograma($palabra1) ? "true" : "false") . ", " . 
     (esIsograma($palabra2) ? "true" : "false") . "\n";

?>