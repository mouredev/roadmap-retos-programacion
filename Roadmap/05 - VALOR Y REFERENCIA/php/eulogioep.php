<?php

// Función para imprimir resultados
function printMessage($message) {
    echo $message . "\n";
}

// Ejemplos de asignación por valor (tipos escalares)
$a = 5;
$b = $a; // $b es una copia del valor de $a
$b = 10; // Cambiar $b no afecta a $a
printMessage("Asignación por valor: a: $a, b: $b"); // a: 5, b: 10

// Ejemplos de asignación por referencia (arrays y objetos)
$arr1 = [1, 2, 3];
$arr2 = &$arr1; // $arr2 es una referencia a $arr1
$arr2[0] = 100; // Cambiar $arr2 afecta a $arr1
printMessage("Asignación por referencia: arr1[0]: {$arr1[0]}, arr2[0]: {$arr2[0]}"); // arr1[0]: 100, arr2[0]: 100

// Función con parámetro por valor
function modificarValor($n) {
    $n = 100; // Este cambio no afecta a la variable original
}

$x = 5;
modificarValor($x);
printMessage("x después de modificarValor: $x"); // x no cambia

// Función con parámetro por referencia
function modificarReferencia(&$arr) {
    $arr[0] = 100; // Este cambio afecta al array original
}

$array = [1, 2, 3];
modificarReferencia($array);
printMessage("array[0] después de modificarReferencia: {$array[0]}"); // array[0] cambia

// DIFICULTAD EXTRA
// Función para intercambio por valor
function intercambioPorValor($a, $b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
    return [$a, $b];
}

// Función para intercambio por referencia
function intercambioPorReferencia(&$a, &$b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
}

// Programa 1: Intercambio por valor
$num1 = 10;
$num2 = 20;
printMessage("Antes del intercambio por valor: num1 = $num1, num2 = $num2");
list($nuevoNum1, $nuevoNum2) = intercambioPorValor($num1, $num2);
printMessage("Después del intercambio por valor:");
printMessage("Variables originales: num1 = $num1, num2 = $num2");
printMessage("Nuevas variables: nuevoNum1 = $nuevoNum1, nuevoNum2 = $nuevoNum2");

// Programa 2: Intercambio por referencia
$ref1 = 30;
$ref2 = 40;
printMessage("\nAntes del intercambio por referencia: ref1 = $ref1, ref2 = $ref2");
intercambioPorReferencia($ref1, $ref2);
printMessage("Después del intercambio por referencia:");
printMessage("Variables modificadas: ref1 = $ref1, ref2 = $ref2");

?>