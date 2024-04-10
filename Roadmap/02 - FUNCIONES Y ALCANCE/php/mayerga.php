<?php

// Ejemplo de funcion sin parametros
function funcionSinParametros(){
    echo "Acabas de invocar a tu primera función en PHP\n";
}

echo "1º. Vamos a usar una función sin pasarle ningún parametro y sin retornar nada\n";
funcionSinParametros();
echo "\n";

// Ejemplo de funcion con parametros
function parametros($parametro1, $parametro2){
    echo "El valor del primer parametro es: ".$parametro1."\n";
    echo "El valor del segundo parametro es: ".$parametro2."\n";
}

echo "2º. Vamos a usar una función pasando dos parametros y sin retornar nada\n";
parametros("Hola", "Mundo");
echo "\n";

// Ejemplo de funcion con parametros por defecto
function parametrosPorDefecto($parametro1 = "Hola", $parametro2 = "Mundo"){
    echo "El valor del primer parametro es: ".$parametro1."\n";
    echo "El valor del segundo parametro es: ".$parametro2."\n";
}

echo "3º. En este ejemplo vamos a usar una función con parametros con defecto. Vamos a invocarla solo con el primer parametro\n";
parametrosPorDefecto("Hello");
echo "\n";

// Ejemplo de funcion con parametros por referencia
function porReferencia(&$parametro1){
    $parametro1 = "Cambiada la variable";
}

echo "4º. En este ejemplo vamos a usar el paso por referencia. El parametro que pasemos se modificará dentro de la función\n";
$cadena = "Adios";
porReferencia($cadena);
echo $cadena."\n";
echo "\n";

// Ejemplo de funcion con retorno
function funcionConRetorno($parametro1, $parametro2){
    return $parametro1 + $parametro2;
}

echo "5º. En este ejemplo vamos a usar una función con retorno. Vamos a sumar dos numeros\n";
$resultado = funcionConRetorno(5, 7);
echo $resultado."\n";
echo "\n";

// Ejemplo de llamada a funciones anonimas o closures
$variable = function($parametro1, $parametro2){
    return $parametro1 + $parametro2;
};

echo "6º. Llamada a una función anónima (closure)\n";
echo $variable(5, 7)."\n";
echo "\n";

// Ejemplo de funcion con retorno por referencia
function retornoPorReferencia(&$parametro1){
    $parametro1 = "Cambiada la variable";
    return $parametro1;
}

echo "7º. En este ejemplo vamos a usar una función con retorno por referencia. Vamos a modificar el valor de la variable\n";
$variable = "Variable original";
$resultado = retornoPorReferencia($variable);
echo $resultado."\n";
echo "\n";

// Ejemplo de variable local y global
$variableGlobal = "Variable global";
function ambitoVariables(){
    global $variableGlobal;
    $variableLocal = "Variable local";
    echo $variableLocal."\n";
    echo $variableGlobal."\n";
}

echo "8º. En este ejemplo vamos a ver el ambito de las variables\n";
ambitoVariables();
echo "\n";

// funcion dentro de funcion
function funcionDentroDeFuncion(){
    function funcionDentroDeFuncion2(){
        echo "Funcion dentro de funcion\n";
    }
    funcionDentroDeFuncion2();
}

echo "9º. En este ejemplo vamos a ver como se puede llamar a una función dentro de otra función\n";
funcionDentroDeFuncion();
echo "\n";

// funcion dentro de funcion con parametros
function funcionDentroDeFuncionConParametros(){
    function funcionDentroDeFuncionConParametros2($parametro1, $parametro2){
        echo "Funcion dentro de funcion con parametros\n";
        echo "El valor del primer parametro es: ".$parametro1."\n";
        echo "El valor del segundo parametro es: ".$parametro2."\n";
    }
    funcionDentroDeFuncionConParametros2("Hola", "Mundo");
}

echo "10º. En este ejemplo vamos a ver como se puede llamar a una función dentro de otra función pasandole parametros\n";
funcionDentroDeFuncionConParametros();
echo "\n";

// funcion dentro de funcion con parametros por referencia
function funcionDentroDeFuncionConParametrosPorReferencia(){
    function funcionDentroDeFuncionConParametrosPorReferencia2(&$parametro1){
        $parametro1 = "Cambiada la variable";
    }
    $cadena = "Adios";
    funcionDentroDeFuncionConParametrosPorReferencia2($cadena);
    echo $cadena."\n";
}

echo "11º. En este ejemplo vamos a ver como se puede llamar a una función dentro de otra función pasandole parametros por referencia\n";
funcionDentroDeFuncionConParametrosPorReferencia();
echo "\n";

// funcion dentro de funcion con retorno
function funcionDentroDeFuncionConRetorno(){
    function funcionDentroDeFuncionConRetorno2($parametro1, $parametro2){
        return $parametro1 + $parametro2;
    }
    $resultado = funcionDentroDeFuncionConRetorno2(5, 7);
    echo $resultado."\n";
}

echo "12º. En este ejemplo vamos a ver como se puede llamar a una función dentro de otra función con retorno\n";
funcionDentroDeFuncionConRetorno();
echo "\n";

// Ejemplo de uso de una funcion propia de PHP
$variable = "Hola Mundo";

echo "13º. En este ejemplo vamos a ver como se puede llamar a una función propia de PHP, en este caso la que devuelve la longitud de una cadena\n";
echo strlen($variable)."\n";
echo "\n";

// Ejercicio extra

function extra ($parametro1, $parametro2){
    $numsImpresos = 0;
    for ( $i = 1; $i <= 100; $i++){
        switch ($i){
            case $i % 15 == 0: 
                    echo $parametro1.$parametro2."\n";
                    break;
            case $i % 3 == 0: 
                    echo $parametro1."\n";
                    break;
            case $i % 5 == 0: 
                    echo $parametro2."\n";
                    break;
            default: 
                    echo $i."\n";
                    $numsImpresos++;
        }
    }

    return $numsImpresos;
}

echo "Finalmente vamos a resolver el ejercicio extra|n";
echo "Se han imprimido un total de ". extra("fizz", "buzz"). " numeros";

?>