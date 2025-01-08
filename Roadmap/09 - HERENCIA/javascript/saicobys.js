/* Concepto de Herencia: Animal, Perro y Gato */

class Animal {
  constructor(nombre) {
    this.nombre = nombre;
  }

  emitirSonido() {
    console.log("Sonido genérico de animal ");
  }
}

class Perro extends Animal {
  emitirSonido() {
    console.log("Guau!");
  }
}

class gato extends Animal {
  emitirSonido() {
    console.log("Miau!");
  }
}

let perro1 = new Perro("Buddy");
let gato1 = new gato("Whiskers");

perro1.emitirSonido();
gato1.emitirSonido();
