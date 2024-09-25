<?php

// Ejemplo de implementación del concepto de herencia en PHP

// Definición de la clase base (superclase) Animal
class Animal {
  protected $especie;
  protected $sonido;

  public function __construct($especie, $sonido) {
    $this->especie = $especie;
    $this->sonido = $sonido;
  }

  // Método que muestra el sonido que hace el animal
  public function hacerSonido() {
    return "El " . $this->especie . " hace: " . $this->sonido;
  }
}

// Definición de la subclase Perro
class Perro extends Animal {
  private $nombre;

  public function __construct($nombre, $especie, $sonido) {
    parent::__construct($especie, $sonido); // Llamada al constructor de la superclase
    $this->nombre = $nombre;
  }

  // Método exclusivo de la subclase Perro
  public function ladrar() {
    return $this->nombre . " lanza un ladrido";
  }
}

// Definición de la subclase Gato
class Gato extends Animal {
  private $nombre;

  public function __construct($nombre, $especie, $sonido) {
    parent::__construct($especie, $sonido); // Llamada al constructor de la superclase
    $this->nombre = $nombre;
  }

  // Método exclusivo de la subclase Gato
  public function maullar() {
    return $this->nombre . " emite un maullido";
  }
}

// Ejemplo de implementación adicional (dificultad extra)
// Definición de la clase base (superclase) Empleado
class Empleado {
  protected $id;
  protected $nombre;

  public function __construct($id, $nombre) {
    $this->id = $id;
    $this->nombre = $nombre;
  }
}

// Definición de la subclase Gerente que hereda de Empleado
class Gerente extends Empleado {
  private $subordinados;

  public function __construct($id, $nombre, array $subordinados) {
    parent::__construct($id, $nombre);
    $this->subordinados = $subordinados;
  }

  // Método exclusivo de la subclase Gerente
  public function informarSobreSubordinados() {
    $informacion = "El gerente " . $this->nombre . " tiene a los siguientes subordinados: \n";
    foreach ($this->subordinados as $subordinado) {
      $informacion .= " - " . $subordinado->nombre . "\n";
    }
    return $informacion;
  }
}

// Definición de la subclase GerenteDeProyectos que hereda de Empleado
class GerenteDeProyectos extends Empleado {
  private $proyectos;

  public function __construct($id, $nombre, array $proyectos) {
    parent::__construct($id, $nombre);
    $this->proyectos = $proyectos;
  }

  // Método exclusivo de la subclase GerenteDeProyectos
  public function informarSobreProyectos() {
    $informacion = "El gerente de proyectos " . $this->nombre . " tiene los siguientes proyectos: \n";
    foreach ($this->proyectos as $proyecto) {
      $informacion .= " - " . $proyecto . "\n";
    }
    return $informacion;
  }
}

// Definición de la subclase Programador que hereda de Empleado
class Programador extends Empleado {
  private $lenguajes;

  public function __construct($id, $nombre, array $lenguajes) {
    parent::__construct($id, $nombre);
    $this->lenguajes = $lenguajes;
  }

  // Método exclusivo de la subclase Programador
  public function informarSobreLenguajes() {
    $informacion = "El programador " . $this->nombre . " domina los siguientes lenguajes: \n";
    foreach ($this->lenguajes as $lenguaje) {
      $informacion .= " - " . $lenguaje . "\n";
    }
    return $informacion;
  }
}

// Ejemplo de uso
$perro = new Perro("Lucky", "Perro", "Gua");
echo $perro->hacerSonido(); // El Perro hace: Gua
echo $perro->ladrar(); // Lucky lanza un ladrido

$gato = new Gato("Whiskers", "Gato", "Miau");
echo $gato->hacerSonido(); // El Gato hace: Miau
echo $gato->maullar(); // Whiskers emite un maullido

$gerente = new Gerente(1, "Juan Perez", [new Programador(2, "Maria Rodriguez", ["JavaScript", "PHP"])]);
echo $gerente->informarSobreSubordinados();

$gerenteProyectos = new GerenteDeProyectos(3, "Luis Martinez", ["Proyecto A", "Proyecto B"]);
echo $gerenteProyectos->informarSobreProyectos();

$programador = new Programador(4, "Karla Sanchez", ["JavaScript", "PHP"]);
echo $programador->informarSobreLenguajes();