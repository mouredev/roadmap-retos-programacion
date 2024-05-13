<?php

/*
*EXERCISE:
* - Create examples of basic functions that represent the different
* possibilities of the language:
* - Without parameters or return, with one or more parameters, with return...
* - Check if you can create functions within functions.
* - Use some examples of functions already created in the language.
* - Test the concept of LOCAL and GLOBAL variables.
* - You must print the result of all the examples to the console.
* (and keep in mind that each language may have more or fewer possibilities)
* EXTRA DIFFICULTY (optional):
* Create a function that receives two string parameters and returns a number.
* - The function prints all the numbers from 1 to 100. Considering that:
* - If the number is a multiple of 3, it displays the string of the first parameter.
* - If the number is a multiple of 5, it displays the string of the second parameter.
* - If the number is a multiple of 3 and 5, it displays the two concatenated strings.
* - The function returns the number of times the number has been printed instead of the texts.
* Pay special attention to the syntax you must use in each case.
* Each language follows conventions that you must respect for the code to be understood.
*/

// simple function

function simplicity()
{
    echo "ok";
};

// One param without return function
function one_param($param)
{
    echo  "This is the param: " . $param . "\n";
};

one_param("hi!");

// 2 Params with return
function two_params_Return($first, $second)
{
    return $first + $second;
}

$asign_to_var = two_params_Return(1, 5);
echo $asign_to_var . "\n";

// Functions in functions

function outside($res)
{
    function inside($first, $second)
    {
        return $first + $second;
    };

    return inside($res, 1);
};

echo outside(5) . "\n";

// Recursive

$i = 0;

function make_i_great_again()
{
    global  $i; // in this way I access it as a global from outside. Otherwise it behaves local.
    if ($i > 99) {
        return $i;
    };
    $i++;
    return make_i_great_again($i);
}

echo make_i_great_again() . "\n";
// native methods

$hardcodedArr = [10, 11, 12];

function sum($carry, $item)
{
    return $carry + $item;
}

$result = array_reduce($hardcodedArr, 'sum', 0);
echo $result . "\n";

// Global variable: Outside any function or class
$globalVar = "This is a global variable";

// Local variable: Inside a function or class
function myFunction()
{
    $localVar = "This is a local variable";
    echo $localVar; // Output: "This is a local variable"
}
// echo $localVar; // error

function flix_bus($str, $str2)
{
    $num_count = 0;
    for ($i = 0; $i <= 100; $i++) {
        if ($i % 3 == 0 && $i % 5 == 0) {
            echo $str . "," . $str2;
        } elseif ($i % 3 == 0) {
            echo $str . ",";
        } elseif ($i % 5 == 0) {
            echo $str2 . ",";
        } else {
            echo $i . ",";
            $num_count++;
        }
    }

    return $num_count;
}

$result = flix_bus("Flix", "Bus");

echo "\n Result: " . $result . "\n";
