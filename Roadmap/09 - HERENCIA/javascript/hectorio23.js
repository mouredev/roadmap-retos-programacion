"use strict";


// Definición de la clase Animal
class Animal {
  // Constructor de la clase Animal
  constructor(sound) {
    this.sound = sound;
  }

  // Método que imprime el sonido del animal
  makeSound() {
    console.log(this.sound);
  }
}

// Definición de la subclase Perro que hereda de Animal
class Perro extends Animal {
  // Constructor de la clase Perro
  constructor() {
    // Llamada al constructor de la clase padre (Animal)
    super("Guau");
  }
}

// Definición de la subclase Gato que hereda de Animal
class Gato extends Animal {
  // Constructor de la clase Gato
  constructor() {
    // Llamada al constructor de la clase padre (Animal)
    super("Miau");
  }
}

// Función para imprimir el sonido de un animal
function imprimirSonido(animal) {
  animal.makeSound();
}

// Definición de la clase Empleado
class Empleado {
  // Constructor de la clase Empleado
  constructor(id, nombre) {
    this.id = id;
    this.nombre = nombre;
  }

  // Método para obtener el nombre del empleado
  getNombre() {
    return this.nombre;
  }

  // Método para obtener el identificador del empleado
  getId() {
    return this.id;
  }

  // Método para mostrar detalles del empleado
  mostrarDetalles() {
    console.log(`ID: ${this.id}, Nombre: ${this.nombre}`);
  }
}

// Definición de la subclase Gerente que hereda de Empleado
class Gerente extends Empleado {
  // Constructor de la clase Gerente
  constructor(id, nombre, departamento) {
    // Llamada al constructor de la clase padre (Empleado)
    super(id, nombre);
    this.departamento = departamento;
    this.empleadosACargo = [];
  }

  // Método para agregar empleados a su cargo
  agregarEmpleado(empleado) {
    this.empleadosACargo.push(empleado);
  }

  // Método para mostrar detalles del gerente
  mostrarDetalles() {
    super.mostrarDetalles();
    console.log(`Departamento: ${this.departamento}`);
    console.log("Empleados a cargo:");
    this.empleadosACargo.forEach((empleado) => {
      console.log(`  - ${empleado.getNombre()}`);
    });
  }
}

// Definición de la subclase GerenteProyecto que hereda de Gerente
class GerenteProyecto extends Gerente {
  // Constructor de la clase GerenteProyecto
  constructor(id, nombre, departamento, proyectos) {
    // Llamada al constructor de la clase padre (Gerente)
    super(id, nombre, departamento);
    this.proyectos = proyectos;
  }

  // Método para mostrar detalles del gerente de proyecto
  mostrarDetalles() {
    super.mostrarDetalles();
    console.log("Proyectos:");
    this.proyectos.forEach((proyecto) => {
      console.log(`  - ${proyecto}`);
    });
  }
}

// Definición de la subclase Programador que hereda de Empleado
class Programador extends Empleado {
  // Constructor de la clase Programador
  constructor(id, nombre, lenguaje) {
    // Llamada al constructor de la clase padre (Empleado)
    super(id, nombre);
    this.lenguaje = lenguaje;
  }

  // Método para mostrar detalles del programador
  mostrarDetalles() {
    super.mostrarDetalles();
    console.log(`Lenguaje: ${this.lenguaje}`);
  }
}

// Creación de instancias de Perro y Gato
const miPerro = new Perro();
const miGato = new Gato();

// Imprime el sonido del perro y del gato
imprimirSonido(miPerro); // Salida esperada: "Guau"
imprimirSonido(miGato); // Salida esperada: "Miau"

// Creación de instancias de empleados
const gerente1 = new Gerente(1, "Carlos", "Desarrollo");
const gerenteProyecto1 = new GerenteProyecto(2, "Laura", "Desarrollo", [
  "Proyecto A",
  "Proyecto B",
]);
const programador1 = new Programador(3, "Ana", "JavaScript");
const programador2 = new Programador(4, "Juan", "Python");

// Agregar empleados a cargo del gerente
gerente1.agregarEmpleado(gerenteProyecto1);
gerenteProyecto1.agregarEmpleado(programador1);
gerenteProyecto1.agregarEmpleado(programador2);

// Mostrar detalles de los empleados
console.log("Detalles del gerente:");
gerente1.mostrarDetalles();
console.log("\nDetalles del gerente de proyecto:");
gerenteProyecto1.mostrarDetalles();
console.log("\nDetalles del programador 1:");
programador1.mostrarDetalles();
console.log("\nDetalles del programador 2:");
programador2.mostrarDetalles();
