<?php

// Variables por valor y referencia

$a = 25;
$b = $a; // Por valor, lo que viene siendo una copia
$b = 30;
echo "Número a vale: " . $a . "\n" . "Número b vale: " . $b ."\n";
$c = &$a; // Por referencia.
$c = 30;
echo "Número a vale: " . $a . "\n" . "Número c vale: " . $c ."\n";


// Funciones

function duplicar_valor($numero) {
    // Modificamos la copia local, no afecta al exterior.
    $numero = $numero * 2;
}


function duplicar_valor_referencia(&$numero) {
    // Modificamos directamente la variable externa.
    $numero = $numero * 2;
}


$original = 10;
echo "\n--- Prueba de valor ---";
echo "\nValor inicial: " . $original;

duplicar_valor($original); // Llamamos a la función por valor.
echo "\nTras duplicar_valor, original sigue valiendo: " . $original; // Debería seguir siendo 10


echo "\n\n--- Prueba por Referencia ---";
echo "\nValor inicial: " . $original;

duplicar_valor_referencia($original); // Llamamos a la función por referencia
echo "\nTras duplicar_valor_referencia, original ahora vale: " . $original; // ¡Debería ser 20!

// Dificultad extra.

// Por valor
$originalA = 'Perro';
$originalB = 'Gato';

echo "\nOrden Normal: \n" . $originalA ."\n" . $originalB . "\n";

function animales($originalA, $originalB) {
    $temporal = $originalB;
    $originalB = $originalA;
    $originalA = $temporal;
    
    return [$originalA, $originalB];
}

[$nuevoValorA, $nuevoValorB] = animales($originalA, $originalB);

echo "--- PROGRAMA1 : POR VALOR ---\n";
echo "Originales : $originalA y $originalB\n";
echo "Nuevo orden: $nuevoValorA y $nuevoValorB\n";

// Por referencia

function animales_referencia(&$originalA, &$originalB) {
    $temporal = $originalB;
    $originalB = $originalA;
    $originalA = $temporal;

    return [$originalA, $originalB];
}

[$nuevoValorC, $nuevoValorD] = animales_referencia($originalA, $originalB);

echo "--- PROGRAMA2 : POR REFERENCIA ---\n";
echo "Originales : $originalA y $originalB\n";
echo "Nuevo orden: $nuevoValorC y $nuevoValorD\n";
