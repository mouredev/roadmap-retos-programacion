<?php
//Recursividad


function cuentaAtras($numero) {
    $stop = 0; // Condición de parada.

    if ($numero >= $stop) {   
        echo "\nVuelta nº: " . $numero;           
        cuentaAtras($numero - 1); // Reasignación de la función
    }
    return; // Detiene la reasignación
}

cuentaAtras(100);

// Ejercicio Extra

// Calcular el fatorial de un número
echo "\nCalcular el factorial de un número.";

function factorial($num) {
    if($num === 0 || $num === 1) { // Condición de parada
        echo "\nSalimos de la recursividad factorial.";
        return 1;
    }
    echo "\nVuelta nº: " . $num;
    return $num * factorial($num - 1);
}

echo "\nResultado final: " . factorial(5);


// Calcular sucesión de Fibonacci recursiva de un número
echo "\nCalcular sucesión de Fibonacci recursiva de un número.";

function fibonacci($posicion) {
    if ($posicion === 0 || $posicion === 1) {
    //echo "\nSalimos de la suseción de Fibonacci.";
    return $posicion;
    } 
    //echo "\nVuelta nº: " . $posicion;
    return fibonacci($posicion - 1) + fibonacci($posicion - 2);
}

echo "\nResultado: " . fibonacci(10);