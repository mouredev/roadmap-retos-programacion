<?php

// Variable global
$contadorGlobal = 0;

// 1. Función sin parámetros ni retorno
function saludar() {
    echo "¡Hola, mundo!\n";
}

// 2. Función con un parámetro y sin retorno
function saludarPersona($nombre) {
    echo "¡Hola, $nombre!\n";
}

// 3. Función con múltiples parámetros y retorno
function sumar($a, $b) {
    return $a + $b;
}

// 4. Función que demuestra una "función" dentro de otra
function operacionMatematica($a, $b) {
    $multiplicar = function($x, $y) {
        return $x * $y;
    };
    return $multiplicar($a, $b) + 10;
}

// 5. Uso de una función incorporada en PHP
function obtenerFechaActual() {
    return date('Y-m-d');
}

// 6. Demostración de variable local vs global
function incrementarContador() {
    global $contadorGlobal;
    $contadorLocal = 0;
    $contadorLocal++;
    $contadorGlobal++;
    echo "Contador local: $contadorLocal, Contador global: $contadorGlobal\n";
}

// DIFICULTAD EXTRA
function imprimirYContar($texto1, $texto2) {
    $contadorNumeros = 0;

    for ($i = 1; $i <= 100; $i++) {
        if ($i % 3 == 0 && $i % 5 == 0) {
            echo $texto1 . $texto2 . "\n";
        } elseif ($i % 3 == 0) {
            echo $texto1 . "\n";
        } elseif ($i % 5 == 0) {
            echo $texto2 . "\n";
        } else {
            echo $i . "\n";
            $contadorNumeros++;
        }
    }

    return $contadorNumeros;
}

// Llamadas a las funciones y impresión de resultados
echo "1. Función sin parámetros ni retorno:\n";
saludar();

echo "\n2. Función con un parámetro y sin retorno:\n";
saludarPersona("Alice");

echo "\n3. Función con múltiples parámetros y retorno:\n";
echo "Suma de 5 y 3: " . sumar(5, 3) . "\n";

echo "\n4. Función que demuestra una \"función\" dentro de otra:\n";
echo "Resultado de operación matemática: " . operacionMatematica(4, 5) . "\n";

echo "\n5. Uso de una función incorporada en PHP:\n";
echo "Fecha actual: " . obtenerFechaActual() . "\n";

echo "\n6. Demostración de variable local vs global:\n";
incrementarContador();
incrementarContador();

echo "\nDIFICULTAD EXTRA:\n";
$numerosPuros = imprimirYContar("Fizz", "Buzz");
echo "Números impresos sin ser reemplazados por texto: $numerosPuros\n";

?>