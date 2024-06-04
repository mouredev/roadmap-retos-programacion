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

$students = [
    [
        "name" => "Gaius Caesar Augustus",
        "date_of_birth" => strtotime("1990-01-01"),
        "grades" => [
            "Math" => 8.5,
            "English" => 9.0,
            "Science" => 7.8,
        ],
    ],
    [
        "name" => "Marcus Aurelius",
        "date_of_birth" => strtotime("1992-02-14"),
        "grades" => [
            "Math" => 9.2,
            "English" => 8.8,
            "Science" => 8.2,
        ],
    ],
    [
        "name" => "Lucius Claudius",
        "date_of_birth" => strtotime("1995-03-08"),
        "grades" => [
            "Math" => 7.5,
            "English" => 9.5,
            "Science" => 8.9,
        ],
    ],
    [
        "name" => "Julius Caesar",
        "date_of_birth" => strtotime("1991-04-22"),
        "grades" => [
            "Math" => 9.8,
            "English" => 9.2,
            "Science" => 9.0,
        ],
    ],
    [
        "name" => "Marcus Junius Brutus",
        "date_of_birth" => strtotime("1993-05-17"),
        "grades" => [
            "Math" => 9.0,
            "English" => 9.0,
            "Science" => 9.2,
        ],
    ],
];


// Grade average: Get a list of students by name and their average grade.
$average_grades = array_map(function ($student) {
    $average = array_sum($student['grades']) / count($student['grades']);
    return ["name" => $student["name"], "average" => $average];
}, $students);
var_dump($average_grades);

// Top students: Get a list with the names of students who have an average grade of 9 or higher.
$best_grades = array_map(function ($student) {
    $average = array_sum($student['grades']) / count($student['grades']);
    if ($average > 9) {
        return ["name" => $student["name"], "average" => $average];
    }
}, $students);

$filtered_grades = array_filter($best_grades, function ($n) {
    return !is_null($n);  // Check for non-null values
});
$best_grades = array_values($filtered_grades);
var_dump($best_grades);


// Birth date: Get a list of students ordered from youngest to oldest. Modifies the original array
usort($students, function ($student1, $student2) {
    return $student1["date_of_birth"] < $student2["date_of_birth"];
});

var_dump($students);

// Highest grade: Get the highest grade among all students.

usort($best_grades, function ($student1, $student2) {
    return $student1["average"] < $student2["average"];
});

$best_grade = $best_grades[0];
var_dump($best_grade);
