<?php

$name = "Alejandro Toro";

// sin retorno
function welcom() {
    echo "Hola mundo!";
}

welcom();

// con parametros y retorno
function sum(int $x, int $y) {
    return $x + $y;
}

echo "suma " . sum(2,3);

$product = [
    "brand" => "Lg",
    "price" => 1000,
];
function getProduct() {
    global $product;
    $user = "Alejandro Toro";
    // no puede obtener la variable de la funcion inicial
    function payment($name, $product) {
        echo "User $name pago " . print_r($product,1);
    }
    payment($user, $product);
}
getProduct();

// el php la no se puede tener contexto de las variables locales y globales, dependiendo de
// usar global o pasar por parametro

function getText(string $param1, string $param2) {

    $countNumbers = 0;

    for($i = 1; $i <= 100; $i++) {
        if($i % 3 === 0 && $i % 5 === 0) echo $param1 . " " . $param2;
        elseif($i % 3 === 0) echo $param1;
        elseif($i % 5 === 0) echo $param2;
        else 
         $countNumbers++;
    };
    return $countNumbers;
}

echo "cantidad de números " . getText("User", "Toro");