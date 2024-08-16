<?php
define('SIZE', 6);

function generarLaberinto() {
    $laberinto = [];

    // Laberinto vacio
    for ($i = 0; $i < SIZE; $i++) {
        for ($j = 0; $j < SIZE; $j++) {
            $laberinto[$i][$j] = '⬜️'; 
        }
    }

    // obstáculos
    $numObstaculos = rand(5, 10); 

    for ($i = 0; $i < $numObstaculos; $i++) {
        do {
            $x = rand(0, SIZE - 1);
            $y = rand(0, SIZE - 1);
        } while ($laberinto[$x][$y] !== '⬜️'); 

        $laberinto[$x][$y] = '⬛️';
    }

    // Mickey
    do {
        $mickeyX = rand(0, SIZE - 1);
        $mickeyY = rand(0, SIZE - 1);
    } while ($laberinto[$mickeyX][$mickeyY] !== '⬜️');

    $laberinto[$mickeyX][$mickeyY] = '🐭';

    // salida
    do {
        $salidaX = rand(0, SIZE - 1);
        $salidaY = rand(0, SIZE - 1);
    } while ($laberinto[$salidaX][$salidaY] !== '⬜️');

    $laberinto[$salidaX][$salidaY] = '🚪';

    return [$laberinto, $mickeyX, $mickeyY, $salidaX, $salidaY];
}

function mostrarLaberintoCiego($laberinto, $mickeyX, $mickeyY) {
    for ($i = 0; $i < SIZE; $i++) {
        for ($j = 0; $j < SIZE; $j++) {
            if ($i === $mickeyX && $j === $mickeyY) {
                echo '🐭 ';
            } elseif (abs($i - $mickeyX) <= 1 && abs($j - $mickeyY) <= 1) {
                echo $laberinto[$i][$j] . ' ';
            } else {
                echo '❓ '; // Celda desconocida
            }
        }
        echo PHP_EOL;
    }
}


function mostrarLaberinto($laberinto) {
    foreach ($laberinto as $fila) {
        echo implode(' ', $fila) . PHP_EOL;
    }
}

function moverMickey($direccion, &$mickeyX, &$mickeyY, &$laberinto, $salidaX, $salidaY) {
    $nuevaX = $mickeyX;
    $nuevaY = $mickeyY;

    switch ($direccion) {
        case 'a': 
            $nuevaX--;
            break;
        case 'b': 
            $nuevaX++;
            break;
        case 'i': 
            $nuevaY--;
            break;
        case 'd': 
            $nuevaY++;
            break;
        default:
            echo "Dirección no válida. Intenta de nuevo.\n";
            return false;
    }


    if ($nuevaX < 0 || $nuevaX >= SIZE || $nuevaY < 0 || $nuevaY >= SIZE) {
        echo "¡No puedes salirte del laberinto!\n";
        return false;
    }

    if ($laberinto[$nuevaX][$nuevaY] === '⬛️') {
        echo "¡Hay un obstáculo en esa dirección!\n";
        return false;
    }

    $laberinto[$mickeyX][$mickeyY] = ($mickeyX === $salidaX && $mickeyY === $salidaY) ? '🚪' : '⬜️'; // Mantener la puerta si estaba ahí
    $mickeyX = $nuevaX;
    $mickeyY = $nuevaY;
    $laberinto[$mickeyX][$mickeyY] = '🐭';

    if ($mickeyX === $salidaX && $mickeyY === $salidaY) {
        return true;
    }

    return false;
}

function jugar() {
    list($laberinto, $mickeyX, $mickeyY, $salidaX, $salidaY) = generarLaberinto();

    while (true) {
        mostrarLaberintoCiego($laberinto, $mickeyX, $mickeyY);

        echo "¿Hacia dónde te gustaría mover a Mickey? (a=arriba, b=abajo, i=izquierda, d=derecha): ";
        $direccion = trim(fgets(STDIN));

        if (moverMickey($direccion, $mickeyX, $mickeyY, $laberinto, $salidaX, $salidaY)) {
            echo "¡Felicidades! Mickey ha llegado a la salida.\n";
            mostrarLaberinto($laberinto); 
            break;
        }
    }
}

jugar();
