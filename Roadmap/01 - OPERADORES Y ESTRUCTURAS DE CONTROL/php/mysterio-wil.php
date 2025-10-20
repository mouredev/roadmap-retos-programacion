<?php

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

echo "### OPERADORES ###\n";

// Operadores Aritméticos
echo "\n--- Aritméticos ---\n";
$a = 10;
$b = 3;
echo "Suma: 10 + 3 = " . ($a + $b) . "\n";
echo "Resta: 10 - 3 = " . ($a - $b) . "\n";
echo "Multiplicación: 10 * 3 = " . ($a * $b) . "\n";
echo "División: 10 / 3 = " . ($a / $b) . "\n";
echo "Módulo: 10 % 3 = " . ($a % $b) . "\n";

// Operadores Lógicos
echo "\n--- Lógicos ---\n";
echo "AND (true && false): " . (true && false ? 'true' : 'false') . "\n";
echo "OR (true || false): " . (true || false ? 'true' : 'false') . "\n";

// Operadores de Comparación
echo "\n--- Comparación ---\n";
echo "Igualdad (10 == '10'): " . (10 == '10' ? 'true' : 'false') . "\n";
echo "Identidad (10 === '10'): " . (10 === '10' ? 'true' : 'false') . "\n";

// Operadores de Asignación
echo "\n--- Asignación ---\n";
$x = 5;
$x += 2;
echo "Suma y asignación: x += 2 -> x = $x\n";

// Operadores de Bits
echo "\n--- Bits ---\n";
$p = 10; // 1010
$q = 3;  // 0011
echo "AND a nivel de bits (10 & 3): " . ($p & $q) . "\n";
echo "OR a nivel de bits (10 | 3): " . ($p | $q) . "\n";

/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 */

echo "\n### ESTRUCTURAS DE CONTROL ###\n";

// Condicionales
echo "\n--- Condicionales (if, else) ---\n";
$edad = 18;
if ($edad < 18) {
    echo "Eres menor de edad.\n";
} else {
    echo "Eres mayor de edad.\n";
}

// Iterativas
echo "\n--- Iterativas (for) ---\n";
for ($i = 1; $i <= 3; $i++) {
    echo $i . "\n";
}

echo "\n--- Iterativas (while) ---\n";
$contador = 3;
while ($contador > 0) {
    echo $contador . "\n";
    $contador--;
}

// Excepciones
echo "\n--- Excepciones (try, catch) ---\n";
try {
    throw new Exception("Este es un error de ejemplo");
} catch (Exception $e) {
    echo "Se capturó una excepción: " . $e->getMessage() . "\n";
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 */

echo "\n### DIFICULTAD EXTRA ###\n";
for ($numero = 10; $numero <= 55; $numero++) {
    if ($numero % 2 == 0 && $numero != 16 && $numero % 3 != 0) {
        echo $numero . "\n";
    }
}

?>
