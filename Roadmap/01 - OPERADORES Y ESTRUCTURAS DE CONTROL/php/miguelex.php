<?php

/* En PHP podemos encontrar los siguientes tipos de operadores:
Operadores aritméticos
Operadores de asignación
Operadores bit a bit
Operadores de comparación
Operadores de incremento/decremento
Operadores lógicos
Operadores para strings
Operadores para arrays
*/

// Operadores aritmeticos

$num1 = 5;
$num2 = 2;

echo "--- Operadores aritméticos ---\n";
echo "Usaremos los valores $num1 y $num2 para las operaciones\n";
echo "Suma: " . ($num1 + $num2)."\n";
echo "Resta: " . ($num1 - $num2)."\n";
echo "Multiplicación: " . ($num1 * $num2)."\n";
echo "División: " . ($num1 / $num2)."\n";
echo "Módulo: " . ($num1 % $num2)."\n";
echo "Exponenciación: " . ($num1 ** $num2)."\n";
echo "Identidad: " . (+$num1)."\n";
echo "Negación: " . (-$num1)."\n";

// Operadores de asignación
$x = 3;
$y = 4;
echo "--- Operadores de asignación ---\n";
echo "x = $x\n";
echo "y = $y\n";
echo "x += y: " . ($x += $y)."\n";
echo "x -= y: " . ($x -= $y)."\n";
echo "x *= y: " . ($x *= $y)."\n";
echo "x /= y: " . ($x /= $y)."\n";
echo "x %= y: " . ($x %= $y)."\n";
echo "x **= y: " . ($x **= $y)."\n";

// Operadores bit a bit
echo "--- Operadores bit a bit ---\n";
echo "x = $x\n";
echo "y = $y\n";
echo "And -> x & y: " . ($x & $y)."\n";
echo "Or -> x | y: " . ($x | $y)."\n";
echo "Xor -> x ^ y: " . ($x ^ $y)."\n";
echo "Desplazamiento a izquierda -> x <<= y: " . ($x <<= $y)."\n";
echo "Desplazamiento a derecha -> x >>= y: " . ($x >>= $y)."\n";

// Operadores de comparación
echo "--- Operadores de comparación ---\n";
echo "x = $x\n";
echo "y = $y\n";
echo "Igual: x == y: " . ($x == $y)."\n";
echo "Identico: x === y: " . ($x === $y)."\n";
echo "Distinto: x != y: " . ($x != $y)."\n";
echo "Distinto: x <> y: " . ($x <> $y)."\n";
echo "No identico: x !== y: " . ($x !== $y)."\n";
echo "Menor que: x < y: " . ($x < $y)."\n";
echo "Mayor que: x > y: " . ($x > $y)."\n";
echo "Menor o igual que x <= y: " . ($x <= $y)."\n";
echo "Mayor o igual que x >= y: " . ($x >= $y)."\n";
echo "x <=> y: " . ($x <=> $y)."\n";

// Operadores de incremento/decremento
echo "--- Operadores de incremento/decremento ---\n";
echo "x = $x\n";
echo "y = $y\n";
echo "Pre-incremento: ++x: " . (++$x)."\n";
echo "Post-incremento: x++: " . ($x++)."\n";
echo "Pre-decremento: --x: " . (--$x)."\n";
echo "Post-decremento: x--: " . ($x--)."\n";

// Operadores lógicos
echo "--- Operadores lógicos ---\n";
echo "x = $x\n";
echo "y = $y\n";
echo "And: x and y: " . ($x and $y)."\n";
echo "Or: x or y: " . ($x or $y)."\n";
echo "Xor: x xor y: " . ($x xor $y)."\n";
echo "&&: x && y: " . ($x && $y)."\n";
echo "||: x || y: " . ($x || $y)."\n";
echo "Not: !x: " . (!$x)."\n";

// Operadores para strings
echo "--- Operadores para strings ---\n";
echo "x = $x\n";
echo "y = $y\n";
echo "Concatenación: x . y: " . ($x . $y)."\n";
echo "Concatenación: x .= y: " . ($x .= $y)."\n";
echo "+: +x: " . (+$x)."\n";
echo "Repetición: x * y: " . ($x * $y)."\n";

// Operadores para arrays
echo "--- Operadores para arrays ---\n";
$arr1 = array(1,2,3,4);
$arr2 = array(1,3, 5,6,7,8);
echo "Unión:\n";
var_dump($arr1+$arr2);
echo "Igualdad:\n";
var_dump($arr1 == $arr2);
echo "Identidad:\n";
var_dump($arr1 === $arr2);
echo "Desigualdad:\n"; 
var_dump($arr1!= $arr2);
echo "Desigualdad:\n"; 
var_dump($arr1 <> $arr2);
echo "No identidad:\n" ;
var_dump($arr1 !== $arr2);

// Excepciones en PHP
echo "--- Excepciones en PHP ---\n";
try {
    throw new Exception("Excepción lanzada");
} catch (Exception $e) {
    echo $e->getMessage();
}

// Excepcion con finally
echo "--- Excepcion con finally ---\n";
try {
    throw new Exception("Excepción lanzada");
} catch (Exception $e) {
    echo $e->getMessage();
} finally {
    echo "Esto se ejecuta siempre\n";
}

// Estructuras de control
echo "--- Estructuras de control ---\n";

// if

echo "--- if ---\n";
if ($x > $y) {
    echo "x es mayor que y\n";
} elseif ($x == $y) {
    echo "x es igual que y\n";
} else {
    echo "x es menor que y\n";
}

// switch
echo "--- switch ---\n";
switch ($x) {
    case 1:
        echo "x es 1\n";
        break;
    case 2:
        echo "x es 2\n";
        break;
    default:
        echo "x no es ni 1 ni 2\n";
}

// while
echo "--- while ---\n";
$i = 0;
while ($i < 10) {
    echo $i."\n";
    $i++;
}

// do while
echo "--- do while ---\n";
$i = 0;
do {
    echo $i."\n";
    $i++;
} while ($i < 10);

// for
echo "--- for ---\n";
for ($i = 0; $i < 10; $i++) {
    echo $i."\n";
}

// foreach
echo "--- foreach ---\n";
$arr = array(1,2,3,4,5,6,7,8,9,10);
foreach ($arr as $value) {
    echo $value."\n";
}

// foreach con clave
echo "--- foreach con clave ---\n";
$arr = array(1,2,3,4,5,6,7,8,9,10);
foreach ($arr as $key => $value) {
    echo "Clave: $key, Valor: $value\n";
}

// break
echo "--- break ---\n";
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) {
        break;
    }
    echo $i."\n";
}

// continue
echo "--- continue ---\n";
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) {
        continue;
    }
    echo $i."\n";
}

// goto
echo "--- goto ---\n";
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) {
        goto end;
    }
    echo $i."\n";
}
end:
echo "Fin del bucle\n";

// return
echo "--- return ---\n";
function suma($x, $y) {
    return $x + $y;
}
echo suma(5, 6)."\n";

// Operador ternario 
echo "Ternario: ".($x > $y ? "x es mayor que y" : "x es menor o igual que y")."\n";

// Extra
echo "--- Extra ---\n";
for ($i = 10; $i <= 55; $i++){
    if (($i % 2 == 0) && ($i != 16) && ($i % 3 != 0))
        echo $i."\n";
}