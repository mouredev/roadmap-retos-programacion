<?php

/**
 * Clase Persona que representa a una persona con nombre y edad.
 */
class Persona {
    private $nombre;
    private $edad;

    // Constructor
    public function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }

    // Métodos getter y setter
    public function getNombre() {
        return $this->nombre;
    }

    public function setNombre($nombre) {
        $this->nombre = $nombre;
    }

    public function getEdad() {
        return $this->edad;
    }

    public function setEdad($edad) {
        $this->edad = $edad;
    }

    // Método para imprimir los datos de la persona
    public function imprimirDatos() {
        echo "Nombre: {$this->nombre}, Edad: {$this->edad}\n";
    }
}

/**
 * Clase Pila que implementa una estructura de datos de tipo pila (LIFO).
 */
class Pila {
    private $elementos;

    public function __construct() {
        $this->elementos = array();
    }

    public function push($elemento) {
        array_push($this->elementos, $elemento);
    }

    public function pop() {
        if (empty($this->elementos)) {
            return "La pila está vacía";
        }
        return array_pop($this->elementos);
    }

    public function size() {
        return count($this->elementos);
    }

    public function imprimirContenido() {
        echo "Contenido de la pila: " . implode(', ', $this->elementos) . "\n";
    }
}

/**
 * Clase Cola que implementa una estructura de datos de tipo cola (FIFO).
 */
class Cola {
    private $elementos;

    public function __construct() {
        $this->elementos = array();
    }

    public function enqueue($elemento) {
        array_push($this->elementos, $elemento);
    }

    public function dequeue() {
        if (empty($this->elementos)) {
            return "La cola está vacía";
        }
        return array_shift($this->elementos);
    }

    public function size() {
        return count($this->elementos);
    }

    public function imprimirContenido() {
        echo "Contenido de la cola: " . implode(', ', $this->elementos) . "\n";
    }
}

// Función principal para probar las implementaciones
function main() {
    // Prueba de la clase Persona
    $persona = new Persona("Juan", 30);
    $persona->imprimirDatos();
    $persona->setEdad(31);
    $persona->imprimirDatos();

    // Prueba de la Pila
    $pila = new Pila();
    $pila->push(1);
    $pila->push(2);
    $pila->push(3);
    $pila->imprimirContenido();
    echo "Elemento extraído de la pila: " . $pila->pop() . "\n";
    $pila->imprimirContenido();

    // Prueba de la Cola
    $cola = new Cola();
    $cola->enqueue("A");
    $cola->enqueue("B");
    $cola->enqueue("C");
    $cola->imprimirContenido();
    echo "Elemento extraído de la cola: " . $cola->dequeue() . "\n";
    $cola->imprimirContenido();
}

// Ejecutar la función principal
main();

?>