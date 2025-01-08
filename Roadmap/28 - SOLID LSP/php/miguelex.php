<?php

    // Ejercicio basico sin LSP

    class Bird {
        public function fly() {
            return "Puedo volar\n";
        }
    }

    class Canary extends Bird {

        public function name(){
            return "Soy un canario\n";
        }
    }

    class Ostrich extends Bird {

        public function name(){
            return "Soy un avestruz\n";
        }

        public function fly() {
            return "No puedo volar (sobreescribi el método)\n";
        }
    }

    echo "Sin LSP\n";
    $canary = new Canary();
    echo $canary->name();
    echo $canary->fly();

    $ostrich = new Ostrich();
    echo $ostrich->name();
    echo $ostrich->fly();

    // Vemos que hemos tenido que sobreescribir el metodo fly para el avestruz. Esto incumple el LSP

    // Ejercicio basico con LSP

    interface Bird2 {
        public function fly();
    }

    class Canary2 implements Bird2 {

        public function name(){
            return "Soy un canario\n";
        }

        public function fly() {
            return "Puedo volar\n";
        }
    }

    class Ostrich2 implements Bird2 {

        public function name(){
            return "Soy un avestruz\n";
        }

        public function fly() {
            return "No puedo volar\n";
        }
    }

    echo "\n";
    echo "Con LSP\n";
    $canary2 = new Canary2();
    echo $canary2->name();
    echo $canary2->fly();
    echo "\n";
    $ostrich2 = new Ostrich2();
    echo $ostrich2->name();
    echo $ostrich2->fly();

    //Al tener la interface no me ha sido necesario sobreescribir nada. Lo implemento (o no) segun mis necesidades

    // Ejercicio Extra

    echo "\n";
    echo "Ejercicio Extra\n";

    interface Vehicle {
        public function speed();
        public function accelerate();
        public function brake();
    }

    class Car implements Vehicle {
        private $speed;

        public function __construct(){
            $this->speed = 0;
        }

        public function speed(){
            return $this->speed;
        }

        public function accelerate(){
            $this->speed += 10;
        }

        public function brake(){
            $this->speed -= 10;
        }
    }

    class Bicycle implements Vehicle {
        private $speed;

        public function __construct(){
            $this->speed = 0;
        }

        public function speed(){
            return $this->speed;
        }

        public function accelerate(){
            $this->speed += 5;
        }

        public function brake(){
            $this->speed -= 5;
        }
    }

    class Truck implements Vehicle {
        private $speed;

        public function __construct(){
            $this->speed = 0;
        }

        public function speed(){
            return $this->speed;
        }

        public function accelerate(){
            $this->speed += 2;
        }

        public function brake(){
            $this->speed -= 2;
        }
    }

    function testVehicle(Vehicle $vehicle){
        echo "Velocidad: ".$vehicle->speed()."\n";
        $vehicle->accelerate();
        echo "Velocidad: ".$vehicle->speed()."\n";
        $vehicle->accelerate();
        echo "Velocidad: ".$vehicle->speed()."\n";
        $vehicle->brake();
        echo "Velocidad: ".$vehicle->speed()."\n";
    }

    $car = new Car();
    $bike = new Bicycle();
    $truck = new Truck();

    echo "Vamos a probar el coche:\n";
    testVehicle($car);
    echo "Vamos a probar la bicicleta:\n";
    testVehicle($bike);
    echo "Vamos a probar el camion:\n";
    testVehicle($truck);
