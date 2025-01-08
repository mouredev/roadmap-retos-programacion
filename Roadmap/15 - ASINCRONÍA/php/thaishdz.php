<?php

/*
* Utilizando el concepto de asincronía y la función anterior, crea
* el siguiente programa que ejecuta en este orden:
* - Una función C que dura 3 segundos.
* - Una función B que dura 2 segundos.
* - Una función A que dura 1 segundo.
* - Una función D que dura 1 segundo.
* - Las funciones C, B y A se ejecutan en paralelo.
* - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
*/

# Usé ReactPHP para manejar la asincronía

use React\EventLoop\Loop;
use React\Promise\Promise;
use function React\Async\parallel;


function task(string $name, int $interval)
{
    return new Promise(function ($resolver) use ($name, $interval) 
    {
        Loop::addTimer($interval, function () use ($resolver, $name, $interval)
        {
            $resolver("Task $name ... Total Time Execution : $interval sg 👻\n");
        });
    });
}


parallel([
    function () { return task('C',3);},
    function () { return task('B',2);},
    function () { return task('A',1);}

])->then(function (array $results){
    // Muestra los resultados de las promesas
    foreach ($results as $result) {
        echo "$result\n";
    }
    return task('D', 1);
})->then(function ($result){
    // Muestra el resultado de la tarea D una vez acaben las 3 anteriores
    echo $result;
});

// Iniciar el loop de eventos
Loop::get()->run();