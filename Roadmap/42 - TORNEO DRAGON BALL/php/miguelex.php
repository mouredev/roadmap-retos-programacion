<?php

class Luchador {
    public $nombre;
    public $velocidad;
    public $ataque;
    public $defensa;
    public $salud = 100;

    public function __construct($nombre, $velocidad, $ataque, $defensa) {
        $this->nombre = $nombre;
        $this->velocidad = $velocidad;
        $this->ataque = $ataque;
        $this->defensa = $defensa;
    }

    public function esquivar() {
        return mt_rand(1, 100) <= 20;
    }
}

function batalla($luchador1, $luchador2) {
    echo "¡Batalla entre {$luchador1->nombre} y {$luchador2->nombre}!\n";

    $atacante = $luchador1->velocidad >= $luchador2->velocidad ? $luchador1 : $luchador2;
    $defensor = $atacante === $luchador1 ? $luchador2 : $luchador1;

    while ($luchador1->salud > 0 && $luchador2->salud > 0) {
        if ($defensor->esquivar()) {
            echo "{$defensor->nombre} esquivó el ataque de {$atacante->nombre}!\n";
        } else {
            $danio = $atacante->ataque - $defensor->defensa;
            if ($danio <= 0) {
                $danio = $atacante->ataque * 0.1; // Recibe un 10% del ataque si la defensa es mayor
            }
            $defensor->salud -= $danio;
            echo "{$atacante->nombre} ataca a {$defensor->nombre} y causa {$danio} de daño. Salud restante de {$defensor->nombre}: {$defensor->salud}\n";
        }

        $temp = $atacante;
        $atacante = $defensor;
        $defensor = $temp;
    }

    $ganador = $luchador1->salud > 0 ? $luchador1 : $luchador2;
    echo "¡{$ganador->nombre} es el ganador de la batalla!\n\n";
    return $ganador;
}

function torneo($luchadores) {
    if ((count($luchadores) & (count($luchadores) - 1)) != 0) {
        echo "El número de luchadores debe ser una potencia de 2.\n";
        return;
    }

    echo "¡Comienza el torneo de Dragon Ball: Sparking! ZERO!\n\n";
    while (count($luchadores) > 1) {
        $luchadoresRestantes = [];
        shuffle($luchadores);
        for ($i = 0; $i < count($luchadores); $i += 2) {
            $ganador = batalla($luchadores[$i], $luchadores[$i + 1]);
            $luchadoresRestantes[] = $ganador;
        }
        $luchadores = $luchadoresRestantes;
    }

    echo "¡El ganador del torneo es {$luchadores[0]->nombre}!\n";
}

function agregarLuchadores() {
    $luchadores = [];
    echo "Ingrese el número de luchadores (debe ser una potencia de 2): ";
    $numLuchadores = (int)trim(fgets(STDIN));

    if (($numLuchadores & ($numLuchadores - 1)) != 0 || $numLuchadores <= 0) {
        echo "El número de luchadores debe ser una potencia de 2.\n";
        exit();
    }

    for ($i = 0; $i < $numLuchadores; $i++) {
        echo "Ingrese el nombre del luchador " . ($i + 1) . ": ";
        $nombre = trim(fgets(STDIN));

        echo "Ingrese la velocidad de {$nombre} (0-100): ";
        $velocidad = (int)trim(fgets(STDIN));

        echo "Ingrese el ataque de {$nombre} (0-100): ";
        $ataque = (int)trim(fgets(STDIN));

        echo "Ingrese la defensa de {$nombre} (0-100): ";
        $defensa = (int)trim(fgets(STDIN));

        $luchadores[] = new Luchador($nombre, $velocidad, $ataque, $defensa);
    }

    return $luchadores;
}

$luchadores = agregarLuchadores();
torneo($luchadores);


