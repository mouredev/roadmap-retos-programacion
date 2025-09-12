// Clase Padre: Animal
class Animal {
  nombre: string;

  constructor(nombre: string) {
    this.nombre = nombre;
  }

  // Función virtual que deben implementar las subclases
  sonido() {
    return;
  }
}

// Clase Hija: Perro
class Perro extends Animal {
  sonido() {
    console.log("GUAUUUU!");
  }
}

// Clase Hija: Gato
class Gato extends Animal {
  sonido() {
    console.log("MIAUUU!");
  }
}

const printSound = (animal: Animal) => {
  animal.sonido();
};

// Clase Hija: Gato
let miAnimal = new Animal("Tobby");
printSound.sonido(Perro);
let miPerro = new Perro("Ponky");
miPerro.sonido();
let miGato = new Gato("Mishi");
miGato.sonido();

// Ejercicio Extra
// Clase Padre: Empleado
class Empleado {
  id: number;
  nombre: string;
  empleados: Empleado[];

  constructor(id: number, nombre: string) {
      this.id = id;
      this.nombre = nombre;
      this.empleados = [];
  }

  // Métodos específicos de cada clase hija
  agregarEmpleado(empleado: Empleado) {
      this.empleados.push(empleado);
  }

  // Métodos comunes para cada clase hija
  imprimirEmpleados() {
      this.empleados.forEach((empleado) => {
          console.log(`Empleado: ${empleado.nombre}`);
      })
  }
}

// Clase Hija: Gerente
class Gerente extends Empleado {
  constructor(id: number, nombre: string) {
      super(id, nombre);
  }

  // Métodos específicos de Gerente: imprimirEmpleados y coordinarProyectos
  coordinarProyectos() {
      console.log(`${this.nombre} esta coordinando los proyectos de la empresa`);
  }
}

// Clase Hija: GerenteProyectos
class GerenteProyectos extends Empleado {
  proyecto: string;
  constructor(id: number, nombre: string, proyecto: string) {
      super(id, nombre);
      this.proyecto = proyecto;
  }

  // Métodos específicos de GerenteProyectos: imprimirEmpleados y coordinarProyecto
  coordinarProyecto() {
      console.log(`${this.nombre} esta coordinando su proyecto`);
  }
}

// Clase Hija: Programador
class Programador extends Empleado {
  lenguaje: string;
  constructor(id: number, nombre: string, lenguaje: string) {
      super(id, nombre);
      this.lenguaje = lenguaje;
  }

  // Métodos específicos de Programador: imprimirEmpleados y codificar
  codificar() {
      console.log(`${this.nombre} esta programando en ${this.lenguaje}`);
  }

  // Métodos específicos de Programador: imprimirEmpleados y agregarEmpleados
  agregarEmpleado(empleado: Empleado) {
      console.log(
          "Un programador no tiene empleados a su cargo, " +
          empleado.nombre +
          " no se agregara"
      );
  }
}

// Pruebas: Empleados
let miManager = new Gerente(1, "Anthony");
let miGerenteProyectos = new GerenteProyectos(2, "Tony", "Proyecto 1");
let miGerenteProyectos2 = new GerenteProyectos(3, "Hector", "Proyecto 2");
let miProgramador = new Programador(4, "Anthony", "Typescript");
let miProgramador2 = new Programador(5, "Tony", "C++");
let miProgramador3 = new Programador(6, "Hector", "Javascript");
let miProgramador4 = new Programador(7, "Antonio", "Python");

// Agregar empleados al gerente
miManager.agregarEmpleado(miGerenteProyectos);
miManager.agregarEmpleado(miGerenteProyectos2);

// Agregar empleados al gerente de proyectos
miGerenteProyectos.agregarEmpleado(miProgramador);
miGerenteProyectos.agregarEmpleado(miProgramador2);
miGerenteProyectos.agregarEmpleado(miProgramador3);
miGerenteProyectos.agregarEmpleado(miProgramador4);

// Agregar empleados al programador: no se agregan empleados
miProgramador.agregarEmpleado(miProgramador2);

// Codificar programador 
miProgramador.codificar();

// Coordinar proyectos
miGerenteProyectos.coordinarProyecto();
miManager.coordinarProyectos();
miManager.imprimirEmpleados();

// Imprimir empleados
miGerenteProyectos.imprimirEmpleados();
miProgramador.imprimirEmpleados();

