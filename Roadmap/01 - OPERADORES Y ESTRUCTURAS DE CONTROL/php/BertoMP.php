<?php

// OPERADORES ARITMÉTICOS
echo "OPERADORES ARITMÉTICOS<br/>";
$firstNumber = 7;
$secondNumber = 2;
$result = 0;

// Operador suma (+)
$result = $firstNumber + $secondNumber;
echo "La suma de $firstNumber + $secondNumber es $result<br />";

// Operador resta (-)
$result = $firstNumber - $secondNumber;
echo "La resta de $firstNumber - $secondNumber es $result<br />";

// Operador multiplicación (*)
$result = $firstNumber * $secondNumber;
echo "La multiplicación de $firstNumber * $secondNumber es $result<br />";

// Operador división (/)
$result = $firstNumber / $secondNumber;
echo "La división de $firstNumber / $secondNumber es $result<br />";

// Operador módulo (%)
$result = $firstNumber % $secondNumber;
echo "El resto de la división de $firstNumber / $secondNumber es $result<br />";

// OPERADORES LÓGICOS
echo "<br />OPERADORES LÓGICOS<br />";
$firstBool = true;
$secondBool = false;

// Operador lógico AND (&&)
$logicAnd = ($firstBool && $secondBool);
echo "AND lógico: $logicAnd<br />";

// Operador lógico OR (||)
$logicOr = ($firstBool || $secondBool);
echo "OR lógico: $logicOr<br />";

// Operador lógico NOT (!)
$logicNot = !$firstBool;
echo "NOT lógico: $logicNot<br />";

// OPERADORES DE COMPARACIÓN
echo "<br />OPERADORES DE COMPARACIÓN<br />";
// Operador mayor que (>)
$greatThan = (5 > 10);
echo "¿Es 5 mayor que 10? -> $greatThan<br />";

// Operador menor que (<)
$lessThan = (5 < 10);
echo "¿Es 5 menor que 10? -> $lessThan<br />";

// Operador mayor o igual que (>=)
$greatOrEqual = (5 >= 10);
echo "¿Es 5 mayor o igual que 10? -> $greatOrEqual<br />";

// Operador menor o igual que (<=)
$lessOrEqual = (5 <= 10);
echo "¿Es 5 menor o igual que 10? -> $lessOrEqual<br />";

// OPERADORES DE ASIGNACIÓN
echo "<br />OPERADORES DE ASIGNACIÓN<br />";
// Operador de asignación simple (=)
$number = 10;
echo "Valor asignado: $number<br />";

// Operador de suma y asignación (+=)
$number += 5; // 10 + 5 = 15
echo "Valor del resultado de suma y asignación: $number<br />";

// Operador de resta y asignación (-=)
$number -= 5; // 15 - 5 = 10
echo "Valor del resultado de resta y asignación: $number<br />";

// Operador de multiplicación y asignación (*=)
$number *= 5; // 10 * 5 = 50
echo "Valor del resultado de multiplicación y asignación: $number<br />";

// Operador de división y asignación (/=)
$number /= 5; // 50 / 5 = 10
echo "Valor del resultado de división y asignación: $number<br />";

// Operador de módulo y asignación (%=)
$number %= 5; // 10 % 5 = 0
echo "Valor del resultado de módulo y asignación: $number<br />";

// OPERADORES DE IDENTIDAD
echo "<br />OPERADORES DE IDENTIDAD<br />";
// Operador de igualdad estricta
$strictEqualComp = (5 === 5);
echo "¿Es 5 estrictamente igual a 5? -> $strictEqualComp<br />";

// Operador de desigualdad estricta (!==)
$strictDiffComp = ('5' !== '5');
echo "¿Es '5' estrictamente diferente a '5'? -> $strictDiffComp<br />";

// OPERADORES DE PERTENENCIA
echo "<br />OPERADORES DE PERTENENCIA<br />";
$intArray = [1, 12, 5, 643, 3];
$firstCheck = in_array(3, $intArray); // Devolverá true
$secondCheck = in_array(65, $intArray); // Devolverá false

echo "¿Está el número 3 en el array de números? -> ";
echo $firstCheck ? "true<br />" : "false<br />";
echo "¿Está el número 65 en el array de números? -> ";
echo $secondCheck ? "true<br />" : "false<br />";

// OPERADORES DE BITS
echo "<br />OPERADORES DE BITS<br />";
$firstBit = 5; // Representación binaria: 0000 0101
$secondBit = 3; // Representación binaria: 0000 0011

