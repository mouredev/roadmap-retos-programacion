<?php
/// Operadores aritmeticos

$nueve = 9;
$quince = 15;
$seven = 7;
$three = 3;

// SUMA

echo "$nueve + $quince" . PHP_EOL;

// RESTA

echo "$seven - $quince" . PHP_EOL;

// MULTIPLICACION

echo "$nueve * $seven" . PHP_EOL;

// DIVISION

echo "$quince / $seven" . PHP_EOL;

// MODULO

echo "$nueve % $three" . PHP_EOL;

/// OPERADORES LOGICOS

$firstBool = true;
$secondBool = false;

// OPERADOR AND &&

$logic = ($firstBool && $secondBool);
echo "logic $logic" . PHP_EOL;

// OPERADORR OR ||

$logic2 = ($firstBool || $secondBool);
echo "logic $logic2" . PHP_EOL;

// OPERADOR  NOT !

$logic3 = (!$firstBool);


/// OPERADOR DE COMPARACION

// OPERADOR < (MENOR QUE)
$quatro = 4;
$sinco = 5;

$menos = ($quatro < $sinco);
echo "el $quatro es menor que $sinco? , $menos" . PHP_EOL;

// OPERADOR > (MAYOR QUE)
$mas = ($sinco > $quatro);
echo "el $sinco es mayor que $quatro? , $mas" . PHP_EOL;

// MENOR O IGUAL QUE (<=)
$menorigual = ($quatro <= $sinco);
echo "el $quatro es menor o igual a $sinco? , $menorigual" . PHP_EOL;

// MAYOR O IGUAL QUE (>=)
$mayorigual = ($sinco >= $sinco);
echo "el $sinco es mayor o igual a $sinco? , $mayorigual" . PHP_EOL;


$personas =  0;

$curso = 'Programacion en php';



while ($personas <= 15) {
    $desicion = readline('quieres inscrirte al curso? y/n ');

    strtolower(trim($desicion));

    if ($desicion === 'exit') {

    exit('usted ha salido');
    }
    

    if ($desicion === 'y') {
        $personas++;

        echo 'usted se ha inscrito correctamente' . PHP_EOL;

        echo "hay $personas inscritas en $curso" . PHP_EOL;
    }

    if ($desicion === 'n') {

        echo "hay $personas inscritas en $curso" . PHP_EOL;
    }

    else  {
        echo "opcion no valida";
    }
}