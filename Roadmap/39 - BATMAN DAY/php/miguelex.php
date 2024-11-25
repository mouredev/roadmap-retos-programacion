<?php

// RETO 1: 
function calcularBatmanDay($anioInicio, $anioFinal) {
    echo "Fechas del Batman Day hasta su 100 aniversario:\n";
    for ($anio = $anioInicio; $anio <= $anioFinal; $anio++) {
        $tercerSabado = new DateTime("third saturday of september $anio");
        echo "Batman Day en el año $anio: " . $tercerSabado->format('d-m-Y') . "\n";
    }
}

$anioInicio = 2024;
$anioFinal = 2024 + (100 - 85); 
calcularBatmanDay($anioInicio, $anioFinal);


// RETO 2
function activarSistemaSeguridad($sensores) {
    $tamanoMapa = 20;
    $umbralSeguridad = 20;
    $mejorSumaAmenazas = 0;
    $mejorCentro = null;

    for ($i = 0; $i <= $tamanoMapa - 3; $i++) {
        for ($j = 0; $j <= $tamanoMapa - 3; $j++) {
            $sumaAmenazas = 0;
            for ($x = $i; $x < $i + 3; $x++) {
                for ($y = $j; $y < $j + 3; $y++) {
                    $sumaAmenazas += $sensores[$x][$y];
                }
            }

            if ($sumaAmenazas > $mejorSumaAmenazas) {
                $mejorSumaAmenazas = $sumaAmenazas;
                $mejorCentro = [$i + 1, $j + 1]; // Centro de la cuadrícula
            }
        }
    }

    if ($mejorCentro) {
        $distanciaABatcueva = abs($mejorCentro[0]) + abs($mejorCentro[1]);
        echo "\nÁrea más amenazada en coordenadas (" . $mejorCentro[0] . ", " . $mejorCentro[1] . ")\n";
        echo "Suma de amenazas: $mejorSumaAmenazas\n";
        echo "Distancia a la Batcueva: $distanciaABatcueva\n";

        if ($mejorSumaAmenazas > $umbralSeguridad) {
            echo "¡Protocolo de seguridad activado!\n";
        } else {
            echo "Protocolo de seguridad NO activado.\n";
        }
    }
}

$sensores = [];
for ($i = 0; $i < 20; $i++) {
    for ($j = 0; $j < 20; $j++) {
        $sensores[$i][$j] = rand(0, 10);
    }
}

activarSistemaSeguridad($sensores);


