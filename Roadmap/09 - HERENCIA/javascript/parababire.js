class Animal {
  constructor(color, nombre) {
    this.color = color;
    this.nombre = nombre;
  }
}
class Perro extends Animal {
  constructor(color, nombre, sonido) {
    super(color, nombre);
    this.sonido = sonido;
  }
  oir() {
    console.log(this.sonido);
  }
}
class Gato extends Animal {
  constructor(color, nombre, sonido) {
    super(color, nombre);
    this.sonido = sonido;
  }
  oir() {
    console.log(this.sonido);
  }
}

let perro = new Perro("blanco", "FeFe", "Wof Wof");
let gato = new Gato("negro", "pesadilla", "Meau");
perro.oir();
gato.oir();