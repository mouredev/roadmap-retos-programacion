<?php

    func(0);

    echo "\n---\n";

    echo fact(4);

    echo "\n---\n";

    echo fib(5);

    function func($number) {

        echo "\n" . $number;

        $number = $number + 1;

        if ($number <= 100) {
            func($number);
        }

    }

    function fact($number) {
        if ($number <= 0) {
            return 0;
        } else if ($number == 1) {
            return 1;
        } else {
            return $number * fact($number - 1);
        }
    }

    function fib($pos) {
        if ($pos <= 1) {
            return 0;
        } else if ($pos == 2 || $pos == 3) {
            return 1;
        } else {
            return fib($pos - 1) + fib($pos - 2);
        }
    }

?>
