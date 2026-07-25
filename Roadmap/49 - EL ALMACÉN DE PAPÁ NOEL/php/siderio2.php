<?php

/**
 * @author Desiderio Martínez Silva aka siderio2
 * @version 1.0
 * @link https://github.com/siderio2
 * @see https://retosdeprogramacion.com/roadmap/
 *
 * PHP implementation of the Santa Claus Warehouse 49 exercise from Mouredev Roadmap
 *
 * Generates a random key of 4 non-repeating characters from the set {A, B, C, 1, 2, 3}
 *
 * Then asks the user to try to guess the key, 10 attempts given
 *
 * After each attempt, the program tells if a character is in the correct position,
 * if it is in the key but in the wrong position, or if it is not in the key
 *
 */

// Defining constants
const KEY_LENGTH = 4;
const ATTEMPTS = 10;
const LETTERS = ['A', 'B', 'C'];
const NUMBERS = ['1', '2', '3'];
define('ALPHABET', array_merge(LETTERS, NUMBERS));

/**
 * Checks if the given guess is valid.
 *
 * A guess is valid if it has exactly $KEY_LENGTH characters and only contains
 * characters from $LETTERS and $NUMBERS.
 *
 * @param string $guess
 * @return string "OK" if the guess is valid, an error message otherwise
 */
function checkGuess(string $guess): string
{
  if (strlen($guess) != KEY_LENGTH) {
    return "The key must be exactly " . KEY_LENGTH . " characters long\n";
  }

  for ($i = 0; $i < KEY_LENGTH; $i++) {
    if (!in_array($guess[$i], LETTERS) && !in_array($guess[$i], NUMBERS)) {
      return "Unauthorized character; only characaters in this list are allowed: - " . implode(" ", ALPHABET) . " -\n";
    }
  }

  return "OK";
}

/**
 * Generates a feedback string for a given guess and key.
 *
 * The feedback string tells if each character of the guess is in the correct
 * position, if it is in the key but in the wrong position, or if it is not in
 * the key.
 *
 * @param string $guess The guess to generate the feedback for
 * @param string $key The key to compare the guess against
 * @return string A string with the feedback, with "correct",
 * "wrong position", or "incorrect" appended to each character
 */
function generateFeedback(string $guess, string $key): string
{
  $feedback = "\n";
  for ($i = 0; $i < KEY_LENGTH; $i++) {
    if ($guess[$i] === $key[$i]) {
      $feedback .= $guess[$i] . " -> correct\t";
    } elseif (strpos($key, $guess[$i]) !== false) {
      $feedback .= $guess[$i] . " -> wrong position\t";
    } else {
      $feedback .= $guess[$i] . " -> incorrect\t";
    }
  }
  $feedback .= "\n\n";

  return $feedback;
}

/**
 * Generates a random key of $KEY_LENGTH characters from the set
 * defined in the ALPHABET constant.
 *
 * @return string A random key of $KEY_LENGTH characters
 */
function generateKey(): string
{
  $key = [];
  $random_keys = array_rand(ALPHABET, KEY_LENGTH);
  for ($j = 0; $j < KEY_LENGTH; $j++) {
    $key[] = ALPHABET[$random_keys[$j]];
  }
  $key = implode("", $key);

  return $key;
}

$key = generateKey();
$unguessed = TRUE; // Initializing unguessed flag

// Main loop
for ($i = 0; $i < ATTEMPTS; $i++) {
  $guess = readline("Attempt #" . ($i + 1) . ". Guess the Santa's warehouse key: ");
  $guess = strtoupper($guess);

  $check = checkGuess($guess); // Check if the guess is valid
  if ($check !== "OK") {
    $i--; // Attempt doesn't count
    echo "\n*ERROR* -> " . $check . "\n";
    continue; // Skip the rest of the loop if the guess is invalid
  }

  if ($guess === $key) { // Check if the guess is correct
    echo "\nCONGRATS!! We've got the key, now Santa can open his warehouse!\n\n";
    $unguessed = FALSE; // Changing the unguessed flag
    break;  // Exit the loop if the guess is correct
  }

  // If the guess is valid but not correct, generate feedback and print it
  echo (generateFeedback($guess, $key));
}

// Final message if the key was not guessed
if ($unguessed) {
  echo "Shame on you: nobody will have presents this year. The key was: " . $key . "\n\n";
}
