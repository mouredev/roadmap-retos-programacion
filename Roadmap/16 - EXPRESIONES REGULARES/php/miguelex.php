<?php

$texto = "Este es un texto con números como 123, 45.6, -7 y 1000.";

function regExpr($cadena){
    $patron = '/-?\d+(\.\d+)?/';
    preg_match_all($patron, $cadena, $numeros);

    echo "Números encontrados:\n";
    foreach ($numeros[0] as $numero) {
        echo $numero . "\n";
    }
    echo "\n\n";
}

echo "Vamos a analizar el siguiente texto:\n";
echo "'".$texto."'\n\n";

regExpr($texto);

$texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456";
echo "Vamos a analizar el siguiente texto:\n";
echo "'".$texto."'\n\n";

regExpr($texto);

// Extra

function emailValidation($email){
    $patron = '/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/';
    if(preg_match($patron, $email)){
        echo "El email ".$email." es válido.\n";
    } else {
        echo "El email ".$email." no es válido.\n";
    }
}

function phoneValidation ($phone){
    $patron = '/^\+?(\d{2,3})?[-. ]?\d{9}$/';
    if(preg_match($patron, $phone)){
        echo "El teléfono ".$phone." es válido.\n";
    } else {
        echo "El teléfono ".$phone." no es válido.\n";
    }
}

function urlValidation ($url){
    $patron = '/^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/';
    if(preg_match($patron, $url)){
        echo "La URL ".$url." es válida.\n";
    } else {
        echo "La URL ".$url." no es válida.\n";
    }
}


emailValidation("correo@correo.com");
emailValidation("correo@correo");

phoneValidation("+34 123456789");
phoneValidation("123456789");

urlValidation("http://www.google.com");
urlValidation("www.google.com");


