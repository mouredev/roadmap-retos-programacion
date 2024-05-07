<?php

// Enumeración de los días de la semana
enum DiaSemana: int {
    case LUNES = 1;
    case MARTES = 2;
    case MIERCOLES = 3;
    case JUEVES = 4;
    case VIERNES = 5;
    case SABADO = 6;
    case DOMINGO = 7;
}

function dayOfWeek($day) {
    switch ($day) {
        case DiaSemana::LUNES:
            return "Lunes";
        case DiaSemana::MARTES:
            return "Martes";
        case DiaSemana::MIERCOLES:
            return "Miércoles";
        case DiaSemana::JUEVES:
            return "Jueves";
        case DiaSemana::VIERNES:
            return "Viernes";
        case DiaSemana::SABADO:
            return "Sábado";
        case DiaSemana::DOMINGO:
            return "Domingo";
        default:
            return "Día no válido";
    }
}

echo dayOfWeek(DiaSemana::LUNES) . "\n";
echo dayOfWeek(7) . "\n";