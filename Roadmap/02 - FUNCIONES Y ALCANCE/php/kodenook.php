<?php

declare(strict_types=1);

function name(): void
{
    echo 'kodenook', PHP_EOL;
}

name();

function fullName(string $fname = 'my', string $lname = 'name'): void
{
    echo "$fname $lname", PHP_EOL;
}

fullName(lname: 'name');

function addition(int|float ...$num): float
{
    $result = 0;

    foreach ($num as $n) {
        $result += $n;
    }

    return $result;
}

echo addition(1, 2.5, 3.2, -2), PHP_EOL;

function ageAddition(int &$age): void
{
    $age += 5;
}

$age = 20;
ageAddition($age);
echo $age, PHP_EOL;

function first(): void
{
    echo 'first', PHP_EOL;

    function second(): void
    {
        echo 'second', PHP_EOL;
    }

    second();
}

first();

$global = 'global';
$global2 = 'global2';
function scope(): void
{
    global $global;
    $local = 'local';

    echo $local, PHP_EOL;
    echo $global, PHP_EOL;
    echo $GLOBALS['global2'], PHP_EOL;
}

scope();

/*
    Exercise
*/

function exercise(string $word1, string $word2): int
{
    $countNumbers = 0;

    foreach (range(1, 100) as $x) {
        if ($x % 3 === 0 && $x % 5 === 0) {
            echo "$word1 $word2", PHP_EOL;
        } elseif ($x % 3 === 0) {
            echo $word1, PHP_EOL;
        } elseif ($x % 5 === 0) {
            echo $word2, PHP_EOL;
        } else {
            $countNumbers++;
        }
    }

    return $countNumbers;
}

echo 'number of times it was a number and not words: ' . exercise('hello', 'php');
