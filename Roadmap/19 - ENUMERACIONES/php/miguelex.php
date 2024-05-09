<?php

// Enumeración de los días de la semana
enum WeekDay: int {
    case LUNES = 1;
    case MARTES = 2;
    case MIERCOLES = 3;
    case JUEVES = 4;
    case VIERNES = 5;
    case SABADO = 6;
    case DOMINGO = 7;
}

function dayOfWeek($day){

    echo "El día de la semana correspondiente al número $day es: ";
    echo WeekDay::from($day)->name;
    echo "\n";
                
}

for ($i = 1; $i <= 7; $i++) {
    dayOfWeek($i);
}

// Extra

enum Status: int {
    case PENDIENTE = 1;
    case ENVIADO = 2;
    case ENTREGADO = 3;
    case CANCELADO = 4;
}
class Parcel {

    private $id;
    private $status;

    function __construct($id, $status) {
        $this->id = $id;
        $this->status = $status;
    }


}



