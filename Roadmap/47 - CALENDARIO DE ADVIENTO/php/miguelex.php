<?php
// Definimos el tamaño de las cuadrículas y el rango de días
const GRID_WIDTH = 4;
const GRID_HEIGHT = 3;
const DAYS = 24;

// Inicializamos los días descubiertos
$discovered = array_fill(1, DAYS, false);

function drawCalendar($discovered) {
    for ($row = 0; $row < ceil(DAYS / 6); $row++) {
        // Líneas superiores de las cuadrículas
        for ($line = 0; $line < GRID_HEIGHT; $line++) {
            for ($col = 0; $col < 6; $col++) {
                $day = $row * 6 + $col + 1;
                if ($day > DAYS) break;

                switch ($line) {
                    case 0:
                    case 2:
                        echo str_repeat("*", GRID_WIDTH) . " ";
                        break;
                    case 1:
                        echo "*";
                        echo $discovered[$day] 
                            ? str_repeat("*", GRID_WIDTH - 2) 
                            : str_pad(sprintf("%02d", $day), GRID_WIDTH - 2, " ", STR_PAD_BOTH);
                        echo "* ";
                        break;
                }
            }
            echo "\n";
        }
    }
}

while (true) {
    // Dibujamos el calendario
    drawCalendar($discovered);

    // Pedimos al usuario que elija un día
    echo "\nSeleccione un día (1-" . DAYS . ") para descubrir o escriba 0 para salir: ";
    $input = trim(fgets(STDIN));

    if ($input == 0) {
        echo "¡Gracias por participar en el aDEViento!\n";
        break;
    }

    if (!is_numeric($input) || $input < 1 || $input > DAYS) {
        echo "Por favor, elija un número válido entre 1 y " . DAYS . ".\n";
        continue;
    }

    if ($discovered[$input]) {
        echo "El día $input ya ha sido descubierto.\n";
    } else {
        $discovered[$input] = true;
        echo "¡Has descubierto el día $input!\n";
    }
}
