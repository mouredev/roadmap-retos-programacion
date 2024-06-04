<?php
/*
 * EXERCISE:
 * Explore the concept of higher-order functions in your language
 * by creating simple examples (of your choice) that demonstrate their operation.
 */
function sum($num1, $num2)
{
    return $num1 + $num2;
}

function sum5($sumfn, $num)
{
    return $sumfn(5, $num);
}

echo sum5("sum", 5) . "\n";

$arr = [1, 2, 3, 4, 5, "potato"];

$filtered = array_map(function ($n) {
    if (is_string($n)) {
        return $n;
    }
}, $arr);

$filtered = array_filter($filtered, function ($n) {
    return !is_null($n);  // Check for non-null values
});
$filtered = array_values($filtered);
var_dump($filtered);

 /*
 * EXTRA DIFFICULTY (optional):
 * Given a list of students (with their names, date of birth, and
 * list of grades), use higher-order functions to perform the following
 * processing and analysis operations:
 * - Grade average: Get a list of students by name and their average grade.
 * - Top students: Get a list with the names of students who have an average
 *   grade of 9 or higher.
 * - Birth date: Get a list of students ordered from youngest to oldest.
 * - Highest grade: Get the highest grade among all students.
 * - A grade must be between 0 and 10 (decimal values allowed).
 */