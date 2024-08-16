<?php

    program("incapable", "display");

    function program($word1, $word2) {

        echo isPalindrome($word1) ? "The word $word1 is a palindrome\n" : "The word $word1 is not a palindrome\n";
        echo isPalindrome($word2) ? "The word $word2 is a palindrome\n" : "The word $word2 is not a palindrome\n";

        echo areAnagrams($word1, $word2) ? "The words $word1 and $word2 are anagrams\n" : "The words $word1 and $word2 are not anagrams\n";

        echo isIsogram($word1) ? "The word $word1 is an isogram\n" : "The word $word1 is not an isogram\n";
        echo isIsogram($word2) ? "The word $word2 is an isogram\n" : "The word $word2 is not an isogram\n";

    }

    function isPalindrome($word) {

        $len = strlen($word);

        for ($i = 0; $i < $len / 2; $i++) {
            if ($word[$i] != $word[$len - $i - 1]) {
                return false;
            }
        }

        return true;

    }

    function areAnagrams($word1, $word2) {

        if (strlen($word1) != strlen($word2)) {
            return false;
        }

        $lettersWord1 = str_split($word1);
        $lettersWord2 = str_split($word2);

        sort($lettersWord1);
        sort($lettersWord2);

        return $lettersWord1 == $lettersWord2;

    }

    function isIsogram($word) {

        $letters = [];

        foreach (str_split($word) as $letter) {
            if (in_array($letter, $letters)) {
                return false;
            }
            $letters[] = $letter;
        }

        return true;

    }

?>
