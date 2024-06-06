<?php

    class Animal {
        private $nombre;

        public function __construct ($nombre){
            $this->nombre = $nombre;
        
        }
        public function getNombre() {
            return $this->nombre;
        }
        public function sonido() {
            return "Sonido de animal";
        }
    }

    class Perro extends Animal {

        public function __construct($nombre) {
            parent::__construct($nombre);
        }
        public function sonido() {
            return "EL perro de nombre {$this->getNombre()} hace el sonido Guau";
        }
    }
       

    class Gato extends Animal {
        public function __construct($nombre) {
            parent::__construct($nombre);
        }
        public function sonido() {
            return "EL gato de nombre {$this->getNombre()} hace el sonido Miau";
        }
    }

    $perro = new Perro("Milu");
    echo $perro->sonido();
    echo "\n";
    $gato = new Gato("Garfield");
    echo $gato->sonido();

    // EXTRA

    class Empleado {
        private $id;
        private $name;

        public function __construct($id, $name) {
            $this->id = $id;
            $this->name = $name;
        }

        public function getId(){
            return $this->id;
        }

        public function getName(){
            return $this->name;
        }
    }

    class Gerente extends Empleado {
        private $empleados = [];
        
        public function __construct($id , $name, $empleados) {
            parent::__construct($id, $name);
            $this->empleados = $empleados;
        }

        public function __toString(){
            $empleados = implode(", ", $this->empleados);
            return "El gerente {$this->getName()} tiene a su cargo a los empleados: {$empleados}";
        }

        public function gestion(){
            return "El gerente {$this->getName()} esta gestionando un total de " . count($this->empleados) . " gerentes de proyecto";
        }
    }

    class GerenteP extends Empleado{
        private $programadores = [];

        public function __construct($id, $name, $programadores){
            parent::__construct($id, $name);
            $this->programadores = $programadores;
        }

        public function __toString(){
            $programadores = implode(", ", $this->programadores);
            return "El gerente de proyecto {$this->getName()} tiene a su cargo los programadores: {$programadores}";
        }

        public function gestion(){
            return "El gerente de proyecto {$this->getName()} esta gestionando un total de " . count($this->programadores) . " programadores";
        }
    }

    class Programador extends Empleado {
        private $lenguajes = [];

        public function __construct($id, $name, $lenguajes){
            parent::__construct($id, $name);
            $this->lenguajes = $lenguajes;
        }

        public function __toString(){
            $lenguajes = implode(", ", $this->lenguajes);
            return "El programador {$this->getName()} sabe los lenguajes: {$lenguajes}";
        }

        public function programar(){
            return "El programador {$this->getName()} esta programando en un total de " . count($this->lenguajes) . " lenguajes";
        }
    }


    echo "\n";

    $gerente1 = new Gerente (1, "Miguel", ["Juan", "Pedro", "Luis"]);
    echo $gerente1;
    echo "\n";
    echo $gerente1->gestion();
    echo "\n";


    $gerente2 = new Gerente (2, "Luis", ["Maria", "Ana"]);
    echo $gerente2 . "\n";
    echo $gerente2->gestion();
    echo "\n";

    $gerenteP1 = new GerenteP (3, "Juan", ["Carlos", "Jose"]);
    echo $gerenteP1 . "\n";
    echo $gerenteP1->gestion();
    echo "\n";

    $gerenteP2 = new GerenteP (4, "Ana", ["Sara", "Lucia"]);
    echo $gerenteP2 . "\n";
    echo $gerenteP2->gestion();
    echo "\n";

    $programador1 = new Programador (5, "Carlos", ["PHP", "JS"]);
    echo $programador1 . "\n";
    echo $programador1->programar();
    echo "\n";

    $programador2 = new Programador (6, "Jose", ["C#", "Python", "Ada", "Kotlin"]);
    echo $programador2 . "\n";
    echo $programador2->programar();
    echo "\n";
    
