<?php
//Crea ejemplos utilizando todos los tipos de operadores en tu lenguaje
//Aritmeticos
$num1 = 1;
$num2 = 2;

$suma = $num1 + $num2;
$resta = $num1 - $num2;
$multi = $num1 * $num2;
$div = $num1 / $num2;
echo "suma: ".$suma; echo "resta: ".$resta; echo "multi: ".$multi; echo "div: ".$div;

//asignacion
$num3 = 3;
$num4 = 4;

$num3 += $num4;
echo "suma: ".$num3; 

$num3 -= $num4;
echo "resta: ".$num3; 

$num3 *= $num4;
echo "multi: ".$num3; 

$num3 /= $num4;
echo "div: ".$num3; 

//Comparacion
echo $num1 == $num2; 
echo $num1 != $num2; 
echo $num1 < $num2; 
echo $num1 > $num2; 
echo $num1 <= $num2; 
echo $num1 >= $num2; 

//incremento o decremento 
$num5 = 1;
echo $num5; $num5++; $num5--;

//Logicos
echo $num1 and $num2, PHP_EOL;
echo $num1 or $num2, PHP_EOL;
echo $num1 xor $num2, PHP_EOL;
echo $num1 && $num2, PHP_EOL;
echo $num1 || $num2, PHP_EOL;
echo !$num1, PHP_EOL;

//Condicionales 
//if
if($num1 < $num2){
    echo "$num2 < $num1";
} else {
    echo "$num2 > $num1";
}

//if acortado
if($num1 < $num2) echo "$num2 < $num1";

//switch 

$diaLibre = "lunes";

switch($diaLibre){
    case "lunes":
        echo "DIA LIBRE!";
        break;
    case "martes":
        echo "TRABAJO!";
        break;
    case "miercoles":
        echo "TRABAJO!";
        break;
    case "jueves":
        echo "TRABAJO!";
        break;
    case "viernes":
        echo "TRABAJO!";
        break;
    case "sabado":
        echo "TRABAJO!";
        break;
    case "domingo":
        echo "TRABAJO!";
        break;
    default:
        echo"dia no encontrado";
        break;
}
$num = 0;
$numTope = 10;

//while
while($num < $numTope){
    echo "numero actual: $num ";
    $num += 1;
} 
//do while
do{
    $num++;
    echo "numero actual: $num";
} while($num == $numTope);
//for
for($num=0;$num!=10;$num++){
    echo $num;
}
$tareas = ["ordenar casa", "lavar la losa", "dormir"];
foreach ($tareas as $key => $value) {
    echo "Tarea n°" . ($key + 1) . " = " . $value . PHP_EOL;
}

$num1 = 1;
$num2 = "2";

try {
    // Intentamos realizar la operacion
    if (!is_numeric($num1) || !is_numeric($num2)) {
        throw new Exception("Uno de los valores no es numérico.");
    }

    echo "Resultado: " . ($num1 + $num2) . PHP_EOL;
} catch (Exception $e) {
    // Capturamos la excepcion
    echo "Error: " . $e->getMessage() . PHP_EOL;
}


//ejercicio adicional
for($num=10;$num<=55;$num++){
    if(($num % 2 == 0) && ($num % 3 != 0) && ($num != 16)){
        echo $num.PHP_EOL;
    }
}
?>
