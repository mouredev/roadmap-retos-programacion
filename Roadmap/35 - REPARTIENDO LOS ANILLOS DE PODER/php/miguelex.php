<?php

function esPrimo($num) {
    if ($num <= 1) return false;
    if ($num == 2) return true;
    if ($num % 2 == 0) return false;
    
    for ($i = 3; $i <= sqrt($num); $i += 2) {
        if ($num % $i == 0) return false;
    }
    return true;
}

function repartirAnillos($totalAnillos) {
    if ($totalAnillos < 4) {
        return "Error: No hay suficientes anillos para cumplir con los requisitos.";
    }

    $anillosSauron = 1;
    $totalAnillos -= 1;
    
    $mejorDiferencia = PHP_INT_MAX;
    $mejorReparto = null;
    
    for ($anillosElfos = 1; $anillosElfos <= $totalAnillos; $anillosElfos += 2) {
        for ($anillosEnanos = 2; $anillosEnanos <= $totalAnillos; $anillosEnanos++) {
            if (esPrimo($anillosEnanos)) {
                $anillosHombres = $totalAnillos - $anillosElfos - $anillosEnanos;
                
                if ($anillosHombres > 0 && $anillosHombres % 2 == 0) {
                    $diferencia = max($anillosElfos, $anillosEnanos, $anillosHombres) - min($anillosElfos, $anillosEnanos, $anillosHombres);
                    
                    if ($diferencia < $mejorDiferencia) {
                        $mejorDiferencia = $diferencia;
                        $mejorReparto = [
                            'Elfos' => $anillosElfos,
                            'Enanos' => $anillosEnanos,
                            'Hombres' => $anillosHombres,
                            'Sauron' => $anillosSauron
                        ];
                    }
                }
            }
        }
    }
    
    if ($mejorReparto) {
        return "Reparto exitoso: Elfos = {$mejorReparto['Elfos']}, Enanos = {$mejorReparto['Enanos']}, Hombres = {$mejorReparto['Hombres']}, Sauron = {$mejorReparto['Sauron']}";
    } else {
        return "Error: No se encontró una combinación válida para repartir los anillos.";
    }
}

echo "Ingresa el número total de anillos: ";
$totalAnillos = intval(readline());

$resultado = repartirAnillos($totalAnillos);
echo $resultado;


