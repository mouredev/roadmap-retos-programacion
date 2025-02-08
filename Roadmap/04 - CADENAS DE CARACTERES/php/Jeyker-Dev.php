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
echo trim($string_2)."\n";

// Returns the reversed string
echo strrev($string)."\n";

class Funcionality
{
    public function palindromes(string $word_1, string $word_2): string
    {
        $word_1 = trim($word_1);
        $word_2 = trim($word_2);

        $convert_word = $this->toLowerAndReversed($word_1);
        $convert_word_2 = $this->toLowerAndReversed($word_2);

        if($convert_word === $word_1) {
            echo "The First Word is a Palindrome.\n";
        }

        if($convert_word_2 === $word_2) {
            echo "The Second Word is a Palindrome.\n";
        }

        return "The words ain't palindromes.\n";
    }

    public function toLowerAndReversed(string $word): string
    {
        $lower_word = strtolower($word);
        return $reversed_word =  strrev($lower_word);
    }
}

echo "This is a program where you write two words and then it will analyze if the words are palindromes, anagrams or isograms.\n";

echo "Write the first word: ";
$word_1 = fgets(STDIN);

echo "Write the second word: ";
$word_2 = fgets(STDIN);

$instance = new Funcionality();

$instance->palindromes($word_1, $word_2);



