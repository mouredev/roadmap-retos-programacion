<?php

$num1 = 3;
$num2 = 2;

# Arithmetic Operators

// addition
echo 'sum: ' . $num1 + $num2, PHP_EOL;
// subtraction
echo 'subtraction: ' . $num1 - $num2, PHP_EOL;
// multiplication
echo 'multiplication: ' . $num1 * $num2, PHP_EOL;
// division
echo 'division: ' . $num1 / $num2, PHP_EOL;
// modulus
echo 'modulus: ' . $num1 % $num2, PHP_EOL;
// exponentiation
echo 'exponentiation: ' . $num1 ** $num2, PHP_EOL;

# Assignment Operators

echo $num3 = 1, PHP_EOL; // assignment
echo $num3 += 2, PHP_EOL; // addition
echo $num3 -= 2, PHP_EOL; // subtraction
echo $num3 *= 4, PHP_EOL; // multiplication
echo $num3 /= 4, PHP_EOL; // division
echo $num3 %= 5, PHP_EOL; // modulus

# Comparison Operators

echo 1 == 1, PHP_EOL; // equal
echo 1 === '1', PHP_EOL; // identical (value and type)
echo 1 != 2, PHP_EOL; // not equal
echo 1 <> 2, PHP_EOL; // not equal (equal to !=)
echo 1 !== '1', PHP_EOL; // not identical (value and type)
echo 2 > 1, PHP_EOL; // greater than
echo 1 < 2, PHP_EOL; // less than
echo 4 >= 3, PHP_EOL; // greater than or equal to
echo 3 <= 4, PHP_EOL; // less than or equal to
echo 1 <=> 1, PHP_EOL; // spaceship (return -1,0 or 1)


# Increment/Decrement Operators

echo ++$num1, PHP_EOL; // increments by 1 then return $num1
echo $num1++, PHP_EOL; // return $num1 then increments by 1
echo --$num1, PHP_EOL; // decrements by 1 then return $num1
echo $num1--, PHP_EOL; // return $num1 then decrements by 1

# Logical Operators

echo $num1 and $num2, PHP_EOL; // true if both are true
echo $num1 or $num2, PHP_EOL; // true if either are true
echo $num1 xor $num2, PHP_EOL; // true if either are true, but not both
echo $num1 && $num2, PHP_EOL; // true if both are true
echo $num1 || $num2, PHP_EOL; // true if either are true
echo !$num1, PHP_EOL; // true if not true

# String Operators

$word = '';

echo 'hello ' . 'world', PHP_EOL; // concatenation
echo $word .= 'word', PHP_EOL; // concatenation assignment

# Conditional Assignment

echo $num1 ? 'true' : 'false', PHP_EOL; // ternary
echo $num1 ?: 'false', PHP_EOL; // short ternary
echo $num4 ?? 'null', PHP_EOL; // null coalescing


# if

if ($num1) {
    echo $num1, PHP_EOL;
} elseif ($num2) {
    echo $num2, PHP_EOL;
} else {
    echo 'null', PHP_EOL;
}

# short hand if

if ($num1 < 10) echo 1, PHP_EOL;

# Switch

$color = 'white';

switch ($color) {
    case 'red':
        echo true, PHP_EOL;
        break;

    default:
        echo 'false', PHP_EOL;
        break;
}

# Match

echo match (8.0) {
    '8.0' => "Oh no!",
    8.0 => "This is what I expected",
}, PHP_EOL;

# Loop While

$a = 1;

while ($a <= 10) {
    echo ++$a, PHP_EOL;
}

# Loop Do-while

do {
    echo --$a, PHP_EOL;
} while ($a >> 1);

# Loop For

for ($a = 0; $a < 10; $a++) {
    echo $a, PHP_EOL;
}

# Loop Foreach

$days = ['saturday', 'sunday', 'monday'];

foreach ($days as $key => $value) {
    echo 'key: ' . $key . ', value: ' . $value, PHP_EOL;
}

# Exceptions

try {
    if ($num1 <> 1000) {
        throw new Exception("Error Processing Request", 1);
    }
} catch (\Throwable $th) {
    echo 'error: ' . $th->getMessage() . ' with code: ' . $th->getCode();
}

# Exercise

for ($i = 10; $i < 56; $i++) {
    if ($i % 2 === 0 and $i !== 16 and $i % 3 !== 0) {
        echo $i, PHP_EOL;
    }
}
