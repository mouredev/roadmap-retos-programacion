<?php
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
  * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 */
class Animal{
    protected $nombre;
    protected $sonido;

    public function __construct($nombre, $sonido){
        $this->nombre = $nombre;
        $this->sonido = $sonido;
    }
    public function hacerSonido(){
        return $this->nombre . " " . $this->sonido;
    }
}

class Perro extends Animal {
    public function __construct($nombre){
        parent::__construct($nombre, "ladra.");
    }
}

class Gato extends Animal {
    public function __construct($nombre){
        parent::__construct($nombre, "maulla.");
    }
}

function imprimirSonido(Animal $animal) {
    echo $animal->hacerSonido() . PHP_EOL;
}

$perro = new Perro("Pluto");
$gato = new Gato("Garfield");
imprimirSonido($perro);
imprimirSonido($gato);



 /* DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */

// Definición de la clase Empleado
class Empleado {
    protected $id;
    protected $nombre;

    public function __construct($id, $nombre) {
        $this->id = $id;
        $this->nombre = $nombre;
    }

    public function getId() {
        return $this->id;
    }

    public function getNombre() {
        return $this->nombre;
    }
}

// Definición de la clase Gerente que hereda de Empleado
class Gerente extends Empleado {
    protected $empleadosACargo;

    public function __construct($id, $nombre) {
        parent::__construct($id, $nombre);
        $this->empleadosACargo = [];
    }

    public function agregarEmpleado(Empleado $empleado) {
        $this->empleadosACargo[] = $empleado;
    }

    public function getEmpleadosACargo() {
        return $this->empleadosACargo;
    }
}

// Definición de la clase GerenteProyecto que hereda de Gerente
class GerenteProyecto extends Gerente {
    protected $proyectoAsignado;

    public function __construct($id, $nombre, $proyectoAsignado) {
        parent::__construct($id, $nombre);
        $this->proyectoAsignado = $proyectoAsignado;
    }

    public function getProyectoAsignado() {
        return $this->proyectoAsignado;
    }
}

// Definición de la clase Programador que hereda de Empleado
class Programador extends Empleado {
    protected $lenguaje;

    public function __construct($id, $nombre, $lenguaje) {
        parent::__construct($id, $nombre);
        $this->lenguaje = $lenguaje;
    }

    public function getLenguaje() {
        return $this->lenguaje;
    }
}

// Crear instancias de empleados
$gerente1 = new Gerente(1, "MoureDev");
$gerente2 = new GerenteProyecto(2, "Carlos", "Pilbeo");
$programador1 = new Programador(3, "Jose", "PHP");
$programador2 = new Programador(4, "Cristina", "JavaScript");

// Agregar empleados a cargo del gerente
$gerente1->agregarEmpleado($gerente2);
$gerente1->agregarEmpleado($programador1);
$gerente1->agregarEmpleado($programador2);

$gerente2->agregarEmpleado($programador1);
$gerente2->agregarEmpleado($programador2);

// Mostrar información
echo "Información del Gerente:" . PHP_EOL;
echo "ID: " . $gerente1->getId() . ", Nombre: " . $gerente1->getNombre() . PHP_EOL;
echo "Empleados contratados:" . PHP_EOL;
foreach ($gerente1->getEmpleadosACargo() as $empleado) {
    echo "- ID: " . $empleado->getId() . ", Nombre: " . $empleado->getNombre() . PHP_EOL;
}

echo "Información del Gerente Proyecto:" . PHP_EOL;
echo "ID: " . $gerente2->getId() . ", Nombre: " . $gerente2->getNombre() . PHP_EOL;
echo "Proyecto Asignado: " . $gerente2->getProyectoAsignado() . PHP_EOL;
echo "Empleados a cargo:" . PHP_EOL;
foreach ($gerente2->getEmpleadosACargo() as $empleado) {
    echo "- ID: " . $empleado->getId() . ", Nombre: " . $empleado->getNombre() . PHP_EOL;
}

echo "Información del Programador 1:" . PHP_EOL;
echo "ID: " . $programador1->getId() . ", Nombre: " . $programador1->getNombre() . PHP_EOL;
echo "Lenguaje: " . $programador1->getLenguaje() . PHP_EOL;

echo "Información del Programador 2:" . PHP_EOL;
echo "ID: " . $programador2->getId() . ", Nombre: " . $programador2->getNombre() . PHP_EOL;
echo "Lenguaje: " . $programador2->getLenguaje() . PHP_EOL;

