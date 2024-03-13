class Animal {
  constructor(raza, color, nombre) {
    this.raza = raza;
    this.color = color;
    this.nombre = nombre;
  }
  caracteristicas() {
    return `${this.nombre} es un ${this.raza} de color ${this.color}`;
  }
}
class Perro extends Animal {
  constructor(raza, color, nombre) {
    super(raza, color, nombre);
  }
  sonido() {
    return `${super.caracteristicas()} hace Woof Woof.`;
  }
}
class Gato extends Animal {
  constructor(raza, color, nombre) {
    super(raza, color, nombre);
  }
  sonido() {
    return `${super.caracteristicas()} hace Meau.`;
  }
}

let perro = new Perro("Poodle", "blanco", "FeFe");
let gato = new Gato("Abisinio", "negro", "Pesadilla");
console.log(perro.sonido());
console.log(gato.sonido());

/*Extra*/

class Empleado {
  constructor(id, nombre) {
    this.id = id;
    this.nombre = nombre;
    this.empleados = [];
  }
  contratar(empleados) {
    this.empleados.push(empleados);
  }
  print() {
    this.empleados.forEach(empleados => {
      console.log(empleados.nombre);
    });
  }
}
class Gerente extends Empleado {
  coordinar() {
    console.log(`${this.nombre} coordina todos los proyectos de la empresa`);
  }
}
class GerenteProyecto extends Empleado {
  constructor(id, nombre, proyecto) {
    super(id, nombre);
    this.proyecto = proyecto;
  }
  coordinar() {
    console.log(`${this.nombre} coordina su proyecto`);
  }
}
class Programador extends Empleado {
  constructor(id, nombre, lenguaje) {
    super(id, nombre);
    this.lenguaje = lenguaje;
  }
  code() {
    console.log(`${this.nombre} está programando en ${this.lenguaje}`);
  }
  contratar(empleados) {
    console.log(`${this.nombre} no puede contratar. ${empleados.nombre} no será contratado`);
  }
}

const gerente = new Gerente(1, "Luis");
const gerenteProyecto1 = new GerenteProyecto(2, "Pedro", "Proyecto1");
const gerenteProyecto2 = new GerenteProyecto(3, "José", "Proyecto2");
const programador = new Programador(4, "Ángel", "Javascript");
const programador2 = new Programador(5, "Tomas", "Java");
const programador3 = new Programador(6, "Marcos", "Phyton");

gerente.contratar(gerenteProyecto1);
gerente.contratar(gerenteProyecto2);

gerenteProyecto1.contratar(programador);
gerenteProyecto2.contratar(programador2);
gerenteProyecto2.contratar(programador3);

programador.contratar(programador2);

programador.code();
gerente.coordinar();
gerenteProyecto1.coordinar();
gerenteProyecto2.coordinar();
gerente.print();
gerenteProyecto2.print();
programador.print();