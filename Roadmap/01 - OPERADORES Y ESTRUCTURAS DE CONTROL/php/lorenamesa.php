<?php

/****************** OPERADORES ****************/

// Aritméticos
$a = 5;
$b = 3;
echo "Identidad: " . +$a . "\n";  // Conversión de $a a int o float según el caso.
echo "Opuesto: " . -$a . "\n";  // Opuesto de $a.
echo "Suma: " . ($a + $b) . "\n"; // Suma de $a y $b.
echo "Resta: " . ($a - $b) . "\n"; // Diferencia de $a y $b.
echo "Multiplicación: " . ($a * $b) . "\n"; // Producto de $a y $b.
echo "División: " . ($a / $b) . "\n"; // Cociente de $a y $b.
echo "Modular: " . ($a % $b) . "\n"; // Resto de $a dividido por $b.
echo "Exponenciación: " . ($a ** $b) . "\n"; // Resultado de elevar $a a la potencia $b

// Incremento/Decremento
echo "Pre-incremento: " . ++$a . "\n";  // Incrementa $a en uno, y luego retorna $a.
echo "Post-incremento: " . --$a . "\n";  // Retorna $a, y luego incrementa $a en uno.
echo "Pre-decremento: " . $a++ . "\n"; // Decrementa $a en uno, luego retorna $a.
echo "Post-decremento: " . $a-- . "\n"; // Retorna $a, luego decrementa $a en uno.

// Asignación
$a = 3;
echo $a . "\n"; // Devuelve 3
$a += 5;
echo $a . "\n"; // Devuelve 8
$a -= 2;
echo $a . "\n"; // Devuelve 7

$b = "Hola";
echo $b . "\n"; // Devuelve "Hola"
$b .= " PHP\n";
echo $b; // Devuelve "Hola PHP"

// Comparación
$a = 5;
$b = 8;
$c = 3;

echo "Igual: " . ($a == $b) . "\n"; // 	true si $a es igual a $b después de la manipulación de tipos.
echo "Idéntico: " . ($a === $b) . "\n"; // true si $a es igual a $b, y son del mismo tipo.
echo "Diferente: " . ($a != $b) . "\n"; // true si $a no es igual a $b después de la manipulación de tipos.
echo "Diferente: " . ($a <> $b) . "\n"; // true si $a no es igual a $b después de la manipulación de tipos.
echo "Distinto: " . ($a !== $b) . "\n"; // true si $a no es igual a $b, o si no son del mismo tipo.
echo "Menor que: " . ($a < $b) . "\n"; // true si $a es estrictamente menor que $b.
echo "Mayor que: " . ($a > $b) . "\n"; // true si $a es estrictamente mayor que $b.
echo "Menor o igual que: " . ($a <= $b) . "\n"; // true si $a es menor o igual que $b.
echo "Mayor o igual que: " . ($a >= $b) . "\n"; // true si $a es mayor o igual que $b.
echo "Nave espacial: " . ($a <=> $b) . "\n"; // Un integer menor que, igual a, o mayor que cero cuando $a es respectivamente menor que, igual a, o mayor que $b. Disponible a partir de PHP 7.
echo "Fusión de null: " . ($a ?? $b ?? $c) . "\n"; // El primer operando de izquierda a derecha que exista y no sea null. null si no hay valores definidos y no son null

// Lógicos
echo "And: " . ($a and $b) . "\n"; // true si tanto $a como $b son true.
echo "Or: " . ($a or $b) . "\n"; // true si cualquiera de $a o $b es true.
echo "Xor: " . ($a xor $b) . "\n"; // true si $a o $b es true, pero no ambos.
echo "Not: " . !$a . "\n"; // true si $a no es true.
echo "And: " . ($a && $b) . "\n"; // true si tanto $a como $b son true.
echo "Or: " . ($a || $b) . "\n"; // true si cualquiera de $a o $b es true.

// Bits
$a = 1;
$b = 0;

echo "Y: " . ($a & $b) . "\n"; // Los bits que están activos en ambos $a y $b son activados.
echo "O inclusivo: " . ($a | $b) . "\n"; // Los bits que están activos ya sea en $a o en $b son activados.
echo "O exclusivo: " . ($a ^ $b) . "\n"; // Los bits que están activos en $a o en $b, pero no en ambos, son activados.
echo "No: " . ~ $b . "\n"; // Los bits que están activos en $a son desactivados, y viceversa.
echo "Desplazamiento a la izquierda: " . ($a << $b) . "\n"; // Desplaza los bits de $a, $b pasos a la izquierda (cada paso quiere decir "multiplicar por dos").
echo "Desplazamiento a la derecha: " . ($a >> $b) . "\n"; // Desplaza los bits de $a, $b pasos a la derecha (cada paso quiere decir "dividir por dos").

/****************** ESTRUCTURAS DE CONTROL ****************/
$a = 3;
$b = 5;
$c = 7;

if ($a < $b) {
    echo '$a es menor que $b' . "\n";
} elseif ($a > $b) {
    echo '$a es mayor que $b' . "\n";
} else {
    echo '$a y $b son iguales' . "\n";
}

while ($a < $c) {
    echo '$a es menor que $c' . "\n";
    $a++;
}

do {
    echo '$a es menor que $b' . "\n";
    $a++;
} while ($a < $b);

for ($i = 0; $i <= $b; $i++) {
    echo 'Estoy imprimiendo numeros hasta el valor de $b: ' . $i . "\n";
}

$arrayValues = [0, 1, 2];
echo "Los valores de mi array son:\n";
foreach ($arrayValues as $arrayValue) {
    echo "$arrayValue\n";
}

switch ($a) {
    case 0:
        echo "a es igual a 0";
        break;
    case 1:
        echo "a es igual a 1";
        break;
    case 2:
        echo "a es igual a 2";
        break;
    default:
        echo "a es mayor a 2";
    echo "\n";
}


/****************** DIFICULTAD EXTRA ****************/
echo "****************EJERCICIO EXTRA:****************\n";

for ($i = 10; $i <= 55; $i++) {
    if (($i == 16) || ($i % 3 === 0)) {
        continue;
    }
    if ($i % 2 === 0) {
        echo $i . "\n";
    }
}
