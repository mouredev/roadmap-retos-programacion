<?php

function createTree($height, $hasStar, $decorations, $lightsOn) {
    $tree = [];
    // Estrella opcional
    if ($hasStar) {
        $tree[] = str_repeat(" ", $height - 1) . "@";
    }

    // Ramas
    for ($i = 1; $i <= $height; $i++) {
        $line = str_repeat(" ", $height - $i);
        for ($j = 0; $j < (2 * $i - 1); $j++) {
            if (isset($decorations[$i][$j])) {
                $line .= $decorations[$i][$j];
            } else {
                $line .= "*";
            }
        }
        $tree[] = $line;
    }

    // Tronco
    $trunkPadding = str_repeat(" ", $height - 2); // Ajustamos el padding para centrar
    $tree[] = $trunkPadding . "|||";
    $tree[] = $trunkPadding . "|||";

    return $tree;
}

function displayTree($tree) {
    foreach ($tree as $line) {
        echo $line . PHP_EOL;
    }
}

function addRandomDecoration(&$decorations, $height, $type, $count) {
    $added = 0;
    while ($added < $count) {
        $row = rand(1, $height);
        $col = rand(0, 2 * $row - 2);

        if (!isset($decorations[$row][$col])) {
            $decorations[$row][$col] = $type;
            $added++;
        }
    }
}

function removeRandomDecoration(&$decorations, $type, $count) {
    $removed = 0;
    foreach ($decorations as $row => &$cols) {
        foreach ($cols as $col => $decor) {
            if ($decor === $type && $removed < $count) {
                unset($cols[$col]);
                $removed++;
            }
        }
    }
}

function toggleLights(&$decorations, $lightsOn) {
    foreach ($decorations as &$cols) {
        foreach ($cols as &$decor) {
            if ($decor === "+") {
                $decor = $lightsOn ? "+" : "*";
            }
        }
    }
}

$height = (int)readline("Ingrese la altura del árbol: ");
$hasStar = true;
$decorations = [];
$lightsOn = true;

while (true) {
    $tree = createTree($height, $hasStar, $decorations, $lightsOn);
    displayTree($tree);

    echo PHP_EOL . "Opciones: " . PHP_EOL;
    echo "1. Añadir/Eliminar estrella" . PHP_EOL;
    echo "2. Añadir bolas (o)" . PHP_EOL;
    echo "3. Eliminar bolas (o)" . PHP_EOL;
    echo "4. Añadir luces (+)" . PHP_EOL;
    echo "5. Eliminar luces (+)" . PHP_EOL;
    echo "6. Apagar/Encender luces" . PHP_EOL;
    echo "7. Salir" . PHP_EOL;

    $option = (int)readline("Seleccione una opción: ");

    switch ($option) {
        case 1:
            $hasStar = !$hasStar;
            echo $hasStar ? "Estrella añadida." : "Estrella eliminada." . PHP_EOL;
            break;
        case 2:
            addRandomDecoration($decorations, $height, "o", 2);
            echo "Bolas añadidas." . PHP_EOL;
            break;
        case 3:
            removeRandomDecoration($decorations, "o", 2);
            echo "Bolas eliminadas." . PHP_EOL;
            break;
        case 4:
            addRandomDecoration($decorations, $height, "+", 3);
            echo "Luces añadidas." . PHP_EOL;
            break;
        case 5:
            removeRandomDecoration($decorations, "+", 3);
            echo "Luces eliminadas." . PHP_EOL;
            break;
        case 6:
            $lightsOn = !$lightsOn;
            toggleLights($decorations, $lightsOn);
            echo $lightsOn ? "Luces encendidas." : "Luces apagadas." . PHP_EOL;
            break;
        case 7:
            echo "¡Feliz Navidad!" . PHP_EOL;
            exit;
        default:
            echo "Opción no válida." . PHP_EOL;
    }
}
