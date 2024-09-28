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

echo "\n\n EJERCICIO EXTRA \n\n"; 

enum Status {
    case PENDIENTE;
    case ENVIADO;
    case ENTREGADO;
    case CANCELADO;
}
class Parcel {

    private $id;
    private $status;

    function __construct($id, $status) {
        $this->id = $id;
        $this->status = $status;
    }

    function __toString(){
        return "Paquete $this->id: {$this->status->name}\n";
    }

    function sendPackage($id) {
        if ($this->status == Status::PENDIENTE){
            echo "El paquete $id ya ha sido enviado\n";
            $this->status = Status::ENVIADO;
            return;
        }

        echo "El paquete $id no se encuentra preparado para el envío o ya no está en el sistema\n";
    }

    function deliverPackage($id) {
        if ($this->status == Status::ENVIADO){
            echo "El paquete $id ha sido entregado\n";
            $this->status = Status::ENTREGADO;
            return;
        }

        echo "El paquete $id no se encuentra en estado de envío\n";
    }

    function cancelPackage($id) {
        if ($this->status == Status::PENDIENTE){
            echo "El paquete $id ha sido cancelado\n";
            $this->status = Status::CANCELADO;
            return;
        }

        echo "El paquete $id no se encuentra en estado de envío\n";
    }
    
}

$parcel1 = new Parcel(1, Status::PENDIENTE);
$parcel2 = new Parcel(2, Status::PENDIENTE);
$parcel3 = new Parcel(3, Status::PENDIENTE);

echo $parcel1;
echo $parcel2;
echo $parcel3;

$parcel1->sendPackage(1);
$parcel2->deliverPackage(2);
$parcel3->cancelPackage(3);

$parcel1->deliverPackage(1);
$parcel2->sendPackage(2);
$parcel3->sendPackage(3);

echo $parcel1;
echo $parcel2;
echo $parcel3;




