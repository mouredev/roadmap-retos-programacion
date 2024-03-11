<?php

declare(strict_types=1);

/*
    Stack
*/

$letters = ['a', 'b', 'c', 'd'];

// Insert
array_unshift($letters, 'e');
array_unshift($letters, 'f');

echo var_dump($letters), PHP_EOL;

// Delete
array_shift($letters);

echo var_dump($letters), PHP_EOL;

/*
Queue
*/

$letters = ['a', 'b', 'c', 'd'];

// Insert

array_push($letters, 'e', 'f');

echo var_dump($letters), PHP_EOL;

// Delete

array_shift($letters);

echo var_dump($letters), PHP_EOL;

/*
    Exercise
*/

/**
 * The function `webNavigation` allows users to navigate through web URLs by storing and displaying the
 * current and previous URLs in a stack.
 */
function webNavigation()
{
    $stack = [];
    $option = '';
    while ($option != 'exit') {

        echo 'give a url or next, before, exit', PHP_EOL;
        $option = readline();

        switch ($option) {
            case 'next':
                break;
            case 'before':
                array_shift($stack);
                $web = $stack[count($stack) - 1];
                echo 'you are in ' . $web, PHP_EOL;
                break;
            default:
                array_unshift($stack, $option);
                echo 'you are in ' . $option, PHP_EOL;
                break;
        }
    }
}

webNavigation();

/**
 * The function `sharedPrint` allows users to add documents to a queue and print them one by one until
 * the user chooses to exit.
 */
function sharedPrint()
{
    $queue = [];
    $option = '';

    while ($option != 'exit') {

        echo 'give a document or print, exit', PHP_EOL;
        $option = readline();

        switch ($option) {
            case 'print':
                $document = array_shift($queue);
                echo 'you printed ' . $document, PHP_EOL;
                break;
            default:
                array_push($queue, $option);
                break;
        }
    }
}

sharedPrint();
