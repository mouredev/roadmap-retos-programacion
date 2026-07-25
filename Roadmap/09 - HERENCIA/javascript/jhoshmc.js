/*
 ! EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
*/
// todo ejercicio
class Animal {
  constructor(nombre) {
    this._nombre = nombre;
  }
  get_Sonido() {}
}

class Perro extends Animal {
  constructor(nombre) {
    super(nombre);
  }
  get_Sonido() {
    console.log(`${this._nombre}: Guau!`);
  }
}

class Gato extends Animal {
  constructor(nombre) {
    super(nombre);
  }
  get_Sonido() {
    console.log(`${this._nombre}: Miau!`);
  }
}

//todo extra
/*
 ! DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
*/

class Empleado {
  constructor(id, nombre, cargo) {
    this._id = id;
    this._nombre = nombre;
    this._cargo = cargo;
  }
  getInfoEmpleado() {
    console.log(
      `\nEmpleado: ${this._id} : ${this._nombre} : cargo : ${this._cargo}`
    );
  }
}

class Gerente extends Empleado {
  constructor(id, nombre, cargo) {
    super(id, nombre, cargo);
    this.personal = [];
  }
  setAgregarPersonal(nuevoP) {
    this.personal.push(nuevoP);
  }
  getPersonal() {
    console.log(`\nGerente: ${this._nombre} con personal a cargo: \n`);
    this.personal.forEach((element) => {
      element.getInfoEmpleado();
    });
  }
}

class GerenteProyectos extends Empleado {
  constructor(id, nombre, cargo) {
    super(id, nombre, cargo);
    this.equipo = [];
    this.proyectos = [];
  }
  setPersonalAcargo(miembro) {
    this.equipo.push(miembro);
  }
  setProyectos(nombreProyecto) {
    this.proyectos.push(nombreProyecto);
  }
  getEquipo() {
    console.log(
      `\nGerente de proyectos ${this._nombre}: miembros en su equipo:\n`
    );
    this.equipo.forEach((element) => {
      element.getInfoEmpleado();
    });
  }
  getProyectos() {
    console.log(
      `\nGerente de proyectos ${this._nombre}: proyectos a su cargo:\n`
    );
    this.proyectos.forEach((element) => {
      console.log(element);
    });
  }
}

class Programador extends Empleado {
  constructor(id, nombre, cargo) {
    super(id, nombre, cargo);
    this._proyectoEnCurso = "ninguno";
  }
  setProyecto(proyecto) {
    this._proyectoEnCurso = proyecto;
  }
  getProyectoEnCurso() {
    console.log(`Programador: ${this._nombre}`);
    console.log(`proyecto en curso: ${this._proyectoEnCurso}`);
  }
}
//todo ejericico
function ejercicio() {
  const chester = new Perro("Chester");
  const lita = new Gato("Lita");
  chester.get_Sonido();
  lita.get_Sonido();
}

ejercicio();

// todo extra

function extra() {
  const manuel = new Gerente("A125", "Manuel Zoto", "Gerente");
  const jonas = new GerenteProyectos(
    "G233",
    "Jonas Marques",
    "Gerente de proyectos"
  );
  const roberto = new Programador("P564", "Roberto Hernandez", "programador");
  manuel.getInfoEmpleado();
  // jonas.getInfoEmpleado();
  // roberto.getInfoEmpleado();
  manuel.setAgregarPersonal(jonas);
  manuel.setAgregarPersonal(roberto);
  manuel.getPersonal();
  jonas.setPersonalAcargo(roberto);
  jonas.setProyectos("cambiar color del boton");
  jonas.setProyectos("reiniciar la pc");
  jonas.getEquipo();
  jonas.getProyectos();
  roberto.setProyecto("cambiar color boton");
  roberto.getProyectoEnCurso();
}

extra();
