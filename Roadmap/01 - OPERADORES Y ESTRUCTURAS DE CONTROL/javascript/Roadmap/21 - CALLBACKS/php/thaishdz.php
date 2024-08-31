<?php

require 'vendor/autoload.php';

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega. ✔️
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos. ✔️
 * - Debe invocar a cada callback siguiendo un orden de procesado. ✔️
 * - Debe notificar que el plato está listo o ha sido entregado. ✔️
 */

use React\EventLoop\Loop;
use React\Promise\Deferred;

function processOrder(
    string $meal, 
    callable $confirmCallback, 
    callable $readyCallback, 
    callable $deliveredCallback
): void
{
    $deferredConfirm = new Deferred(); // crea una promesa

    // Etapa Confirm
    Loop::addTimer(rand(1,10), function() use ($meal, $confirmCallback,$deferredConfirm)
    {
        echo $confirmCallback($meal);
        $deferredConfirm->resolve($meal); // se le pasa el pedido a la siguiente etapa
    });

    // Encadenar la siguiente etapa - Ready
    $deferredConfirm->promise()->then(function($meal) use($readyCallback, $deliveredCallback) 
    {   
        $deferredReady = new Deferred(); // nueva promesa ya que la anterior se resolvió

        Loop::addTimer(rand(1,10), function() use ($meal, $readyCallback, $deliveredCallback, $deferredReady)
        {
            echo $readyCallback($meal);
            $deferredReady->resolve($meal);

                
        });
        // Encadenar la siguiente etapa - Delivered
        $deferredReady->promise()->then(function($meal) use ($deliveredCallback)
        {
            Loop::addTimer(rand(1,10), function() use ($meal, $deliveredCallback)
            {
                
                echo $deliveredCallback($meal);
            });
        });
    });
}

function confirm(string $order) : string 
{
    return "$order confirmed \n";
}


function ready(string $order) : string 
{
    return "$order ready! \n";
}


function deliver(string $order) : string 
{
   return "Order delivered!, Enjoy your $order 😋 \n";
}



# Orders in queue

processOrder('Big Mac 🍔', 'confirm', 'ready', 'deliver');
processOrder('Happy Meal 🍟','confirm', 'ready', 'deliver');
processOrder('Mcflurry 🍦', 'confirm', 'ready', 'deliver');
