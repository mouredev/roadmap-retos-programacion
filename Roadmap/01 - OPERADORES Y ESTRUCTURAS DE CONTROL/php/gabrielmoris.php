<?php
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// Arithmetic
$addition = 1 + 1;
$substraction = 1 - 1;
$increment = $addition++;
$decrement = $addition--;
$increment2 = ++$addition;
$decrement2 = --$addition;
$multiplication = 1 * 1;
$division = 1 / 1;
$reminder = 1 % 1;
$exponential = 2 ** 2;
$negation = -$exponential;
$identity = +$exponential;

//Bitwise Operators
$and = 1 & 2;
$or = 1 | 2;
$xor = 1 ^ 2;
$not = ~1;
$shift_left = 1 << 2;
$shift_right = 1 >> 2;

// String Operators

$a = "Hello ";
$b = $a . "World!";
$b .= "!\n";

echo $b;

// Array Operators

$arr1 = ["item1" => "value1", "item2" => "value2"];
$arr2 = ["item3" => "value3"];

$union = $arr1 + $arr2;
print_r($union);

// Coparison
$equal = 1 == 1;
$identical = 1 === 1;
$not_Equal = 1 != 2;
$not_equal_2 = 1 <> 2;
$not_identical = 1 !== 2;
$less_than =  1 < 2;
$more_than = 2 > 1;
$less_or_equal = 1 <= 2;
$more_or_equal = 2 >= 1;
$less_equal_more_than = 1 <=> 2;

// Logic

$if_both_true = true and true;
$if_both_true2 = true && true;
$if_one_true = true or false;
$if_one_true2 = true || false;
$only_one_true = true xor true;
$not = !false;

// Control Structures

// conditionals
if (1 < 0) {
    return;
} elseif (1 === 0) {
    return;
} else {
    echo "Else: 1 < 0\n";
};

$ternalOp = true ? "yes\n" : "not\n";
echo $ternalOp;

// Iterators
echo "\nWhile:\n";
$index = 10;
while ($index < 56) {
    if ($index % 2 === 0 && $index % 3 !== 0 && $index !== 16) {
        echo $index;
        echo ", ";
    }
    $index++;
};
echo "\nDO While:\n";
$index = 10;
do {
    if ($index % 2 === 0 && $index % 3 !== 0 && $index !== 16) {
        echo $index;
        echo ", ";
    }
    $index++;
} while ($index < 56);


echo "\nFor Loop:\n";
for ($i = 10; $i <= 55; $i++) {
    if ($i % 2 === 0 && $i % 3 !== 0 && $i !== 16) {
        echo $i;
        echo ", ";
    }
}
echo "\nFor Each Arr:\n";
$hardcodedArr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55];

foreach ($hardcodedArr as $val) {
    if ($val % 2 === 0 && $val % 3 !== 0 && $val !== 16) {
        echo $val;
        echo ", ";
    }
}
// Switch
echo "\nSwitch:\n";
foreach ($hardcodedArr as $index) {
    switch ($index) {
        case $index % 2 === 0 && $index % 3 !== 0 && $index !== 16:
            echo $index;
            echo ", ";
            break;
        default:
            break;
    }
}

// Match
echo "\nMatch:\n";
$food = 'cake';

$return_value = match ($food) {
    'apple' => 'This food is an apple',
    'bar' => 'This food is a bar',
    'cake' => 'This food is a cake',
};
echo $return_value . "\n";
