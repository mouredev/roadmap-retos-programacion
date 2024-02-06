<?php

    function sumaRecursiva ($a, $b){
        if ($b == 0) {
            return $a;
        } else {
            return 1 + sumaRecursiva($a, $b - 1);
        }
    }

    echo "Vamos a sumar 5 + 3 usando una función recursiva\n";
    echo sumaRecursiva(5, 3);
    echo "\n";

    function potenciaRecursiva($a, $b){
        if ($b == 0) {
            return 1;
        } else {
            return $a * potenciaRecursiva($a, $b - 1);
        }
    }

    echo "Vamos a calcular el cubo de 2 usando una función recursiva\n";
    echo potenciaRecursiva(2, 3);
    echo "\n";

    function imprimirNumeros($numero) {
        if ($numero >= 0) {
            echo $numero . " ";
            imprimirNumeros($numero - 1);
        }
    }
    
    echo "De 100 a 0 usando rercusividad: ";
    imprimirNumeros(100);
    echo "\n";

    // Extra 

    echo "Como ejercicios extras, vamos a calcular el factorial de 5 y el octavo número de la serie de Fibonacci\n";

    function factorial($n) {
        if ($n == 0) {
            return 1;
        } else {
            return $n * factorial($n - 1);
        }
    }

    echo "El numero 5! es = ".factorial(5)."\n";

    function fibonacci($n){
        if ($n == 0) {
            return 0;
        } else if ($n == 1) {
            return 1;
        } else {
            return fibonacci($n - 1) + fibonacci($n - 2);
        }
    }

    echo "El 8º numero de Fibonacci es = ".fibonacci(8)."\n";

    echo "Finalmente, vamos a comproabr el funcionamiento de amabs funciones de forma interactiva\n";

    echo "Introduce un número para calcular su factorial: ";
    $n = trim(fgets(STDIN));
    echo "El número ".$n."! es = ".factorial($n)."\n";

    echo "Introduce un número para calcular su posición en la serie de Fibonacci: ";
    $n = trim(fgets(STDIN));
    echo "El número ".$n." de Fibonacci es = ".fibonacci($n)."\n";

    