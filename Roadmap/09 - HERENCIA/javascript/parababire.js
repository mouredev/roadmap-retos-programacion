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
  }
  informacion() {
    return `Mi nombre es: ${this.nombre}, número de identificación ${this.id}.`;
  }
}
class Gerente extends Empleado {
  constructor(id, nombre, cargo) {
    super(id, nombre);
    this.cargo = cargo;
    this.nomina = [];
  }
  presentacion() {
    return `${super.informacion()} Manejo el área de ${this.cargo}.`
  }
  contratar(empleado) {
    this.nomina.push(empleado);
  }
  empleados() {
    if (this.nomina.length === 0) {
      return `${this.nombre} aún no ha contratado empleados.`;
    } else if (this.nomina.length === 1) {
      return `${this.nombre} maneja una nómina de ${this.nomina.length} empleado.`;
    } else {
      return `${this.nombre} maneja una nómina de ${this.nomina.length} empleados.`;
    }
  }
}
class GerenteProyecto extends Empleado {
  constructor(id, nombre, cargo) {
    super(id, nombre);
    this.cargo = cargo;
    this.nomina = [];
    this.proyecto = [];
  }
  presentacion() {
    return `${super.informacion()} Manejo el área de ${this.cargo}.`
  }
  contratar(empleado) {
    this.nomina.push(empleado);
  }
  empleados() {
    if (this.nomina.length === 0) {
      return `La ${this.cargo} a cargo de ${this.nombre} aún no ha contratado empleados.`;
    } else if (this.nomina.length === 1) {
      return `La ${this.cargo} a cargo de ${this.nombre} maneja una nómina de ${this.nomina.length} empleado.`;
    } else {
      return `La ${this.cargo} a cargo de ${this.nombre} maneja una nómina de ${this.nomina.length} empleados.`;
    }
  }
  desarrollos(proyecto) {
    return this.proyecto.push(proyecto);
  }
  planificacion() {
    if (this.proyecto.length === 0) {
      return `La ${this.cargo} no está desaarrollando proyectos actualmente.`;
    } else if (this.proyecto.length === 1) {
      return `La ${this.cargo} desarrolla actualmente ${this.proyecto.length} proyecto.`;
    } else {
      return `La ${this.cargo} desarrolla ${this.proyecto.length} proyectos simultaneamente.`;
    }
  }
}
class Programador extends Empleado {
  constructor(id, nombre, cargo, lenguaje) {
    super(id, nombre);
    this.cargo = cargo;
    this.lenguaje = lenguaje;
  }
  presentacion() {
    return `${super.informacion()} Me desempeño como ${this.cargo} y me especializo en ${this.lenguaje}.`
  }
}
const gerenteVentas = new Gerente(12075, "Ángel", "Gerencia");
console.log(gerenteVentas.presentacion());
gerenteVentas.contratar("empleado1");
console.log(gerenteVentas.empleados());
gerenteVentas.contratar("empleado2");
console.log(gerenteVentas.empleados());

const gerenteProyecto = new GerenteProyecto(31023, "Luis", "Gerencia de Proyecto");
console.log(gerenteProyecto.presentacion());
console.log(gerenteProyecto.empleados());
gerenteProyecto.contratar("Empleado1");
console.log(gerenteProyecto.empleados());
gerenteProyecto.contratar("Empleado2");
console.log(gerenteProyecto.empleados());
console.log(gerenteProyecto.planificacion());
gerenteProyecto.desarrollos("Proyecto1");
console.log(gerenteProyecto.planificacion());
gerenteProyecto.desarrollos("Proyecto2");
console.log(gerenteProyecto.planificacion());

const programador = new Programador(25624, "Robert", "Programador", "Javascript");
console.log(programador.presentacion());