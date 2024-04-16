<?php

// Superclase
class Animal {
    protected $nombre;
    protected $edad;

    public function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }
}

// Heredera Perro
class Perro extends Animal {
    public function sonido() {
        echo "¡guau guau!\n";
    }
}

// Heredera Gato
class Gato extends Animal {
    public function sonido() {
        echo "¡miau miau!\n";
    }
}

// Clase base abstracta para representar a un empleado genérico
abstract class Empleado {
    protected $id;
    protected $nombre;

    public function __construct($id, $nombre) {
        $this->id = $id;
        $this->nombre = $nombre;
    }

    abstract public function informacion();
}

// Clase Gerente hereda de Empleado
class Gerente extends Empleado {
    protected $empleadosACargo;

    public function __construct($id, $nombre) {
        parent::__construct($id, $nombre);
        $this->empleadosACargo = [];
    }

    public function agregarEmpleado($empleado) {
        $this->empleadosACargo[] = $empleado;
    }

    public function informacion() {
        echo "ID: {$this->id}, Nombre: {$this->nombre}\n";
        echo "Tipo: Gerente\n";
        echo "Empleados a cargo: " . count($this->empleadosACargo) . "\n";
    }
}

// Clase GerenteProyecto hereda de Gerente
class GerenteProyecto extends Gerente {
    protected $areaProyecto;

    public function __construct($id, $nombre, $areaProyecto) {
        parent::__construct($id, $nombre);
        $this->areaProyecto = $areaProyecto;
    }

    public function informacion() {
        parent::informacion();
        echo "Área del Proyecto: {$this->areaProyecto}\n";
    }
}

// Clase Programador hereda de Empleado
class Programador extends Empleado {
    protected $lenguaje;

    public function __construct($id, $nombre, $lenguaje) {
        parent::__construct($id, $nombre);
        $this->lenguaje = $lenguaje;
    }

    public function informacion() {
        parent::informacion();
        echo "Lenguaje: {$this->lenguaje}\n";
    }
}

// Creación de instancias de Perro y Gato
$miPerro = new Perro("Bobby", 5);
$miGato = new Gato("Whiskers", 3);

// Llamada a los métodos específicos de cada clase
$miPerro->sonido(); // Salida: ¡Guau Guau!
$miGato->sonido(); // Salida: ¡Miau Miau!

// Creación de instancias de empleados
$gerente1 = new Gerente(1, "Juan");
$gerenteProyecto1 = new GerenteProyecto(2, "María", "Desarrollo Web");
$programador1 = new Programador(3, "Pedro", "C#");

// Agregar empleados a cargo del gerente
$gerente1->agregarEmpleado($gerenteProyecto1);
$gerenteProyecto1->agregarEmpleado($programador1);

// Mostrar información de los empleados
echo "Información del Gerente:\n";
$gerente1->informacion();
echo "\nInformación del Gerente de Proyecto:\n";
$gerenteProyecto1->informacion();
echo "\nInformación del Programador:\n";
$programador1->informacion();
