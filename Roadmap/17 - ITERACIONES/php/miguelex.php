<?php

    echo "Imprimiendo los numeros del 1 al 10 con un bucle for: \n";

    for ($i = 1; $i <= 10; $i++) {
        echo $i . " ";
    }

    echo "\nImprimiendo los numeros del 1 al 10 con un bucle while: \n";

    $i = 1;

    while($i <= 10) {
        echo $i . " ";
        $i++;
    }

    echo "\nImprimiendo los numeros del 1 al 10 con un bucle do-while: \n";

    $i = 1;
    while($i <= 10) {
        echo $i . " ";
        $i++;
    }

    echo "\nImprimiendo los numeros del 1 al 10 con un bucle foreach: \n";

    $numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        
    foreach ($numeros as $numero) {
        echo $numero . " ";
    }

    echo "\nImprimiendo los numeros del 1 al 10 con array map\n";
    $funcion_map = function($numero) {
        return $numero;
    };
    
    $resultado_map = array_map($funcion_map, $numeros);
    print_r($resultado_map);

    echo "\nImprimiendo los numeros del 1 al 10 con array filter\n";
    $funcion_filter = function($numero) {
        return $numero;
    };

    $resultado_filter = array_filter($numeros, $funcion_filter);
    print_r($resultado_filter);

    

