// Herencia

class Animal {
  constructor(nombre) {
    this.nombre = nombre;
  }

  hacerSonido() {
    // Este método será implementado por las subclases
  }
}

class Perro extends Animal {
  hacerSonido() {
    return "Guau";
  }
}

class Gato extends Animal {
  hacerSonido() {
    return "Miau";
  }
}

function imprimirSonido(animal) {
  const tipoAnimal = animal.constructor.name;
  console.log(
    `${animal.nombre} mi ${tipoAnimal} hace: ${animal.hacerSonido()}`
  );
}

const miPerro = new Perro("Buddy");
const miGato = new Gato("Whiskers");

imprimirSonido(miPerro);
imprimirSonido(miGato);

// Ejercicio extra

class Empleado {
  constructor(identificador, nombre) {
    this.identificador = identificador;
    this.nombre = nombre;
  }

  realizarTarea() {
    // Este método será implementado por las subclases
  }
}

class Gerente extends Empleado {
  constructor(identificador, nombre, departamento) {
    super(identificador, nombre);
    this.departamento = departamento;
    this.empleadosACargo = [];
  }

  asignarTarea(tarea) {
    console.log(`El gerente ${this.nombre} asigna la tarea: ${tarea}`);
  }

  realizarTarea() {
    console.log(`El gerente ${this.nombre} está gestionando el departamento.`);
  }
}

class GerenteProyecto extends Gerente {
  constructor(identificador, nombre, departamento, proyecto) {
    super(identificador, nombre, departamento);
    this.proyecto = proyecto;
  }

  realizarTarea() {
    console.log(
      `El gerente de proyecto ${this.nombre} está supervisando el proyecto ${this.proyecto}.`
    );
  }
}

class Programador extends Empleado {
  constructor(identificador, nombre, lenguaje) {
    super(identificador, nombre);
    this.lenguaje = lenguaje;
  }

  codificar() {
    console.log(
      `El programador ${this.nombre} está codificando en ${this.lenguaje}.`
    );
  }

  realizarTarea() {
    this.codificar();
  }
}

const gerenteJefe = new Gerente(1, "Ana", "Desarrollo");
const gerenteProyecto1 = new GerenteProyecto(
  2,
  "Carlos",
  "Desarrollo",
  "ProyectoX"
);
const gerenteProyecto2 = new GerenteProyecto(
  3,
  "Diana",
  "Desarrollo",
  "ProyectoY"
);
const gerenteProyecto3 = new GerenteProyecto(4, "Eduardo", "QA", "ProyectoZ");
const programador1 = new Programador(5, "Fernando", "Python");
const programador2 = new Programador(6, "Gabriela", "Java");
const programador3 = new Programador(7, "Hugo", "C++");
const programador4 = new Programador(8, "Isabel", "JavaScript");
const programador5 = new Programador(9, "Javier", "Ruby");
const programador6 = new Programador(10, "Karen", "Swift");

gerenteJefe.empleadosACargo.push(
  gerenteProyecto1,
  gerenteProyecto2,
  gerenteProyecto3,
  programador1,
  programador2,
  programador3,
  programador4,
  programador5,
  programador6
);

gerenteJefe.asignarTarea("Planificación anual");
for (const empleado of gerenteJefe.empleadosACargo) {
  empleado.realizarTarea();
}
