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


$add = 1 + 1; // Addition
$sub = 5 - 2; // Subtraction
$multiply = 3 * 4; // Multiplication
$division = 1 / 3; // Division
$greatThan = 10 > 5; // Greater than
$lessThan = 10 < 5; // Less than
$greatOrEqual = 10 >= 5; // Greater than or equal to
$lessOrEqual = 10 <= 5; // Less than or equal to
$notEqual = 10 <> 5; // Not equal to
$assignment = "Value"; // Assignment
$number = 5;
$number++; // Return $number and then increments  by 1
$number--; // Return $number and then decrements  by 1
++$number; // Increments  by 1 and then return $number
$number--; // Decrements  by 1 and then return $number
$isValid = true && false; // AND operator
$isValid = true || false; // OR operator
$isValid = true and false; // AND operator
$isValid = true or false; // OR operator
$isValid = true xor false; // XOR operator
$isValid = !true; // NOT operator
$isValid = true ? 'accepted' : 'rejected'; // Ternary operator
$name = null;
$userName = $name ?: 'Unknow'; // Short ternary opertor
$roleName = $role ?? 'guest'; // Null coalescing

// If
if ($roleName == 'guest') {
	$grantAccess = false;
} elseif ($roleName == 'admin') {
	$grantAccess = true;
}

// Switch

switch ($roleName) {
	case 'guest':
		$grantAccess = false;
		break;

	case 'admin':
		$grantAccess = true;
		break;
	
	default:
		$grantAccess = false;
		break;
}

// Match
$grantAccess = match ($roleName) {
	'guest' => false,
	'admin' => true,
	default => false,
};

$page = 1;
$totalPages = 10;

while ($page < $totalPages) {
	// Do stuff
	$page++;
}

do {
	$page++;
	// Do stuff
} while ($page <= $totalPages);

$sales = [10, 15, 12, 20];
$total = 0;
for ($i=0; $i <= 3; $i++) { 
	$total = $total + $sales[$i];
}

$total = 0;
foreach ($sales as $sale) {
	$total = $total + $sale;
}

try {
	throw new Exception("Error Processing Request", 1);

} catch (Exception $e) {
	// Handle the exception
}

foreach (range(10, 55) as $number) {

	if (($number % 2 == 0 || $number == 55) && $number != 16 && $number % 3 != 0) {

		echo $number . PHP_EOL;
	}

}