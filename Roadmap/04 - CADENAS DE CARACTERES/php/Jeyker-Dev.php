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
$string_3 = "Another";

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

    public function anagrams(string $word_1, string $word_2): string
    {
        $word_1 = strtolower(trim($word_1));
        $word_2 = strtolower(trim($word_2));

        $sorted_word_1 = $this->sortString($word_1);
        $sorted_word_2 = $this->sortString($word_2);

        if ($sorted_word_1 === $sorted_word_2) {
            return "The words are anagrams.\n";
        } else {
            return "The words are not anagrams.\n";
        }
    }

    public function isograms(string $word_1, string $word_2)
    {
        $word_1 = strtolower(trim($word_1));
        $word_2 = strtolower(trim($word_2));

        $letters = str_split($word_1);
        $letters_2 = str_split($word_2);

        $is_isogram = $this->hasRepeatingLetters($letters);
        $is_isogram_2 = $this->hasRepeatingLetters($letters);

        if($is_isogram === true) {
            echo "The First Word is a Isogram.\n";
        }

        if($is_isogram_2 === true) {
            echo "The Second Word is a Isogram.\n";
        }
    }

    public function hasRepeatingLetters(array $letters): bool
    {
        foreach ($letters as $letter => $count) {
            if ($count > 1) {
                return true;
            }
        }

        return false;
    }

    private function sortString(string $word): string
    {
        $letters = str_split($word);
        sort($letters);
        return implode('', $letters);
    }

    public function toLowerAndReversed(string $word): string
    {
        $lower_word = strtolower($word);
        return $reversed_word =  strrev($lower_word);
    }
}

$instance = new Funcionality();

$instance->isograms($string,$string_3);

echo "This is a program where you write two words and then it will analyze if the words are palindromes, anagrams or isograms.\n";

echo "Write the first word: ";
$word_1 = fgets(STDIN);

echo "Write the second word: ";
$word_2 = fgets(STDIN);



$instance->palindromes($word_1, $word_2);
$instance->anagrams($word_1, $word_2);
$instance->isograms($word_1, $word_2);



