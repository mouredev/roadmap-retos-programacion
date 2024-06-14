<?php
    enum DiasSemana: int {
        case Lunes = 1;
        case Martes = 2;
        case Miercoles = 3;
        case Jueves = 4;
        case Viernes = 5;
        case Sabado = 6;
        case Domingo = 7;

        public function label(): string {
            return match($this) {
                static::Lunes => 'Lunes',
                static::Martes => 'Martes',
                static::Miercoles => 'Miércoles',
                static::Jueves => 'Jueves',
                static::Viernes => 'Viernes',
                static::Sabado => 'Sábado',
                static::Domingo => 'Domingo'
            };
        }
    }

    function getNameDay($day) {
        if (in_array($day, [1, 2, 3, 4, 5, 6, 7])) {
            return DiasSemana::from($day)->label();
        } else {
            return "Número de día no válido.  Debe estar en el rango de 1 a 7";
        }        
    }

    for ($i = 0; $i <=10; $i++) {
        echo getNameDay($i), "\n";
    } 
