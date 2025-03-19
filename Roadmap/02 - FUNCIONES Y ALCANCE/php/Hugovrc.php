<?php

// Funciones Sin parámetros ni retorno
function hola_mundo() {
    echo "Hola, mundo \n";
}

hola_mundo();

// Con un parametro
function funcion_con_parametro($lenguaje) {
    echo "Estoy aprendiendo: ". $lenguaje;
}

funcion_con_parametro("PHP\n");

// Con varios parametros
function funcion_con_varios_parametros($numero1, $numero2) {
    echo $numero1. " + " .$numero2. " = ". $numero1 + $numero2. "\n";
}

funcion_con_varios_parametros(1,2);

// Funciones con retorno
function cuadrado($num) {
    return $num * $num."\n";
}

echo cuadrado(5);

//funciones dentro de funciones
function hola_php() {
    function lenguaje() {
        echo "Hola PHP \n";
    }
    lenguaje();
}

hola_php();

// funciones ya creadas en el lenguaje
date_default_timezone_set('America/Mexico_City');

$fecha_y_hora = date("d-m-y H:m:s");
echo $fecha_y_hora. "\n";

  // Obtiene la version de php
echo "Version de PHP: " .phpversion(). "\n";

// variable local y global

//variable global
$numero = 2;

function tabla_del_dos() {
    global $numero;
    for ($i=1; $i<=10; $i++) { // i Variable local
       echo $numero * $i. "\n";
    }
}

tabla_del_dos();


// DIFICULTAD EXTRA
echo "------- Dificultad Extra-------- \n";
function fizz_buzz($parametro1, $parametro2) {
    $veces = 0;
    for ($a=1; $a<=100; $a++) {
        if ($a % 3 == 0 and $a % 5 == 0) {
            echo $parametro1. $parametro2."\n";
        } elseif ($a % 3 == 0) {
            echo $parametro1."\n";
        } elseif ($a % 5 == 0) {
            echo $parametro2."\n";
        } else {
            echo $a."\n";
            $veces += 1;
        }
    }
return $veces. " veces se ha impreso el numero \n";
}

echo fizz_buzz("fizz","buzz");

?>