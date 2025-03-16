<?php
/* EXERCISE:
* Show examples of all the operations you can perform with strings in your language. Some of these operations could include (search for as many as you can):
* - Accessing specific characters
* - Substrings
* - Length
* - Concatenation
* - Repetition
* - Iteration
* - Conversion to uppercase and lowercase
* - Replacement
* - Division
* - Joining
* - Interpolation
* - Verification
*/
$string = "Hello, World!";
$string2 = "";
$third_char = $string[2]; // Access Char
$substring = substr($string, 5, 7); // Extract part of the string
$length = strlen($string); // check lenght
$dramatice = $string . "!!!!!"; // Concatenate
$stars = str_repeat("*", 5); // Generates *****
for ($i = 0; $i < strlen($string); $i++) { // Iteration
    $string2 .= $string[$i]; // Prints each character
}
$uppercase = strtoupper($string2); // uppercase
$lowercase = strtolower($string2); // lowercase
$replacement = str_replace("World", "Gabriel", $string2); // replace
$array = explode(",", $replacement); // create an array using the regex as a separatore
$join = implode("", $array); // joins an array
$interpolate = "$join. I hope you had a nice day!";
$verification = strpos($interpolate, "Gabriel"); // gives the index back or false if it is not in the string
$reverse = strrev($interpolate);

/* EXTRA CHALLENGE (optional):
* Create a program that analyzes two different words and checks if they are:
* - Palindromes
* - Anagrams
* - Isograms
*/

function sort_string($string)
{
    $arr = str_Split($string);
    sort($arr); // It sorts in the original variable. Doesn't return.
    $string_worked = implode($arr);
    return $string_worked;
}

function is_isogram($string)
{
    $sorted_str = sort_string($string);

    for ($i = 0; $i < strlen($sorted_str) - 1; $i++) {
        if ($sorted_str[$i] == $sorted_str[$i + 1]) {
            return false;
        }
    }
    return true;
}

function str_check($str1, $str2)
{
    if (strrev($str1) == $str1) {
        echo "$str1 is a Palindrome.\n";
    }
    if (strrev($str2) == $str2) {
        echo "$str2 is a Palindrome.\n";
    }

    if (sort_string($str1) == sort_string($str2)) {
        echo "$str1 and $str2 are Anagrams.\n";
    }

    if (is_isogram($str1)) {
        echo "$str1 is a Isogram.\n";
    }

    if (is_isogram($str2)) {
        echo "$str1 is a Isogram.\n";
    }
}

str_check("manam", "maman");
str_check("abcde", "aba");
