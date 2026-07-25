<?php

// Ejemplos de operadores en PHP

// 1. Operadores Aritméticos
echo "--- Operadores Aritméticos ---\n";
echo "Suma: 5 + 3 = " . (5 + 3) . "\n";
echo "Resta: 10 - 4 = " . (10 - 4) . "\n";
echo "Multiplicación: 6 * 2 = " . (6 * 2) . "\n";
echo "División: 15 / 3 = " . (15 / 3) . "\n";
echo "Módulo: 17 % 5 = " . (17 % 5) . "\n";
echo "Exponenciación: 2 ** 3 = " . (2 ** 3) . "\n";
$a = 5; $a++; echo "Incremento: \$a = 5; \$a++; \$a = $a\n";
$b = 8; $b--; echo "Decremento: \$b = 8; \$b--; \$b = $b\n";

// 2. Operadores de Asignación
echo "\n--- Operadores de Asignación ---\n";
$x = 10;
echo "Asignación simple: \$x = 10; $x\n";
$x += 5;
echo "Suma y asignación: \$x += 5; $x\n";
$x *= 2;
echo "Multiplicación y asignación: \$x *= 2; $x\n";

// 3. Operadores de Comparación
echo "\n--- Operadores de Comparación ---\n";
echo "Igualdad: 5 == '5' es " . (5 == '5' ? 'true' : 'false') . "\n";
echo "Igualdad estricta: 5 === '5' es " . (5 === '5' ? 'true' : 'false') . "\n";
echo "Desigualdad: 5 != '6' es " . (5 != '6' ? 'true' : 'false') . "\n";
echo "Mayor que: 7 > 5 es " . (7 > 5 ? 'true' : 'false') . "\n";
echo "Menor o igual que: 10 <= 10 es " . (10 <= 10 ? 'true' : 'false') . "\n";

// 4. Operadores Lógicos
echo "\n--- Operadores Lógicos ---\n";
echo "AND lógico: true && false es " . (true && false ? 'true' : 'false') . "\n";
echo "OR lógico: true || false es " . (true || false ? 'true' : 'false') . "\n";
echo "NOT lógico: !true es " . (!true ? 'true' : 'false') . "\n";

// 5. Operadores de Tipo
echo "\n--- Operadores de Tipo ---\n";
echo "instanceof: new stdClass() instanceof stdClass es " . (new stdClass() instanceof stdClass ? 'true' : 'false') . "\n";
echo "gettype(42) es " . gettype(42) . "\n";

// 6. Operadores de Bits
echo "\n--- Operadores de Bits ---\n";
echo "AND a nivel de bits: 5 & 3 = " . (5 & 3) . "\n";
echo "OR a nivel de bits: 5 | 3 = " . (5 | 3) . "\n";
echo "XOR a nivel de bits: 5 ^ 3 = " . (5 ^ 3) . "\n";
echo "Desplazamiento a la izquierda: 5 << 1 = " . (5 << 1) . "\n";

// Ejemplos de estructuras de control

// 1. Estructura Condicional: if-else
echo "\n--- Estructura Condicional: if-else ---\n";
$numero = 15;
if ($numero > 10) {
    echo "El número es mayor que 10\n";
} elseif ($numero < 10) {
    echo "El número es menor que 10\n";
} else {
    echo "El número es igual a 10\n";
}

// 2. Estructura Condicional: switch
echo "\n--- Estructura Condicional: switch ---\n";
$dia = "Lunes";
switch ($dia) {
    case "Lunes":
        echo "Hoy es Lunes\n";
        break;
    case "Martes":
        echo "Hoy es Martes\n";
        break;
    default:
        echo "Es otro día de la semana\n";
}

// 3. Estructura Iterativa: for
echo "\n--- Estructura Iterativa: for ---\n";
for ($i = 0; $i < 5; $i++) {
    echo "Iteración for: $i\n";
}

// 4. Estructura Iterativa: while
echo "\n--- Estructura Iterativa: while ---\n";
$contador = 0;
while ($contador < 3) {
    echo "Iteración while: $contador\n";
    $contador++;
}

// 5. Estructura Iterativa: do-while
echo "\n--- Estructura Iterativa: do-while ---\n";
$j = 0;
do {
    echo "Iteración do-while: $j\n";
    $j++;
} while ($j < 3);

// 6. Manejo de Excepciones: try-catch
echo "\n--- Manejo de Excepciones: try-catch ---\n";
try {
    throw new Exception("Este es un error de ejemplo");
} catch (Exception $e) {
    echo "Error capturado: " . $e->getMessage() . "\n";
} finally {
    echo "Este bloque siempre se ejecuta\n";
}

// DIFICULTAD EXTRA
echo "\n--- DIFICULTAD EXTRA ---\n";
for ($num = 10; $num <= 55; $num++) {
    if ($num % 2 == 0 && $num != 16 && $num % 3 != 0) {
        echo $num . "\n";
    }
}

?>