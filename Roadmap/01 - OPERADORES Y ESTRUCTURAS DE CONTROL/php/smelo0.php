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

/// OPERADOR DE IDENTIDAD
// OPERADOR DE IGUALDAD ESTRICTA
$strictEqualComp = (5 === 5);
echo "es 5 exactamente igual al 5, $strictEqualComp";

// PARQUEADERO DE DESIGUALDAD ESTRICTA
$strictNotEqual = (5 !== 5);
echo "es 5 exactamente diferente a 5?, $strictNotEqual";

/// OPERADOR DE PERTENENCIA Y FOREACH

$myArray = [5, 8, 13, 21, 34];
$checkIn = [5, 13, 34];
$checkIngArray = in_array($checkIn, $myArray);

foreach ($myArray as $number) {
    if (in_array($number, $checkIn )) {
        echo "el numero $number esta en el arreglo" . PHP_EOL;
    }
    else {
        echo "el numero $number no esta en el arreglo" . PHP_EOL;
    }
}

/// FOR

for ($contador = 0; $contador <= 5; $contador++) {
    echo "el contador va en $contador";
}

/// TRY, CATCH Y FINALLY


$sheInterested = false;


try {
    if ($sheInterested !== true) {// lo que podria ir mal
        throw new Exception("no esta interesada");
    }
} catch (Exception $error) {
    echo "algo fallo, {$error->getMessage()}" . PHP_EOL;
} finally {
    echo "sigue intentando pa, {$error->getMessage()}, eso pasa" . PHP_EOL;
}

$personas =  0;

$curso = 'Programacion en php';

/// WHILE, IF Y ELSE

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
};

// RETO EXTRA

/* 
* Crea un programa que imprima por consola todos los números comprendidos
* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/



for ($i = 10; $i < 55; $i++) {
    if (($i % 2 === 0) && ($i !== 16) && ($i % 3 === 0)) {
        echo "joder iteracion $i" . PHP_EOL;
    }

}