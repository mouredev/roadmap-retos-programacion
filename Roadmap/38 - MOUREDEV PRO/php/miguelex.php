<?php
function obtenerSuscriptoresActivos($archivoCsv) {
    $suscriptores = [];

    if (($handle = fopen($archivoCsv, "r")) !== FALSE) {
        fgetcsv($handle); 
        
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $id = $data[0];
            $email = $data[1];
            $status = $data[2];

            if (strtolower($status) === "activo") {
                $suscriptores[] = ['id' => $id, 'email' => $email];
            }
        }
        fclose($handle);
    }

    return $suscriptores;
}

function seleccionarGanadores($suscriptores, $numeroGanadores) {
    if (count($suscriptores) < $numeroGanadores) {
        return null; 
    }

    $ganadores = [];
    $indicesSeleccionados = [];

    while (count($ganadores) < $numeroGanadores) {
        $indiceAleatorio = rand(0, count($suscriptores) - 1);

        if (!in_array($indiceAleatorio, $indicesSeleccionados)) {
            $ganadores[] = $suscriptores[$indiceAleatorio];
            $indicesSeleccionados[] = $indiceAleatorio;
        }
    }

    return $ganadores;
}

$archivoCsv = 'suscriptores.csv';

$suscriptoresActivos = obtenerSuscriptoresActivos($archivoCsv);

if (count($suscriptoresActivos) > 0) {
    $ganadores = seleccionarGanadores($suscriptoresActivos, 3);

    if ($ganadores) {
        echo "Ganador de la suscripción:\n";
        echo "ID: " . $ganadores[0]['id'] . " | Email: " . $ganadores[0]['email'] . "\n\n";

        echo "Ganador del descuento:\n";
        echo "ID: " . $ganadores[1]['id'] . " | Email: " . $ganadores[1]['email'] . "\n\n";

        echo "Ganador del libro:\n";
        echo "ID: " . $ganadores[2]['id'] . " | Email: " . $ganadores[2]['email'] . "\n\n";
    } else {
        echo "No hay suficientes suscriptores activos para seleccionar 3 ganadores.\n";
    }
} else {
    echo "No hay suscriptores activos.\n";
}

