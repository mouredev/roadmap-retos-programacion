<?php

    main();

    function main() {

        $a = 3;
        $b = 4;
        $x = 5;
        $y = 6;

        $newAB = program1($a, $b);
        $newXY = program2($x, $y);

        echo "\nA value: " . $a;
        echo "\nNew A value: " . $newAB[0];
        echo "\nB value: " . $b;
        echo "\nNew b value: " . $newAB[1];
        echo "\nX value: " . $x;
        echo "\nNew X value: " . $newXY[0];
        echo "\nY value: " . $y;
        echo "\nNew Y value: " . $newXY[1];

    }

    function program1($a, $b) {

        $temp = $a;

        $a = $b;
        $b = $temp;

        return [$a, $b];

    }

    function program2(&$x, &$y) {

        $temp = $x;

        $x = $y;
        $y = $temp;

        return [$x, $y];

    }

?>
