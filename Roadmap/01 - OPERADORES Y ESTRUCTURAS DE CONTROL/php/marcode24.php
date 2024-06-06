<?php

/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// Operadores aritméticos
$suma = 5 + 3;
$resta = 10 - 4;
$multiplicacion = 6 * 7;
$division = 20 / 4;
$modulo = 15 % 4;

echo "Operadores Aritméticos:\n";
echo "Suma: $suma\n";
echo "Resta: $resta\n";
echo "Multiplicación: $multiplicacion\n";
echo "División: $division\n";
echo "Módulo: $modulo\n";

// Operadores lógicos
$and = true && false;
$or = true || false;
$not = !true;

echo "\nOperadores Lógicos:\n";
echo "AND: " . var_export($and, true) . "\n";
echo "OR: " . var_export($or, true) . "\n";
echo "NOT: " . var_export($not, true) . "\n";

// Operadores de comparación
$igual = 5 == '5';
$estrictamenteIgual = 5 === '5';
$diferente = 10 !== 5;
$mayorQue = 15 > 10;
$menorQue = 7 < 12;

echo "\nOperadores de Comparación:\n";
echo "Igual (==): " . var_export($igual, true) . "\n";
echo "Estrictamente Igual (===): " . var_export($estrictamenteIgual, true) . "\n";
echo "Diferente (!=): " . var_export($diferente, true) . "\n";
echo "Mayor Que (>): " . var_export($mayorQue, true) . "\n";
echo "Menor Que (<): " . var_export($menorQue, true) . "\n";

// Operadores de asignación
$x = 10;
$x += 5; // equivalente a $x = $x + 5
$y = 20;
$y *= 2; // equivalente a $y = $y * 2

echo "\nOperadores de Asignación:\n";
echo "x: $x\n";
echo "y: $y\n";

// Operadores bitwise
$bitwiseAnd = 5 & 3; // AND
$bitwiseOr = 5 | 3; // OR
$bitwiseXor = 5 ^ 3; // XOR
$bitwiseNot = ~5; // NOT
$leftShift = 5 << 1; // Left Shift
$rightShift = 5 >> 1; // Right Shift
$zeroFillRightShift = 5 >> 1; // Zero-fill Right Shift

echo "\nOperadores Bitwise:\n";
echo "Bitwise AND (&): $bitwiseAnd\n";
echo "Bitwise OR (|): $bitwiseOr\n";
echo "Bitwise XOR (^): $bitwiseXor\n";
echo "Bitwise NOT (~): $bitwiseNot\n";
echo "Left Shift (<<): $leftShift\n";
echo "Right Shift (>>): $rightShift\n";
echo "Zero-fill Right Shift (>>>): $zeroFillRightShift\n";

// Estructuras de control
// Condicionales
$edad = 18;
if ($edad >= 18) {
  echo "\nEres mayor de edad.\n";
} else {
  echo "\nEres menor de edad.\n";
}

// Iterativas
echo "\nNúmeros entre 10 y 55 (pares, no 16 ni múltiplos de 3):\n";
for ($i = 10; $i <= 55; $i++) {
  if ($i % 2 === 0 && $i !== 16 && $i % 3 !== 0) {
    echo "$i\n";
  }
}

// Excepciones
try {
  throw new Exception('Este es un ejemplo de excepción.');
} catch (Exception $error) {
  echo "\nExcepción: {$error->getMessage()}\n";
}

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

?>