// Operador AND a nivel de bits (&)
$bitAnd = $firstBit & $secondBit; // Devuelve 1 (representación binaria: 0000 0001)
echo "Resultado AND bit a bit -> $bitAnd<br />";

// Operador OR a nivel de bits (|)
$bitOr = $firstBit | $secondBit; // Devuelve 7 (representación binaria: 0000 0111)
echo "Resultado OR bit a bit -> $bitOr<br />";

// Operador XOR a nivel de bits (^)
$bitXor = $firstBit ^ $secondBit; // Devuelve 6 (representación binaria: 0000 0110)
echo "Resultado OR bit a bit -> $bitXor<br />";

// Operador NOT a nivel de bits (~)
$bitNot = ~$firstBit; // Devuelve -6 (representación binaria: 1111 1010)
echo "Resultado NOT bit a bit -> $bitNot<br />";

// Operador de desplazamiento hacia la derecha (>>)
$toRightBit = $firstBit >> 1; // Devuelve 2 (representación binaria: 0000 0010)
echo "Desplazamiento hacia la derecha -> $toRightBit<br />";

// Operador de desplazamiento hacia la izquierda (<<)
$toLeftBit = $firstBit << 1; // Devuelve 10 (representación binaria: 0000 1010)
echo "Desplazamiento hacia la izquierda -> $toLeftBit<br />";

// ESTRUCTURAS DE CONTROL CONDICIONAL
echo "<br />ESTRUCTURAS DE CONTROL CONDICIONAL<br />";
// if-else
echo "if-else<br />";
$num = 10;

if ($num > 0) {
    echo "El número es positivo.<br />";
} else if ($num === 0) {
    echo "El número es cero.<br />";
} else {
    echo "El número es negativo.<br />";
}

// Operador ternario
echo "<br />Operador ternario<br />";
echo ($num > 0) ? "El número es positivo.<br />" : "El número es cero o negativo.<br />";

// switch-case
echo "<br />Switch-Case<br />";
$option = 1;

switch ($option) {
    case 1:
        echo "Se ha seleccionado la opción 1.<br />";
        break;
    case 2:
        echo "Se ha seleccionado la opción 2.<br />";
        break;
    default:
        echo "Opción por defecto.<br />";
        break;
}

// ESTRUCTURAS DE CONTROL ITERATIVAS
echo "<br />ESTRUCTURAS DE CONTROL ITERATIVAS<br />";
// while
echo "Bucle While<br />";
$counter = 0;
while ($counter < 5) {
    echo "Iteración: $counter<br />";
    $counter++;
}

// do-while
echo "<br />Bucle do-while<br />";
$counter = 0;
do {
    echo "Iteración: $counter<br />";
    $counter++;
} while ($counter < 5);

// for
echo "<br />Bucle for<br />";
for ($counter = 0; $counter < 5; $counter++) {
    echo "Iteración: $counter<br />";
}

// for ... each
echo "<br />Bucle for ... each<br />";
$arrNumbers = [1, 2, 5, 2, 7, 9];
foreach ($arrNumbers as $number) {
    echo "Número -> $number<br />";
}

// for ... in (Simulación)
echo "<br />Bucle for ... in (Simulación)<br />";
$persona = ['name' => 'Alberto', 'age' => 33];
foreach ($persona as $key => $value) {
    echo "$key -> $value<br />";
}

// MANEJO DE EXCEPCIONES
echo "<br />MANEJO DE EXCEPCIONES<br />";
echo "Bloque try-catch<br />";
$errNumber = 10;

try {
    if ($errNumber === 10) {
        throw new Exception('El número es igual a 10.');
    }
    echo "El número es distinto de 10.<br />";
} catch (Exception $error) {
    echo "Se ha producido un error debido a -> {$error->getMessage()}<br />";
}

echo "<br />Bloque try-catch-finally<br />";
try {
    if ($errNumber === 10) {
        throw new Exception('El número es igual a 10.');
    }
    echo "El número es distinto de 10.<br />";
} catch (Exception $error) {
    echo "Se ha producido un error debido a -> {$error->getMessage()}<br />";
} finally {
    echo "Bloque finally. Esto siempre se ejecuta haya o no excepción.<br />";
}

// DIFICULTAD EXTRA
echo "<br />EJERCICIO EXTRA<br />";
/*  Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y
 *  que no son ni el 16 ni múltiplos de 3.*/
for ($i = 10; $i <= 55; $i++) {
    if (($i % 2 === 0) && ($i !== 16) && ($i % 3 !== 0)) {
        echo "Iteración: $i<br />";
    }
}