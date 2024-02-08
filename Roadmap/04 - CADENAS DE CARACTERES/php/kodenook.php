<?php

declare(strict_types = 1);

$txt = 'hello, php!';

echo strlen($txt), PHP_EOL;
echo str_word_count($txt), PHP_EOL;
echo strpos($txt, ', p'), PHP_EOL;
echo strtoupper($txt), PHP_EOL;
echo strtolower($txt), PHP_EOL;
echo str_replace('hello', 'dolly', $txt), PHP_EOL;
echo strrev($txt), PHP_EOL;
echo trim($txt), PHP_EOL;
echo substr($txt, 4, 8), PHP_EOL;
echo var_dump(count_chars($txt, 1)), PHP_EOL;

/**
 * The function checks if a word is a palindrome, an anagram of another word, or an isogram.
 *
 * @param string word The "word" parameter is a string that represents a word.
 * @param string word2 The parameter `word2` is a string that represents the second word that will be
 * compared with `word` to check if they are anagrams.
 */
function wordType(string $word, string $word2): void {

    if ($word === strrev($word)) {
        echo 'is palindrome', PHP_EOL;
    }

    if (count_chars($word, 3) === count_chars($word2, 3)) {
        echo 'is an anagram', PHP_EOL;
    }

    if (strlen($word) === strlen(count_chars($word, 3))) {
        echo 'is isogram', PHP_EOL;
    }
}

wordType('reconocer', 'roma');