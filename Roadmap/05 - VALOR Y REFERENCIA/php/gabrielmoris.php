<?php

/*EXERCISE:
* Provide examples of variable assignment "by value" and "by reference" based on their data type.
* Demonstrate functions with variables passed "by value" and "by reference," and how they behave when modified in each case.
(Understanding these concepts is essential in the majority of programming languages)
*/

$data = 1;

// Asign by VALUE
$by_value = $data;

// Asign by REFERENCE
$by_reference = &$data;

// Demonstration

function demonstration($data)
{
    echo "Original before modification: " . $data . "\n";

    $by_val = $data;
    $by_ref = &$data;

    $data = 100;
    echo "By value: " . $by_val . "\n" . "By Reference: " . $by_ref . "\n" . "Original after modification: " . $data . "\n";
}

demonstration(1);

/*EXTRA CHALLENGE (optional):
Create two programs that receive two parameters each, defined as previously assigned variables.
* In one case, the programs receive two parameters by value, and in the other case, by reference.
* Inside the programs, swap the values of these parameters, return them, and assign the returned values to 
* two different variables from the originals.
* Finally, print the values of the original variables and the new ones, verifying that the values have been inverted in the latter.
* Also, confirm that the original values are preserved in the former.
*/
echo " =============== CHALLENGE ===============\n";
function modify_values($val1, $val2)
{
    $temp = $val1;
    $val1 = $val2;
    $val2 = $temp;

    return [$val1, $val2];
};

function modify_references(&$variable1, &$variable2)
{
    $temp = $variable1;
    $variable1 = $variable2;
    $variable2 = $temp;

    return [$variable1, $variable2];
}

$variable1 = 1;
$variable2 = 2;

echo "Originals Initialized: " . $variable1 . ", " . $variable2 . "\n";

$res_val = modify_values($variable1, $variable2);
var_dump($res_val);
echo "Originals after modify values: " . $variable1 . ", " . $variable2 . "\n";

$res_ref = modify_references($variable1, $variable2);
var_dump($res_ref);
echo "Originals after modify references: " . $variable1 . ", " . $variable2 . "\n";
