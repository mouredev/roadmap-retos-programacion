<?php

$numero1 = 10;
$numero2 = 5;
$resultado = 0;
// Operadores Aritmeticos

//suma
echo "----suma----\n";
$resultado = $numero1 + $numero2;
echo $numero1. " + " .$numero2. " = " .$resultado. "\n"; 
//resta
echo "----resta----\n";
$resultado = $numero1 - $numero2;
echo $numero1. " - " .$numero2. " = " .$resultado. "\n";
//multiplicacion
echo "----multiplicacion----\n";
$resultado = $numero1 * $numero2;
echo $numero1. " * " .$numero2. " = " .$resultado. "\n";
//division
echo "----division----\n";
$resultado = $numero1 / $numero2;
echo $numero1. " / " .$numero2. " = " .$resultado. "\n";
//modulo
echo "----modulo----\n";
$resultado = $numero1 % $numero2;
echo $numero1. " % " .$numero2. " = " .$resultado. "\n";
//exponenciacion
echo "----exponenciacion----\n";
$resultado = $numero1 ** $numero2;
echo $numero1. " ** " .$numero2. " = " .$resultado. "\n";

//Operadores de asignación
$numero3 = 4;

//Operadores de comparación
//igual
$numero1 == $numero2;
//identico
$numero1 === $numero2;
//diferente
$numero1 != $numero2;
$numero1 <> $numero2;
//no identico
$numero1 !== $numero2;
//menor que
$numero1 < $numero2;
//mayor que
$numero1 > $numero2;
//menor o igual que
$numero1 <= $numero2;
//mayor o igual que
$numero1 >= $numero2;

//Operadores de incremento/decremento
//pre-incremento
++$numero1. "\n"; //incrementa $numero1 en 1 y luego retorna $numero1.
//post-incremento
$numero2++. "\n"; //retorna $numero2, y luego incrementa $numero2 en 1.
//pre-decremento
--$numero1. "\n"; //Decrementa $numero1 en uno, luego retorna $numero1.
//post-decremento
$numero2++. "\n"; //Retorna $numero2, luego decrementa $numero2 en uno.

//Operadores lógicos
// And
$numero1 and $numero2; //verdadero si tanto $numero1 como $numero2 son verdaderos.
$numero1 && $numero2;
// Or
$numero1 or $numero2; //verdadero si cualquiera de $numero1 o $numero2 es verdadero.
$numero1 || $numero2;
// Xor
$numero1 xor $numero2; //verdadero si $numero1 o $numero2 es verdadero, pero no ambos.
// Not
!$numero1; //verdadero si $numero1 no es true.

//Estructuras de Control
//Condicionales

//If
echo "----if----\n";
if ($numero1 > $numero2) {
    echo $numero1. " es mayor que " .$numero2. "\n"; 
}
//else
echo "----else----\n";
if ($numero1 < $numero2) {
    echo $numero1. " es menor que " .$numero2. "\n";
} else {
    echo $numero1. " es mayor que " .$numero2. "\n";
}
//elseif
echo "----elseif----\n";
if ($numero1 < $numero2) {
    echo $numero1. " es menor que " .$numero2. "\n";
} elseif ($numero1 == $numero2) {
    echo $numero1. " es igual que " .$numero2. "\n";
} else {
    echo $numero1. " es mayor que " .$numero2. "\n";
}

//switch
echo "----switch----\n";
$fruta = "manzana";
switch ($fruta) {
    case "naranja":
        echo "la fruta es una naranja\n";
        break;
    case "manzana":
        echo "la fruta es una manzana\n";
        break;
    case "limon":
        echo "la fruta es un lima\n";
        break;
}

//Iterativas
//while
echo "----while----\n";
$numero4 = 1;
while ($numero4 <= 10) {
    echo $numero4++. "\n";
}

//do-while
echo "----do-while----\n";
$numero4 = 0;
do {
    echo $numero4. "\n";
    $numero4++;
} while ($numero4 <= 5);

//for
echo "----for----\n";
for ($numero4 = 1; $numero4 <= 10; $numero4++) {
    echo $numero4. "\n";
}

//foreach
echo "----foreach----\n";
$array = array(1,2,10,9);
foreach ($array as &$valor) {
    echo $valor. "\n";
}

//excepciones
echo "----try catch----\n";
echo "----division por 0----\n";
$a = 10;
$b = 0;
try {
    if ($b === 0) {
        throw new Exception("no se admiten divisiones por 0");
    }
    echo $a / $b;
} catch (Exception $e) {
    echo "ha habido una excepcion: " .$e->getMessage(). "\n";
}

echo "----Dificultad extra----\n";
for ($numero = 10; $numero <= 55; $numero++) {
    if ($numero % 2 == 0 and $numero != 16 and $numero % 3 != 0) {
        echo $numero. "\n";
    }
}
?>