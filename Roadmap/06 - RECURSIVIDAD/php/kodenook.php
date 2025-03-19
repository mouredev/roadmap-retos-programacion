<?php

declare(strict_types = 1);

/**
 * The above PHP function uses recursion to print numbers from the input number down to 0.
 *
 * @param int number The function `recursion` takes an integer parameter `number` and recursively
 * prints the value of `number` until it reaches 0. Each time it prints the value of `number`, it
 * decrements the value by 1 before calling itself recursively.
 */
function recursion(int $number): void
{
    echo $number, PHP_EOL;
    if ($number > 0) recursion(--$number);
}

recursion(100);

/*
    Exercise
*/

/**
 * The function calculates the factorial of a given number recursively in PHP.
 *
 * @param int number The `number` parameter in the `factorial` function represents the integer for
 * which you want to calculate the factorial. The factorial of a non-negative integer n is the product
 * of all positive integers less than or equal to n.
 * @param int result The `result` parameter in the `factorial` function is used to keep track of the
 * intermediate result as the factorial calculation progresses through recursive calls. It starts with
 * a default value of 1 and gets updated with the multiplication of the current number and the previous
 * result in each recursive call.
 */
function factorial(int $number, int $result = 1): void
{
    if ($number > 1) factorial($number - 1, $number * $result);
    else echo $result, PHP_EOL;
}

factorial(5);

/**
 * The function calculates the Fibonacci sequence up to a given number using recursion in PHP.
 *
 * @param int number The function you provided is a recursive implementation of the Fibonacci sequence.
 * It calculates the Fibonacci number at a given position in the sequence.
 * @return int the nth number in the Fibonacci sequence, where n is the input number provided to the
 * function.
 */
function fibonacci(int $number): int
{
    if ($number > 2) return fibonacci($number - 1) + fibonacci($number - 2);
    else return 1;

}

echo fibonacci(7);