<?php
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

// Función recursiva para imprimir números del 100 al 0
function imprimirNumeros($num) {
    if ($num < 0) {
        return; // La función termina cuando $num es menor que 0
    }
    echo $num . "\n"; // Imprime el número seguido de un salto de línea
    imprimirNumeros($num - 1); // Llamada recursiva con $num decrementado en 1
}

echo "Imprimiendo números del 100 al 0:\n";
imprimirNumeros(100);

// Función recursiva para calcular el factorial de un número
function factorial($n) {
    if ($n === 0 || $n === 1) {
        return 1; // El factorial de 0 y 1 es 1
    }
    return $n * factorial($n - 1); // Llamada recursiva con $n decrementado en 1
}

$numero = 5;
echo "Factorial de $numero: " . factorial($numero) . "\n";

// Función recursiva para calcular el valor de un elemento en la sucesión de Fibonacci
function fibonacci($n) {
    if ($n <= 1) {
        return $n; // Si $n es 0 o 1, devuelve $n
    }
    return fibonacci($n - 1) + fibonacci($n - 2); // Llamada recursiva con $n decrementado en 1 y 2
}

$posicion = 6;
echo "Valor en la posición $posicion de la sucesión de Fibonacci: " . fibonacci($posicion) . "\n";

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

?>
