<?php 

// Crear dos variables por valor

$a = 5;
$b = "Hola";

echo "El valor de a es: ".$a."\n";
echo "El valor de b es: ".$b."\n";

$aCopia = $a;
$bCopia = $b;

echo "El valor de aCopia es: ".$aCopia."\n";
echo "El valor de bCopia es: ".$bCopia."\n";

// Modificar el contenido de las variables

$a = 10;
$b = "Adios";
echo "\nValores despues de la modificación:\n";
echo "El valor de a es: ".$a."\n";
echo "El valor de b es: ".$b."\n";
echo "El valor de aCopia es: ".$aCopia."\n";
echo "El valor de bCopia es: ".$bCopia."\n";


// Crear dos variables por referencia

$c = &$a;
$d = &$b;

echo "\nValores de c y d:\n";
echo "El valor de c es: ".$c."\n";
echo "El valor de d es: ".$d."\n";

// Modificar el contenido de las variables

$c = 15;
$d = "Hasta luego";
echo "\nValores despues de la modificación:\n";
echo "El valor de a es: ".$a."\n";
echo "El valor de b es: ".$b."\n";
echo "El valor de c es: ".$c."\n";
echo "El valor de d es: ".$d."\n";

// Ejemplo de una funcio con paso por valor

function incrementa($valor){
    $valor++;
    return $valor;
}

echo "\nEjemplo de funcion con paso por valor:\n";
echo "El valor de a es: ".$a."\n";
$resultado = incrementa($a);
echo "La cantidad que devuelve la funcion es: ".$resultado."\n";
echo "Pero el valor de a sigue siendo: ".$a."\n";


// Ejemplo de una funcio con paso por referencia
function decrementa(&$valor){
    $valor--;
    return $valor;
}   

echo "\nEjemplo de funcion con paso por referencia:\n";
echo "El valor de a es: ".$a."\n";
$resultado = decrementa($a);
echo "La funcion retorna el valor: ".$resultado."\n";
echo "Y el valor de a ahora es: ".$a."\n";

// Extra

echo "\nExtra:\n";

echo "\nPaso por valor\n";
function byValor($a, $b){
    $aux = $a;
    $a = $b;
    $b = $aux;

    return [$a, $b];
}

$aOriginal = 2;
$bOriginal = 3;

echo "El valor de aOriginal es: ".$aOriginal."\n";
echo "El valor de bOriginal es: ".$bOriginal."\n";  

$resultado = byValor($aOriginal, $bOriginal);
echo "La funcion retornó los valores: ".implode(",", $resultado)."\n";
echo "Pero los valores originales siguen siendo: ".$aOriginal." y ".$bOriginal."\n";

$arrAOriginal = [1, 2, 3];
$arrBOriginal = [4, 5, 6];

$resultado = byValor($arrAOriginal, $arrBOriginal);
echo "La funcion retornó los valores: ".print_r($resultado, true)."\n";
echo "pero los valroes valores originales siguen siendo: ".print_r($arrAOriginal, true). " y ".print_r($arrBOriginal, true)."\n";

echo "\nPaso por referencia\n";
function byReferencia(&$a, &$b){
    $aux = $a;
    $a = $b;
    $b = $aux;

    return [$a, $b];
}

$aOriginal = 2;
$bOriginal = 3;

echo "El valor de aOriginal es: ".$aOriginal."\n";
echo "El valor de bOriginal es: ".$bOriginal."\n";

$resultado = byReferencia($aOriginal, $bOriginal);
echo "La funcion retornó los valores: ".implode(",", $resultado)."\n";
echo "Y los valores originales ahora son: ".$aOriginal." y ".$bOriginal."\n";

$arrAOriginal = [1, 2, 3];
$arrBOriginal = [4, 5, 6];

$resultado = byReferencia($arrAOriginal, $arrBOriginal);
echo "La funcion retornó los valores: ".print_r($resultado, true)."\n";
echo "Y los valores originales ahora son: ".print_r($arrAOriginal, true). " y ".print_r($arrBOriginal, true)."\n";




