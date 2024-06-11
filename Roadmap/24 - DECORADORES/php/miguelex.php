<?php


    interface Vehicle {
        public function wheels();
    }

    class Car implements Vehicle {
        public function wheels() {
            return 4;
        }
    }

    class Bike implements Vehicle {
        public function wheels() {
            return 2;
        }
    }

    class VehicleDecorator implements Vehicle {
        protected $vehicle;

        public function __construct(Vehicle $vehicle) {
            $this->vehicle = $vehicle;
        }

        public function wheels() {
            return $this->vehicle->wheels();
        }
    }

    // Vamos a usar el patron decorador para definir ahora un tipo especial de coche que sol otien 2 puertas
    class Coupe extends VehicleDecorator {
        public function doors() {
            return ;
        }
    }

    $car = new Car();
    $bike = new Bike();
    $car->wheels();
    $bike->wheels();
    $carWithDoors = new Coupe($car);
    $carWithDoors->doors();
    $carWithDoors->wheels();





