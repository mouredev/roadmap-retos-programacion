<?php

    $a = 3;
    $b = 4;

    echo "\nNumber A: " . $a;
    echo "\nNumber B: " . $b;

    $sum = $a + $b;
    echo "\n$a + $b = " . $sum;

    $sub = $a - $b;
    echo "\n$a - $b = " . $sub;

    $mul = $a * $b;
    echo "\n$a * $b = " . $mul;

    $div = $a / $b;
    echo "\n$a / $b = " . $div;

    $res = $a % $b;
    echo "\n$a % $b = " . $res;

    $pow = $a ** $b;
    echo "\n$a ** $b = " . $pow;

    $a += $b;
    echo "\n$a += $b\t Number A: " . $a;

    $a -= $b;
    echo "\n$a -= $b\t Number A: " . $a;

    $a *= $b;
    echo "\n$a *= $b\t Number A: " . $a;

    $a /= $b;
    echo "\n$a /= $b\t Number A: " . $a;

    $a %= $b;
    echo "\n$a %= $b\t Number A: " . $a;

    $a++;
    echo "\n$a++\t Number A: " . $a;

    $b--;
    echo "\n$b--\t Number B: " . $b;

    if ($a == $b) {
        echo "\nNumber A equals number B";
    }

    if ($a === $b) {
        echo "\nNumber A is equal to the number B and they are of the same kind";
    } else {
        echo "\nNumber A is equal to number B and they are not of the same type";
    }

    echo ($a != $b) ? "\nThe number A is different from the number B" : "\nThe number A is not different from the number B";

    echo ($a <> $b) ? "\nThe number A is different from the number B" : "\nThe number A is not different from the number B";

    echo ($a !== $b) ? "\nThe number A and its type are different from the number B" : "\nThe number A and its type are not different from the number B";

    if ($a > $b) {
        echo "\nThe number A is greater than the number B";
    } else if ($a < $b) {
        echo "\nThe number A is less than the number B";
    } else {
        echo "\nNumber A equals number B";
    }

    while ($a > 0 and $b > 0) {
        echo "\nLoop while";
        $a--;
    }

    do {
        echo "\nLoop do while";
        $a++;
        $b++;
    } while ($a < 3 || $b < 0);

    do {
        echo "\nLoop do while";
        $a++;
        $b--;
    } while ($a xor $b);

    switch ($a <=> $b) {
        case -1:
            echo "\nNumber A is less than number B";
            break;

        case 0:
            echo "\nNumber A is equal to the number B";
            break;

        case 1:
            echo "\nNumber A is greater than the number B";
            break;

        default:
            break;

    }

    for ($i = 0; $i < 3; $i++) {
        echo "\nLoop for " . $i;
    }
      

    foreach ([1, 2, 3] as $num) {
        echo "\nLoop for each " . $num;
    }

    checkNum(2);

    program();

    function checkNum($n) {
        if ($n > 3) {
            throw new Exception("\nThe value must be equal to or less than 3");
        }
        return true;
    }

    function program() {
        echo "\nProgram:\n";
        for ($i = 10; $i <= 55; $i++) {
            if ($i % 2 == 0 && $i != 16 && $i % 3 != 0) {
                echo $i . "\t";
            }
        }
    }

?>
