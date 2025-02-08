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

$string = "String";
$string_2 = "    String 2";

// Returns the length of the string
echo "The length of string is ".strlen($string).".\n";

// Makes a string to lowercase
echo strtolower($string).".\n";

// Makes a string to uppercase
echo strtoupper($string).".\n";

// Return a part of the string
echo substr($string,0,3).".\n";

// Replace all occurrences of the search string with the replacement string
echo str_replace("String", "Hola", $string).".\n";

// Returns a string with the first character of str lowercase if that character is alphabetic.
echo lcfirst($string)."\n";

// Removes whitespace (or other characters) from the beginning of a string.
echo ltrim($string_2)."\n";

$words = ["Engineer", "Teacher", "Level", "Radar", "Listen", "Silent", "Lumberjack", "Background"];
$count = 0;



foreach ($words as $word) {
    $compared_word = lcfirst($word);
    $palindromes = strrev($compared_word);

    if($compared_word === $palindromes) {
        $count++;
    }
}

echo "There's {$count} palindromes.";


