<?php

//Mecanismo LIFO
$pila = [];
echo "\n--- Mecanismo LIFO ---\n";
// Se introduce los valores en el array
array_push ($pila, 'coche');
array_push ($pila, 'moto');
array_push ($pila, 'camión');



echo "\nContenido del array; \n";
foreach( $pila as $vehiculos) {
    echo $vehiculos . "\n";
}
// Se sacan los valores del array
$valorExtraido = array_pop($pila);
echo "\nValor extraido: $valorExtraido \n";

echo "\nContenido del array actual; \n";
foreach( $pila as $vehiculos) {
    echo $vehiculos . "\n";
}

// Mecanismo FIFO---------------------------------------
echo "\n--- Mecanismo FIFO ---\n";
$cola = [];
// Se introduce los valores en el array
array_push ($cola, 'Manzana');
array_push ($cola, 'Pera');
array_push ($cola, 'Limón');



echo "\nContenido del array; \n";
foreach( $cola as $frutas) {
    echo $frutas . "\n";
}
// Se sacan los valores del array
$valorExtraidoFIFO = array_shift($cola);
echo "\nValor extraido: $valorExtraidoFIFO \n";

echo "\nContenido del array actual; \n";
foreach( $cola as $frutas) {
    echo $frutas . "\n";
}

echo "\n--- EXTRA ---\n";
//Extra
$historialAtras = [];
$historialAdelante = [];

function nuevaWeb($web) {
    GLOBAL $historialAtras;
    GLOBAL $historialAdelante;

    array_push($historialAtras, $web);// Se mete la nueva web en el historial.
    $historialAdelante = []; // Se resetea el historialAdelante.

    echo "Navegando a: " . $web .  "\n";
}

function atras() {
    GLOBAL $historialAdelante;
    GLOBAL $historialAtras;

    if (count($historialAtras) > 1) {// Se necesita como mínimo dos páginas web en el historial.
        $paginaActual = array_pop($historialAtras); // Sacamos la página actual de la pila de atrás.

        array_push($historialAdelante, $paginaActual); // La enviamos a la pila de adelante, por si el ususario pulsa "Adelante".

        echo "Se pulsa Atrás. Web actual: " . end($historialAtras) . "\n";

    }else {
        echo "Se pulsa Atrás. No hay más páginas en el historial. \n ";
    }
}

function adelante() {
    GLOBAL $historialAtras;
    GLOBAL $historialAdelante;

    // Si hay páginas en la pila de adelante, podemos avanzar
    if (count($historialAdelante) > 0) {
        // 1. Sacamos la página de la pila de adelante
        $paginaSiguiente = array_pop($historialAdelante);
        
        // 2. La devolvemos a la pila de atrás (vuelve a ser la actual)
        array_push($historialAtras, $paginaSiguiente);

        echo "Se pulsa Adelante. Web actual: " . end($historialAtras) . "\n";
    } else {
        echo "Se pulsa Adelante. No puedes avanzar más.\n";
    }
}

// Pruebas

nuevaWeb('www.tualbornoz.com');
nuevaWeb('www.acerogourmet.es');
nuevaWeb('www.google.com');

atras();
atras();
adelante();
nuevaWeb('www.laravel.tualbornoz.com');
adelante();