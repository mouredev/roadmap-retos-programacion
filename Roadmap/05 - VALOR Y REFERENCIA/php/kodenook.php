<?php

declare(strict_types=1);

/*
    Assignment By Value
*/

$var1 = 3;
$var2 = $var1;

$var1 = 4;

echo $var1, PHP_EOL;
echo $var2, PHP_EOL;

/*
    Assignment By Reference
*/

$var3 = 3;
$var4 = &$var3;

$var3 = 4;

echo $var3, PHP_EOL;
echo $var4, PHP_EOL;

/*
    Exercise
*/

function ByValue(int $a, int $b): array
{
    $temp = $a;

    $a = $b;
    $b = $temp;

    return [$a, $b];
}

$original1 = 20;
$original2 = 30;
$values = ByValue($original1, $original2);

echo 'By Values', PHP_EOL;
echo 'Original Values', PHP_EOL;
echo $original1, PHP_EOL;
echo $original2, PHP_EOL;
echo 'After Function Values', PHP_EOL;
echo $values[0], PHP_EOL;
echo $values[1], PHP_EOL;

function ByReference(int &$c, &$d): array
{
    $e = $d;
    $f = $c;

    return [$e, $f];
}

$original1 = 50;
$original2 = 60;
$values = ByReference($original1, $original2);

echo 'By Reference', PHP_EOL;
echo 'Original Values', PHP_EOL;
echo $original1, PHP_EOL;
echo $original2, PHP_EOL;
echo 'After Function Values', PHP_EOL;
echo $values[0], PHP_EOL;
echo $values[1], PHP_EOL;
