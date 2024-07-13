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
            return 2;
        }
    }

    $car = new Car();
    $bike = new Bike();
    echo "Un coche tiene ".$car->wheels()." ruedas\n";
    echo "Una bicicleta tiene ".$bike->wheels(). " ruedas\n";
    $carWithDoors = new Coupe($car);
    echo "Prueba de uso de decorador\n";    
    echo "Un coche modelo Coupe tiene ".$carWithDoors->wheels(). " ruedas pero solo tiene ".$carWithDoors->doors()." puertas\n";

    // Ejercicio extra

    echo "\n\nEjercicio extra\n";
    

    interface Funcion {
        public function ejecutar();
    }

    class Suma implements Funcion {
        private $a;
        private $b;

        public function __construct($a, $b) {
            $this->a = $a;
            $this->b = $b;
        }

        public function ejecutar() {
            return $this->a + $this->b;
        }
    }

    class ContadorDeLlamadas implements Funcion {
        private $funcion;
        private static $contador = 0;

        public function __construct(Funcion $funcion) {
            $this->funcion = $funcion;
        }

        public function ejecutar() {
            self::$contador++;
            echo "La función ha sido llamada " . self::$contador . " veces.\n";
            return $this->funcion->ejecutar();
        }
    }

    $suma = new Suma(2, 2);
    $sumaContada = new ContadorDeLlamadas($suma);

    echo $sumaContada->ejecutar() . "\n";
    echo $sumaContada->ejecutar() . "\n";
    echo $sumaContada->ejecutar() . "\n";



