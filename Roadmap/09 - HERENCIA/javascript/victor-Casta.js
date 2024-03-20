/*
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
*/

class Animal {
  constructor(name, sonido) {
    this.name = name;
    this.sonido = sonido;
  }

  emitirSonido() {
    console.log(this.sonido);
  }
}

class Perro extends Animal {
  constructor(name) {
    super(name, "Guau guau");
  }
}

class Gato extends Animal {
  constructor(name) {
    super(name, "Miau miau");
  }
}

const mi_perro = new Perro("Rufo");
const mi_gato = new Gato("Bigotes");

mi_perro.emitirSonido(); // Output: Guau guau
mi_gato.emitirSonido(); // Output: Miau miau


/*
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
*/
class Empleado {
  constructor(identificador, nombre) {
    this.identificador = identificador;
    this.nombre = nombre;
  }
}

class Gerente extends Empleado {
  constructor(identificador, nombre, clientes) {
    super(identificador, nombre);
    this.clientes = clientes;
    this.subordinados = []; // Almacenar empleados a cargo
  }
  
  agregarSubordinado(empleado) {
    this.subordinados.push(empleado);
  }
}

class GerenteDeProyecto extends Empleado {
  constructor(identificador, nombre, proyecto) {
    super(identificador, nombre);
    this.proyecto = proyecto;
    this.subordinados = []; // Almacenar empleados a cargo
  }
  
  agregarSubordinado(empleado) {
    this.subordinados.push(empleado);
  }
}

class Programador extends Empleado {
  constructor(identificador, nombre, lenguaje) {
    super(identificador, nombre);
    this.lenguaje = lenguaje;
  }
}

// Ejemplo de uso:
const gerente1 = new Gerente(1, "Juan", ["Cliente A", "Cliente B"]);
const gerenteDeProyecto1 = new GerenteDeProyecto(2, "Pedro", "Proyecto X");
const programador1 = new Programador(3, "María", "JavaScript");

// Asignar subordinados a un gerente
gerente1.agregarSubordinado(gerenteDeProyecto1);
gerenteDeProyecto1.agregarSubordinado(programador1);
