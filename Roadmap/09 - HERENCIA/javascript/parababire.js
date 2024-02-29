class Animal {
  constructor(raza, color, nombre) {
    this.raza = raza;
    this.color = color;
    this.nombre = nombre;
  }
  sonido() {
    return `${this.nombre} es un ${this.raza} de color ${this.color}`;
  }
}
class Perro extends Animal {
  constructor(raza, color, nombre) {
    super(raza, color, nombre);
  }
  oir() {
    return `${this.sonido()} hace Woof Woof.`;
  }
}
class Gato extends Animal {
  constructor(raza, color, nombre) {
    super(raza, color, nombre);
  }
  oir() {
    return `${this.sonido()} hace Meau.`;
  }
}

let perro = new Perro("Poodle", "blanco", "FeFe");
let gato = new Gato("Abisinio", "negro", "Pesadilla");
console.log(perro.oir());
console.log(gato.oir());

/*Extra*/

class Empleado {
  constructor(id, nombre) {
    this.id = id;
    this.nombre = nombre;
  }
  informacion() {
    return `ID: ${this.id}, Nombre: ${this.nombre}`;
  }
}
class Gerente extends Empleado {
  constructor(id, nombre) {
    super(id, nombre);
    this.nomina = [];
  }
  contratar(empleado) {
    this.nomina.push(empleado);
  }
  nomina() {
    return `El cargo de ${this.nombre} maneja una nómina de ${this.nomina.length} empleados`
  }
}
class GerenteProyecto extends Empleado {
  constructor(id, nombre, cargo, area) {
    super(id, nombre, cargo);
    this.area = area;
  }
  mostrar() {
    return `${this.identificarse()} de ${this.area}.`;
  }
  nomina() {
    return `El cargo de ${this.cargo} de ${this.area} maneja una nómina de 5 empleados`
  }
}
const gerenteVentas = new Gerente(12075, "Ángel");
console.log(gerenteVentas.informacion());
gerenteVentas.contratar("empleado1");
gerenteVentas.nomina();