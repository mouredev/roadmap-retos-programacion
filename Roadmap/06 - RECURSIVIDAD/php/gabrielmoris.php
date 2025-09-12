<?php
/*
 * EXERCISE:
 * Understand the concept of recursion by creating a recursive function that
 * prints numbers from 100 to 0.
 */

$num = 0;

function recursive_print(&$num)
{
    do {
        echo $num . "\n";
        $num++;
    } while ($num < 101);
}

recursive_print($num);

/* EXTRA DIFFICULTY (optional):
 * Use the concept of recursion to:
 * - Calculate the factorial of a specific number (the function receives that number).
 * - Calculate the value of a specific element (according to its position) in the
 *   Fibonacci sequence (the function receives the position).
 */



function factorial($num)
{
    if ($num < 0) {
        return "Error: Factorial of a negative number doesn't exist.";
    } elseif ($num == 0 || $num == 1) {
        return 1;
    } else {
        return (int)$num * (int)factorial($num - 1); // In this way I am specifying the return type as (int)
    }
}


$num = 7;
$fac = factorial($num);
echo "Factorial of " . $num . " is " . $fac . "\n";

$memo = [];

function fibonacci($pos, &$memo)
{
    if ($pos <= 2) {
        return 1;
    }

    if (!isset($memo[$pos])) {
        $memo[$pos] = fibonacci($pos - 1, $memo) + fibonacci($pos - 2, $memo);
    }

    return $memo[$pos];
}

$fib = fibonacci($num, $memo);
echo "Fibonacci in possition " . $num . " is " . $fib . "\n";


function get_fibo_pos($num)
{

    $memo = [];
    $pos = 0;
    $fib_res = fibonacci($pos, $memo);

    do {
        $pos++;
        $fib_res = fibonacci($pos, $memo);
    } while ($num > $fib_res);


    if ($num != $fib_res) {
        return "Error: This Number doesn't belong to fibonacci sequence.";
    }

    return $pos;
}

$fibo_num = 1346269;
$posi = get_fibo_pos($fibo_num);
echo "Fibonacci possition of number " . $fibo_num . " is " . $posi . "\n";
