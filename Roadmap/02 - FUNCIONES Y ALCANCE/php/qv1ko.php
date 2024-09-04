<?php

$a = 3;

main();

function main() {

    func1();

    echo func2();

    func3($GLOBALS['a'], "\nParameterized and non-return function:\nGlobal variable A: ");

    echo func4(-4, "\nFunction with return and with parameters:\nGlobal variable A: ");

    echo "\nProgram:";
    echo "\nNumber of times a text was not printed: " . program("zip", "zap");

}

function func1() {
    $b = 4;
    echo "\nFunction without return and without parameters:\nGlobal variable A: " . $GLOBALS['a'] . "\nLocal variable B: " . $b;
}

function func2() {
    return "\nFunction with return and without parameters:\nGlobal variable A: " . $GLOBALS['a'];
}

function func3($num, $str) {
    echo $str . $num;
}

function func4($num, $str) {
    return $str . $GLOBALS['a'] . "\nAbsolute number: " . abs($num);
}

function program($zip, $zap) {

    $count = 0;

    for ($i = 1; $i <= 100; $i++) {
        if ($i % 3 == 0 && $i % 5 == 0) {
            echo "\n";
            echo $zip . $zap;
        } elseif ($i % 3 == 0) {
            echo "\n";
            echo $zip;
        } elseif ($i % 5 == 0) {
            echo "\n";
            echo $zap;
        } else {
            $count++;
        }
    }

    return $count;

}

?>
