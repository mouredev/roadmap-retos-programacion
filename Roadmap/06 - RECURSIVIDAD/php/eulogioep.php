<?php

/**
 * Función recursiva para imprimir números del 100 al 0.
 * @param int $numero El número actual a imprimir.
 */
function imprimirNumeros($numero) {
    // Caso base: si el número es menor que 0, terminamos la recursión
    if ($numero < 0) {
        return;
    }
    
    // Imprimimos el número actual
    echo $numero . " ";
    
    // Llamada recursiva con el número decrementado
    imprimirNumeros($numero - 1);
}

/**
 * Función recursiva para calcular el factorial de un número.
 * @param int $n El número del cual calcular el factorial.
 * @return int El factorial del número.
 */
function factorial($n) {
    // Casos base: factorial de 0 y 1 es 1
    if ($n == 0 || $n == 1) {
        return 1;
    }
    
    // Llamada recursiva: n * factorial(n-1)
    return $n * factorial($n - 1);
}

/**
 * Función recursiva para calcular el valor de un elemento en la sucesión de Fibonacci.
 * @param int $posicion La posición del elemento en la sucesión de Fibonacci.
 * @return int El valor del elemento en la posición dada.
 */
function fibonacci($posicion) {
    // Casos base: posiciones 0 y 1 de Fibonacci son 0 y 1 respectivamente
    if ($posicion == 0) {
        return 0;
    }
    if ($posicion == 1) {
        return 1;
    }
    
    // Llamada recursiva: suma de los dos elementos anteriores
    return fibonacci($posicion - 1) + fibonacci($posicion - 2);
}

// Pruebas de las funciones
echo "Números del 100 al 0:\n";
imprimirNumeros(100);
echo "\n\n";

$numeroFactorial = 5;
echo "Factorial de $numeroFactorial: " . factorial($numeroFactorial) . "\n";

$posicionFibonacci = 7;
echo "Elemento en la posición $posicionFibonacci de Fibonacci: " . fibonacci($posicionFibonacci) . "\n";

?>