<?php

require 'vendor/autoload.php';  

use Amp\Loop;
use Amp\Promise;

/*
* De forma nativa, php no tiene soporte para funciones asíncronas. 
* Sin embargo, podemos simularlo con la función sleep.
*/
function asyncTask($name, $seconds){
    echo "Función asíncrona con nombre $name iniciada en el instante " . date('H:i:s') . "\n";
    sleep($seconds);
    echo "Función asíncrona con nombre $name finalizada en el instante " . date('H:i:s') . "\n";
}

echo "Simulacion con sleep (No realmente asincrono)\n";
asyncTask('MiFuncion', 5);

/*
* Para realizar tareas asíncronas de forma real, podemos utilizar librerías externas como Amp.
* Amp es una librería que nos permite realizar tareas asíncronas de forma sencilla.
*/

function asyncTaskAmp($name, $seconds){
    return Amp\call(function () use ($name, $seconds) {
        echo "Función asíncrona con nombre $name iniciada en el instante " . date('H:i:s') . "\n";
        yield Amp\delay($seconds * 1000);  // Amp\delay espera un tiempo en milisegundos
        echo "Función asíncrona con nombre $name finalizada en el instante " . date('H:i:s') . "\n";
    });
}

echo "\n\nAsincronía real mediante uso de libreria externa\n";  
Loop::run(function () {
    asyncTaskAmp('MiFuncion', 5);
});

echo "\n\nEjercicio Extra (solo con Amp, con sleep no se podria hacer)\n";
Loop::run(function () {
    // Iniciar las funciones C, B y A en paralelo
    $promises = [
        asyncTaskAmp('C', 3),
        asyncTaskAmp('B', 2),
        asyncTaskAmp('A', 1),
    ];

    // Esperar a que las funciones C, B y A finalicen
    Promise\wait(Promise\all($promises));

    // Iniciar la función D
    Loop::run(function () {
        asyncTaskAmp('D', 1);
    });
});