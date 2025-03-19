<?php
function callbackExample(array $numeros, callable $callback) {
    $resultado = 0;
    foreach ($numeros as $numero) {
        $resultado = $callback($resultado, $numero);
    }
    return $resultado;
}

$numeros = [10, 9, -5, 3, 2, 1, 0];

function numberSum($a, $b) {
    return $a + $b;
}

echo "Vamos a ver un ejemplo simple de Callback. Pasaremos un array de numeros y obtendremos la suma de todo sus elementos\n";

echo "El resultado de la suma de los numeros es: " . callbackExample($numeros, 'numberSum');


// Extra

echo '\n\nEjercicio Extra\n\n';

function procesarPedido($plato, callable $confirmacion, callable $listo, callable $entrega) {
    
    echo "Procesando el pedido del plato: $plato\n";
    $confirmacion($plato);
    
    
    $tiempoPreparacion = rand(1, 10);
    sleep($tiempoPreparacion);
    
    
    $listo($plato);
    
   
    $tiempoEntrega = rand(1, 10);
    sleep($tiempoEntrega);
    
    
    $entrega($plato);
}


function confirmarPedido($plato) {
    echo "Pedido confirmado: $plato\n";
}

function platoListo($plato) {
    echo "El plato está listo: $plato\n";
}

function entregarPedido($plato) {
    echo "El plato ha sido entregado: $plato\n";
}


function leerEntrada($mensaje) {
    echo $mensaje;
    $entrada = trim(fgets(STDIN));
    return $entrada;
}


echo "Simulador de pedidos de un restaurante\n\n";

while (true) {
    $plato = leerEntrada("Ingrese el nombre del plato (o escriba 'salir' para terminar): ");
    if (strtolower($plato) == 'salir') {
        break;
    }
    procesarPedido($plato, 'confirmarPedido', 'platoListo', 'entregarPedido');
    echo "\n";
}

echo "Fin de la simulación de pedidos.\n";